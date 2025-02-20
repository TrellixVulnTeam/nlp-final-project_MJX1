"""Python wrappers around TensorFlow ops.

This file is MACHINE GENERATED! Do not edit.
Original C++ source file: ragged_conversion_ops.cc
"""

import collections as _collections
import six as _six

from tensorflow.python import pywrap_tensorflow as _pywrap_tensorflow
from tensorflow.python.eager import context as _context
from tensorflow.python.eager import core as _core
from tensorflow.python.eager import execute as _execute
from tensorflow.python.framework import dtypes as _dtypes
from tensorflow.python.framework import errors as _errors
from tensorflow.python.framework import tensor_shape as _tensor_shape

from tensorflow.core.framework import op_def_pb2 as _op_def_pb2
# Needed to trigger the call to _set_call_cpp_shape_fn.
from tensorflow.python.framework import common_shapes as _common_shapes
from tensorflow.python.framework import op_def_registry as _op_def_registry
from tensorflow.python.framework import ops as _ops
from tensorflow.python.framework import op_def_library as _op_def_library
from tensorflow.python.util.deprecation import deprecated_endpoints
from tensorflow.python.util import dispatch as _dispatch
from tensorflow.python.util.tf_export import tf_export
from tensorflow.python.util.tf_export import kwarg_only as _kwarg_only
from tensorflow.tools.docs import doc_controls as _doc_controls


_ragged_tensor_from_variant_outputs = ["output_nested_splits",
                                      "output_dense_values"]
_RaggedTensorFromVariantOutput = _collections.namedtuple(
    "RaggedTensorFromVariant", _ragged_tensor_from_variant_outputs)


def ragged_tensor_from_variant(encoded_ragged, input_ragged_rank, output_ragged_rank, Tvalues, Tsplits, name=None):
  r"""Decodes a `variant` Tensor into a `RaggedTensor`.

  Decodes the given `variant` Tensor and returns a `RaggedTensor`. The input
  could be a scalar, meaning it encodes a single `RaggedTensor` with ragged_rank
  `output_ragged_rank`. It could also have an arbitrary rank, in which case each
  element is decoded into a `RaggedTensor` with ragged_rank `input_ragged_rank`
  and these are then stacked according to the input shape to output a single
  `RaggedTensor` with ragged_rank `output_ragged_rank`. Each `variant` element in
  the input Tensor is decoded by retrieving from the element a 1-D `variant`
  Tensor with `input_ragged_rank + 1` Tensors, corresponding to the splits and
  values of the decoded `RaggedTensor`. If `input_ragged_rank` is -1, then it is
  inferred as `output_ragged_rank` - `rank(encoded_ragged)`. See
  `RaggedTensorToVariant` for the corresponding encoding logic.

  Args:
    encoded_ragged: A `Tensor` of type `variant`.
      A `variant` Tensor containing encoded `RaggedTensor`s.
    input_ragged_rank: An `int` that is `>= -1`.
      The ragged rank of each encoded `RaggedTensor` component in the input. If set to
      -1, this is inferred as `output_ragged_rank` - `rank(encoded_ragged)`
    output_ragged_rank: An `int` that is `>= 1`.
      The expected ragged rank of the output `RaggedTensor`. The following must hold:
      `output_ragged_rank = rank(encoded_ragged) + input_ragged_rank`.
    Tvalues: A `tf.DType`.
    Tsplits: A `tf.DType` from: `tf.int32, tf.int64`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output_nested_splits, output_dense_values).

    output_nested_splits: A list of `output_ragged_rank` `Tensor` objects with type `Tsplits`.
    output_dense_values: A `Tensor` of type `Tvalues`.
  """
  _ctx = _context._context or _context.context()
  if _ctx is not None and _ctx._thread_local_data.is_eager:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._thread_local_data.device_name,
        "RaggedTensorFromVariant", name, _ctx._post_execution_callbacks,
        encoded_ragged, "input_ragged_rank", input_ragged_rank,
        "output_ragged_rank", output_ragged_rank, "Tvalues", Tvalues,
        "Tsplits", Tsplits)
      _result = _RaggedTensorFromVariantOutput._make(_result)
      return _result
    except _core._FallbackException:
      try:
        return ragged_tensor_from_variant_eager_fallback(
            encoded_ragged, input_ragged_rank=input_ragged_rank,
            output_ragged_rank=output_ragged_rank, Tvalues=Tvalues,
            Tsplits=Tsplits, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)
  # Add nodes to the TensorFlow graph.
  input_ragged_rank = _execute.make_int(input_ragged_rank, "input_ragged_rank")
  output_ragged_rank = _execute.make_int(output_ragged_rank, "output_ragged_rank")
  Tvalues = _execute.make_type(Tvalues, "Tvalues")
  Tsplits = _execute.make_type(Tsplits, "Tsplits")
  _, _, _op = _op_def_lib._apply_op_helper(
        "RaggedTensorFromVariant", encoded_ragged=encoded_ragged,
                                   input_ragged_rank=input_ragged_rank,
                                   output_ragged_rank=output_ragged_rank,
                                   Tvalues=Tvalues, Tsplits=Tsplits,
                                   name=name)
  _result = _op.outputs[:]
  _inputs_flat = _op.inputs
  _attrs = ("input_ragged_rank", _op.get_attr("input_ragged_rank"),
            "output_ragged_rank", _op.get_attr("output_ragged_rank"),
            "Tvalues", _op.get_attr("Tvalues"), "Tsplits",
            _op.get_attr("Tsplits"))
  _execute.record_gradient(
      "RaggedTensorFromVariant", _inputs_flat, _attrs, _result, name)
  _result = [_result[:output_ragged_rank]] + _result[output_ragged_rank:]
  _result = _RaggedTensorFromVariantOutput._make(_result)
  return _result

