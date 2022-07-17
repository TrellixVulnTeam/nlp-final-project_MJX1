import sys
import warnings

import six
from pathlib2 import Path

from .import_bind import PostImportHookPatching
from ..binding.frameworks import _patched_call, _Empty, WeightsFileHandler
from ..config import running_remotely
from ..debugging.log import LoggerRoot
from ..model import Framework


class PatchedJoblib(object):
    _patched_joblib = False
    _patched_sk_joblib = False
    _current_task = None

    @staticmethod
    def patch_joblib():
        # try manually
        PatchedJoblib._patch_joblib()
        # register callback
        PostImportHookPatching.add_on_import('joblib',
                                             PatchedJoblib._patch_joblib)
        PostImportHookPatching.add_on_import('sklearn',
                                             PatchedJoblib._patch_joblib)

    @staticmethod
    def _patch_joblib():
        # noinspection PyBroadException
        try:
            if not PatchedJoblib._patched_joblib and 'joblib' in sys.modules:
                PatchedJoblib._patched_joblib = True
                try:
                    import joblib
                except ImportError:
                    joblib = None

                if joblib:
                    joblib.dump = _patched_call(joblib.dump, PatchedJoblib._dump)
                    joblib.load = _patched_call(joblib.load, PatchedJoblib._load)

            if not PatchedJoblib._patched_sk_joblib and 'sklearn' in sys.modules:
                PatchedJoblib._patched_sk_joblib = True
                try:
                    import sklearn
                    # avoid deprecation warning, we must import sklearn before, so we could catch it
                    with warnings.catch_warnings():
                        warnings.simplefilter("ignore")
                        from sklearn.externals import joblib as sk_joblib
                except ImportError:
                    sk_joblib = None

                if sk_joblib:
                    sk_joblib.dump = _patched_call(sk_joblib.dump, PatchedJoblib._dump)
                    sk_joblib.load = _patched_call(sk_joblib.load, PatchedJoblib._load)

        except Exception:
            return False
        return True

    @staticmethod
    def update_current_task(task):
        PatchedJoblib._current_task = task
        PatchedJoblib.patch_joblib()

    @staticmethod
    def _dump(original_fn, obj, f, *args, **kwargs):
        ret = original_fn(obj, f, *args, **kwargs)
        if not PatchedJoblib._current_task:
            return ret

        if isinstance(f, six.string_types):
            filename = f
        elif hasattr(f, 'name'):
            filename = f.name
            # noinspection PyBroadException
            try:
                f.flush()
            except Exception:
                pass
        else:
            filename = None

        # give the model a descriptive name based on the file name
        # noinspection PyBroadException
        try:
            model_name = Path(filename).stem
        except Exception:
            model_name = None
        current_framework = PatchedJoblib.get_model_framework(obj)
        WeightsFileHandler.create_output_model(obj, filename, current_framework,
                                               PatchedJoblib._current_task, singlefile=True, model_name=model_name)
        return ret

    @staticmethod
    def _load(original_fn, f, *args, **kwargs):
        if isinstance(f, six.string_types):
            filename = f
        elif hasattr(f, 'name'):
            filename = f.name
        else:
            filename = None

        if not PatchedJoblib._current_task:
            return original_fn(f, *args, **kwargs)

        # register input model
        empty = _Empty()
        # Hack: disabled
        if False and running_remotely():
            # we assume scikit-learn, for the time being
            current_framework = Framework.scikitlearn
            filename = WeightsFileHandler.restore_weights_file(empty, filename, current_framework,
                                                               PatchedJoblib._current_task)
            model = original_fn(filename or f, *args, **kwargs)
        else:
            # try to load model before registering, in case we fail
            model = original_fn(f, *args, **kwargs)
            current_framework = PatchedJoblib.get_model_framework(model)
            WeightsFileHandler.restore_weights_file(empty, filename, current_framework,
                                                    PatchedJoblib._current_task)

        if empty.trains_in_model:
            # noinspection PyBroadException
            try:
                model.trains_in_model = empty.trains_in_model
            except Exception:
                pass
        return model

    @staticmethod
    def get_model_framework(obj):
        object_orig_module = obj.__module__
        framework = Framework.scikitlearn
        try:
            model = object_orig_module.partition(".")[0]
            if model == 'sklearn':
                framework = Framework.scikitlearn
            elif model == 'xgboost':
                framework = Framework.xgboost
            else:
                framework = Framework.scikitlearn
        except Exception as _:
            LoggerRoot.get_base_logger().debug(
                "Can't get model framework {}, model framework will be: {} ".format(object_orig_module, framework))
        finally:
            return framework
