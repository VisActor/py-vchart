from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Gauge(Chart):
    def set_gauge_spec(
        self,
        category_field: types.Optional[types.Union[str, types.Sequence[str]]] = None,
        value_field: types.Optional[types.Union[str, types.Sequence[str]]] = None,
        outer_radius: types.Optional[types.Numeric] = None,
        inner_radius: types.Optional[types.Numeric] = None,
        start_angle: types.Optional[types.Numeric] = -90,
        end_angle: types.Optional[types.Numeric] = 270,
        center_x: types.Optional[types.Union[types.Numeric, str]] = None,
        center_y: types.Optional[types.Union[types.Numeric, str]] = None,
        corner_radius: types.Optional[types.Numeric] = None,
        round_cap: types.Optional[types.Union[bool, types.Sequence[bool]]] = None,
        radius_field: types.Optional[str] = None,
        pointer_opts: types.Optional[opts.GaugePointerOpts] = None,
        pin_opts: types.Optional[opts.GaugePinOpts] = None,
        pin_background_opts: types.Optional[opts.GaugePinBackgroundOpts] = None,
        gauge_opts: types.Optional[opts.GaugeOpts] = None,
        layout_radius: types.Optional[
            types.Union[str, types.Numeric, types.JSFunc]
        ] = None,
    ):
        self.options.update(
            {
                "type": ChartType.GAUGE,
                "categoryField": category_field,
                "valueField": value_field,
                "outerRadius": outer_radius,
                "innerRadius": inner_radius,
                "startAngle": start_angle,
                "endAngle": end_angle,
                "centerX": center_x,
                "centerY": center_y,
                "cornerRadius": corner_radius,
                "roundCap": round_cap,
                "radiusField": radius_field,
                "pointer": pointer_opts,
                "pin": pin_opts,
                "pinBackground": pin_background_opts,
                "gauge": gauge_opts,
                "layoutRadius": layout_radius,
            }
        )

        return self
