from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Rose(Chart):
    def set_rose_spec(
        self,
        category_field: types.Optional[types.Union[str, types.Sequence[str]]] = None,
        value_field: types.Optional[types.Union[str, types.Sequence[str]]] = None,
        outer_radius: types.Optional[types.Numeric] = None,
        inner_radius: types.Optional[types.Numeric] = None,
        start_angle: types.Optional[types.Numeric] = -90,
        end_angle: types.Optional[types.Numeric] = 270,
        center_x: types.Optional[types.Union[types.Numeric, str]] = None,
        center_y: types.Optional[types.Union[types.Numeric, str]] = None,
        rose_opts: types.Optional[opts.RoseOpts] = None,
        label_opts: types.Optional[opts.LabelOpts] = None,
        layout_radius: types.Optional[
            types.Union[str, types.Numeric, types.JSFunc]
        ] = None,
    ):
        self.options.update(
            {
                "type": ChartType.ROSE,
                "categoryField": category_field,
                "valueField": value_field,
                "outerRadius": outer_radius,
                "innerRadius": inner_radius,
                "startAngle": start_angle,
                "endAngle": end_angle,
                "centerX": center_x,
                "centerY": center_y,
                "rose": rose_opts,
                "label": label_opts,
                "layoutRadius": layout_radius,
            }
        )

        return self
