from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType, RegisterFunctionType


class Venn(Chart):
    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        # register venn chart.
        self.add_js_funcs(RegisterFunctionType.Venn)

    def set_venn_spec(
        self,
        category_field: types.Optional[str] = None,
        value_field: types.Optional[str] = None,
        circle_opts: types.Optional[opts.VennCircleOpts] = None,
        overlap_opts: types.Optional[opts.VennOverlapOpts] = None,
        label_opts: types.Optional[opts.LabelOpts] = None,
        overlap_label_opts: types.Optional[opts.LabelOpts] = None,
    ):
        self.options.update(
            {
                "type": ChartType.VENN,
                "categoryField": category_field,
                "valueField": value_field,
                "circle": circle_opts,
                "overlap": overlap_opts,
                "label": label_opts,
                "overlapLabel": overlap_label_opts,
            }
        )

        return self
