from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Correlation(Chart):
    def set_correlation_spec(
        self,
        category_field: types.Optional[str] = None,
        value_field: types.Optional[str] = None,
        size_field: types.Optional[str] = None,
        size_range: types.Optional[types.Sequence] = None,
        center_x: types.Optional[types.Union[types.Numeric, str]] = None,
        center_y: types.Optional[types.Union[types.Numeric, str]] = None,
        inner_radius: types.Optional[types.Numeric] = None,
        outer_radius: types.Optional[types.Numeric] = None,
        start_angle: types.Optional[types.Numeric] = -90,
        end_angle: types.Optional[types.Numeric] = 270,
        center_point_opts: types.Optional[opts.CorrelationCenterPointOpts] = None,
        ripple_point_opts: types.Optional[opts.CorrelationRipplePointOpts] = None,
        center_label_opts: types.Optional[opts.LabelOpts] = None,
        node_point_opts: types.Optional[opts.CorrelationNodePointOpts] = None,
        label_opts: types.Optional[opts.LabelOpts] = None,
        layout_radius: types.Optional[
            types.Union[str, types.Numeric, types.JSFunc]
        ] = None,
    ):
        self.options.update(
            {
                "type": ChartType.CORRELATION,
                "categoryField": category_field,
                "valueField": value_field,
                "sizeField": size_field,
                "sizeRange": size_range,
                "centerX": center_x,
                "centerY": center_y,
                "innerRadius": inner_radius,
                "outerRadius": outer_radius,
                "startAngle": start_angle,
                "endAngle": end_angle,
                "centerPoint": center_point_opts,
                "ripplePoint": ripple_point_opts,
                "centerLabel": center_label_opts,
                "nodePoint": node_point_opts,
                "label": label_opts,
                "layoutRadius": layout_radius,
            }
        )

        return self
