import _plotly_utils.basevalidators


class BingroupValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="bingroup", parent_name="histogram", **kwargs):
        super(BingroupValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
