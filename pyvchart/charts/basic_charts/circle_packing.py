from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class CirclePacking(Chart):
    def set_circle_packing_spec(
        self,
        category_field: types.Optional[str] = None,
        value_field: types.Optional[str] = None,
        layout_padding: types.Optional[
            types.Union[types.Numeric, types.Sequence[types.Numeric]]
        ] = None,
        is_drill: types.Optional[bool] = None,
        drill_field: types.Optional[str] = None,
        label_opts: types.Optional[opts.LabelOpts] = None,
        circle_packing_opts: types.Optional[opts.CirclePackingOpts] = None,
    ):
        self.options.update(
            {
                "type": ChartType.CIRCLE_PACKING,
                "categoryField": category_field,
                "valueField": value_field,
                "layoutPadding": layout_padding,
                "drill": is_drill,
                "drillField": drill_field,
                "label": label_opts,
                "circlePacking": circle_packing_opts,
            }
        )

        return self