def RaggedTensorFromVariant(encoded_ragged, input_ragged_rank, output_ragged_rank, Tvalues, Tsplits, name=None):
  return ragged_tensor_from_variant(encoded_ragged=encoded_ragged, input_ragged_rank=input_ragged_rank, output_ragged_rank=output_ragged_rank, Tvalues=Tvalues, Tsplits=Tsplits, name=name)
RaggedTensorFromVariant.__doc__ = ragged_tensor_from_variant.__doc__
RaggedTensorFromVariant = _doc_controls.do_not_generate_docs(_kwarg_only(RaggedTensorFromVariant))
tf_export("raw_ops.RaggedTensorFromVariant")(RaggedTensorFromVariant)


def ragged_tensor_from_variant_eager_fallback(encoded_ragged, input_ragged_rank, output_ragged_rank, Tvalues, Tsplits, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function ragged_tensor_from_variant
  """
  _ctx = ctx if ctx else _context.context()
  input_ragged_rank = _execute.make_int(input_ragged_rank, "input_ragged_rank")
  output_ragged_rank = _execute.make_int(output_ragged_rank, "output_ragged_rank")
  Tvalues = _execute.make_type(Tvalues, "Tvalues")
  Tsplits = _execute.make_type(Tsplits, "Tsplits")
  encoded_ragged = _ops.convert_to_tensor(encoded_ragged, _dtypes.variant)
  _inputs_flat = [encoded_ragged]
  _attrs = ("input_ragged_rank", input_ragged_rank, "output_ragged_rank",
  output_ragged_rank, "Tvalues", Tvalues, "Tsplits", Tsplits)
  _result = _execute.execute(b"RaggedTensorFromVariant", output_ragged_rank +
                             1, inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                             name=name)
  _execute.record_gradient(
      "RaggedTensorFromVariant", _inputs_flat, _attrs, _result, name)
  _result = [_result[:output_ragged_rank]] + _result[output_ragged_rank:]
  _result = _RaggedTensorFromVariantOutput._make(_result)
  return _result


_ragged_tensor_to_sparse_outputs = ["sparse_indices", "sparse_values",
                                   "sparse_dense_shape"]
_RaggedTensorToSparseOutput = _collections.namedtuple(
    "RaggedTensorToSparse", _ragged_tensor_to_sparse_outputs)


def ragged_tensor_to_sparse(rt_nested_splits, rt_dense_values, name=None):
  r"""Converts a `RaggedTensor` into a `SparseTensor` with the same values.

  input=ragged.from_nested_row_splits(rt_dense_values, rt_nested_splits)
  output=SparseTensor(indices=sparse_indices, values=sparse_values,
                      dense_shape=sparse_dense_shape)

  Args:
    rt_nested_splits: A list of at least 1 `Tensor` objects with the same type in: `int32`, `int64`.
      The `row_splits` for the `RaggedTensor`.
    rt_dense_values: A `Tensor`. The `flat_values` for the `RaggedTensor`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (sparse_indices, sparse_values, sparse_dense_shape).

    sparse_indices: A `Tensor` of type `int64`.
    sparse_values: A `Tensor`. Has the same type as `rt_dense_values`.
    sparse_dense_shape: A `Tensor` of type `int64`.
  """
  _ctx = _context._context or _context.context()
  if _ctx is not None and _ctx._thread_local_data.is_eager:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._thread_local_data.device_name,
        "RaggedTensorToSparse", name, _ctx._post_execution_callbacks,
        rt_nested_splits, rt_dense_values)
      _result = _RaggedTensorToSparseOutput._make(_result)
      return _result
    except _core._FallbackException:
      try:
        return ragged_tensor_to_sparse_eager_fallback(
            rt_nested_splits, rt_dense_values, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)
  # Add nodes to the TensorFlow graph.
  if not isinstance(rt_nested_splits, (list, tuple)):
    raise TypeError(
        "Expected list for 'rt_nested_splits' argument to "
        "'ragged_tensor_to_sparse' Op, not %r." % rt_nested_splits)
  _attr_RAGGED_RANK = len(rt_nested_splits)
  _, _, _op = _op_def_lib._apply_op_helper(
        "RaggedTensorToSparse", rt_nested_splits=rt_nested_splits,
                                rt_dense_values=rt_dense_values, name=name)
  _result = _op.outputs[:]
  _inputs_flat = _op.inputs
  _attrs = ("RAGGED_RANK", _op.get_attr("RAGGED_RANK"), "T",
            _op.get_attr("T"), "Tsplits", _op.get_attr("Tsplits"))
  _execute.record_gradient(
      "RaggedTensorToSparse", _inputs_flat, _attrs, _result, name)
  _result = _RaggedTensorToSparseOutput._make(_result)
  return _result

def RaggedTensorToSparse(rt_nested_splits, rt_dense_values, name=None):
  return ragged_tensor_to_sparse(rt_nested_splits=rt_nested_splits, rt_dense_values=rt_dense_values, name=name)
RaggedTensorToSparse.__doc__ = ragged_tensor_to_sparse.__doc__
RaggedTensorToSparse = _doc_controls.do_not_generate_docs(_kwarg_only(RaggedTensorToSparse))
tf_export("raw_ops.RaggedTensorToSparse")(RaggedTensorToSparse)


def ragged_tensor_to_sparse_eager_fallback(rt_nested_splits, rt_dense_values, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function ragged_tensor_to_sparse
  """
  _ctx = ctx if ctx else _context.context()
  if not isinstance(rt_nested_splits, (list, tuple)):
    raise TypeError(
        "Expected list for 'rt_nested_splits' argument to "
        "'ragged_tensor_to_sparse' Op, not %r." % rt_nested_splits)
  _attr_RAGGED_RANK = len(rt_nested_splits)
  _attr_T, (rt_dense_values,) = _execute.args_to_matching_eager([rt_dense_values], _ctx)
  _attr_Tsplits, rt_nested_splits = _execute.args_to_matching_eager(list(rt_nested_splits), _ctx, _dtypes.int64)
  _inputs_flat = list(rt_nested_splits) + [rt_dense_values]
  _attrs = ("RAGGED_RANK", _attr_RAGGED_RANK, "T", _attr_T, "Tsplits",
  _attr_Tsplits)
  _result = _execute.execute(b"RaggedTensorToSparse", 3, inputs=_inputs_flat,
                             attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "RaggedTensorToSparse", _inputs_flat, _attrs, _result, name)
  _result = _RaggedTensorToSparseOutput._make(_result)
  return _result


def ragged_tensor_to_variant(rt_nested_splits, rt_dense_values, batched_input, name=None):
  r"""Encodes a `RaggedTensor` into a `variant` Tensor.

  
  Encodes the given `RaggedTensor` and returns a `variant` Tensor. If
  `batched_input` is True, then input `RaggedTensor` is unbatched along the
  zero-th dimension, each component `RaggedTensor` is encoded into a scalar
  `variant` Tensor, and these are stacked to return a 1-D `variant` Tensor.
  If `batched_input` is False, then the input `RaggedTensor` is encoded as is and
  a scalar `variant` Tensor is returned. A `RaggedTensor` is encoded by first
  creating a 1-D `variant` Tensor with `ragged_rank + 1` elements, containing the
  splits and values Tensors of the `RaggedTensor`. Then the 1-D `variant` Tensor
  is wrapped in a scalar `variant` Tensor. See `RaggedTensorFromVariant` for the
  corresponding decoding logic.

  Args:
    rt_nested_splits: A list of at least 1 `Tensor` objects with the same type in: `int32`, `int64`.
      A list of one or more Tensors representing the splits of the input
      `RaggedTensor`.
    rt_dense_values: A `Tensor`.
      A Tensor representing the values of the input `RaggedTensor`.
    batched_input: A `bool`.
      A `bool` denoting whether the input is a batched `RaggedTensor`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """
  _ctx = _context._context or _context.context()
  if _ctx is not None and _ctx._thread_local_data.is_eager:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._thread_local_data.device_name,
        "RaggedTensorToVariant", name, _ctx._post_execution_callbacks,
        rt_nested_splits, rt_dense_values, "batched_input", batched_input)
      return _result
    except _core._FallbackException:
      try:
        return ragged_tensor_to_variant_eager_fallback(
            rt_nested_splits, rt_dense_values, batched_input=batched_input,
            name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)
  # Add nodes to the TensorFlow graph.
  if not isinstance(rt_nested_splits, (list, tuple)):
    raise TypeError(
        "Expected list for 'rt_nested_splits' argument to "
        "'ragged_tensor_to_variant' Op, not %r." % rt_nested_splits)
  _attr_RAGGED_RANK = len(rt_nested_splits)
  batched_input = _execute.make_bool(batched_input, "batched_input")
  _, _, _op = _op_def_lib._apply_op_helper(
        "RaggedTensorToVariant", rt_nested_splits=rt_nested_splits,
                                 rt_dense_values=rt_dense_values,
                                 batched_input=batched_input, name=name)
  _result = _op.outputs[:]
  _inputs_flat = _op.inputs
  _attrs = ("RAGGED_RANK", _op.get_attr("RAGGED_RANK"), "Tvalues",
            _op.get_attr("Tvalues"), "Tsplits", _op.get_attr("Tsplits"),
            "batched_input", _op.get_attr("batched_input"))
  _execute.record_gradient(
      "RaggedTensorToVariant", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

def RaggedTensorToVariant(rt_nested_splits, rt_dense_values, batched_input, name=None):
  return ragged_tensor_to_variant(rt_nested_splits=rt_nested_splits, rt_dense_values=rt_dense_values, batched_input=batched_input, name=name)
RaggedTensorToVariant.__doc__ = ragged_tensor_to_variant.__doc__
RaggedTensorToVariant = _doc_controls.do_not_generate_docs(_kwarg_only(RaggedTensorToVariant))
tf_export("raw_ops.RaggedTensorToVariant")(RaggedTensorToVariant)


def ragged_tensor_to_variant_eager_fallback(rt_nested_splits, rt_dense_values, batched_input, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function ragged_tensor_to_variant
  """
  _ctx = ctx if ctx else _context.context()
  if not isinstance(rt_nested_splits, (list, tuple)):
    raise TypeError(
        "Expected list for 'rt_nested_splits' argument to "
        "'ragged_tensor_to_variant' Op, not %r." % rt_nested_splits)
  _attr_RAGGED_RANK = len(rt_nested_splits)
  batched_input = _execute.make_bool(batched_input, "batched_input")
  _attr_Tvalues, (rt_dense_values,) = _execute.args_to_matching_eager([rt_dense_values], _ctx)
  _attr_Tsplits, rt_nested_splits = _execute.args_to_matching_eager(list(rt_nested_splits), _ctx)
  _inputs_flat = list(rt_nested_splits) + [rt_dense_values]
  _attrs = ("RAGGED_RANK", _attr_RAGGED_RANK, "Tvalues", _attr_Tvalues,
  "Tsplits", _attr_Tsplits, "batched_input", batched_input)
  _result = _execute.execute(b"RaggedTensorToVariant", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "RaggedTensorToVariant", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

def _InitOpDefLibrary(op_list_proto_bytes):
  op_list = _op_def_pb2.OpList()
  op_list.ParseFromString(op_list_proto_bytes)
  _op_def_registry.register_op_list(op_list)
  op_def_lib = _op_def_library.OpDefLibrary()
  op_def_lib.add_op_list(op_list)
  return op_def_lib
# op {
#   name: "RaggedTensorFromVariant"
#   input_arg {
#     name: "encoded_ragged"
#     type: DT_VARIANT
#   }
#   output_arg {
#     name: "output_nested_splits"
#     type_attr: "Tsplits"
#     number_attr: "output_ragged_rank"
#   }
#   output_arg {
#     name: "output_dense_values"
#     type_attr: "Tvalues"
#   }
#   attr {
#     name: "input_ragged_rank"
#     type: "int"
#     has_minimum: true
#     minimum: -1
#   }
#   attr {
#     name: "output_ragged_rank"
#     type: "int"
#     has_minimum: true
#     minimum: 1
#   }
#   attr {
#     name: "Tvalues"
#     type: "type"
#   }
#   attr {
#     name: "Tsplits"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_INT32
#         type: DT_INT64
#       }
#     }
#   }
# }
# op {
#   name: "RaggedTensorToSparse"
#   input_arg {
#     name: "rt_nested_splits"
#     type_attr: "Tsplits"
#     number_attr: "RAGGED_RANK"
#   }
#   input_arg {
#     name: "rt_dense_values"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "sparse_indices"
#     type: DT_INT64
#   }
#   output_arg {
#     name: "sparse_values"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "sparse_dense_shape"
#     type: DT_INT64
#   }
#   attr {
#     name: "RAGGED_RANK"
#     type: "int"
#     has_minimum: true
#     minimum: 1
#   }
#   attr {
#     name: "T"
#     type: "type"
#   }
#   attr {
#     name: "Tsplits"
#     type: "type"
#     default_value {
#       type: DT_INT64
#     }
#     allowed_values {
#       list {
#         type: DT_INT32
#         type: DT_INT64
#       }
#     }
#   }
# }
# op {
#   name: "RaggedTensorToVariant"
#   input_arg {
#     name: "rt_nested_splits"
#     type_attr: "Tsplits"
#     number_attr: "RAGGED_RANK"
#   }
#   input_arg {
#     name: "rt_dense_values"
#     type_attr: "Tvalues"
#   }
#   output_arg {
#     name: "encoded_ragged"
#     type: DT_VARIANT
#   }
#   attr {
#     name: "RAGGED_RANK"
#     type: "int"
#     has_minimum: true
#     minimum: 1
#   }
#   attr {
#     name: "Tvalues"
#     type: "type"
#   }
#   attr {
#     name: "Tsplits"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_INT32
#         type: DT_INT64
#       }
#     }
#   }
#   attr {
#     name: "batched_input"
#     type: "bool"
#   }
# }
_op_def_lib = _InitOpDefLibrary(b"\n\362\001\n\027RaggedTensorFromVariant\022\022\n\016encoded_ragged\030\025\0323\n\024output_nested_splits\"\007Tsplits*\022output_ragged_rank\032\036\n\023output_dense_values\"\007Tvalues\"%\n\021input_ragged_rank\022\003int(\0010\377\377\377\377\377\377\377\377\377\001\"\035\n\022output_ragged_rank\022\003int(\0010\001\"\017\n\007Tvalues\022\004type\"\027\n\007Tsplits\022\004type:\006\n\0042\002\003\t\n\326\001\n\024RaggedTensorToSparse\022(\n\020rt_nested_splits\"\007Tsplits*\013RAGGED_RANK\022\024\n\017rt_dense_values\"\001T\032\022\n\016sparse_indices\030\t\032\022\n\rsparse_values\"\001T\032\026\n\022sparse_dense_shape\030\t\"\026\n\013RAGGED_RANK\022\003int(\0010\001\"\t\n\001T\022\004type\"\033\n\007Tsplits\022\004type\032\0020\t:\006\n\0042\002\003\t\n\312\001\n\025RaggedTensorToVariant\022(\n\020rt_nested_splits\"\007Tsplits*\013RAGGED_RANK\022\032\n\017rt_dense_values\"\007Tvalues\032\022\n\016encoded_ragged\030\025\"\026\n\013RAGGED_RANK\022\003int(\0010\001\"\017\n\007Tvalues\022\004type\"\027\n\007Tsplits\022\004type:\006\n\0042\002\003\t\"\025\n\rbatched_input\022\004bool")
