from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class CircularProgress(Chart):
    def set_circular_progress_spec(
        self,
        radius: types.Optional[types.Numeric] = None,
        outer_radius: types.Optional[types.Numeric] = None,
        inner_radius: types.Optional[types.Numeric] = None,
        corner_radius: types.Optional[types.Numeric] = None,
        start_angle: types.Optional[types.Numeric] = None,
        end_angle: types.Optional[types.Numeric] = None,
        center_x: types.Optional[types.Union[types.Numeric, str]] = None,
        center_y: types.Optional[types.Union[types.Numeric, str]] = None,
        category_field: types.Optional[types.Union[str, types.Sequence[str]]] = None,
        value_field: types.Optional[str] = None,
        radius_field: types.Optional[str] = None,
        max_value: types.Optional[types.Numeric] = None,
        is_round_cap: types.Optional[bool] = None,
        progress_opts: types.Optional[opts.ProgressOpts] = None,
        track_opts: types.Optional[opts.TrackOpts] = None,
        layout_radius: types.Optional[
            types.Union[str, types.Numeric, types.JSFunc]
        ] = None,
    ):
        self.options.update(
            {
                "type": ChartType.CIRCULAR_PROGRESS,
                "radius": radius,
                "outerRadius": outer_radius,
                "innerRadius": inner_radius,
                "cornerRadius": corner_radius,
                "startAngle": start_angle,
                "endAngle": end_angle,
                "centerX": center_x,
                "centerY": center_y,
                "categoryField": category_field,
                "valueField": value_field,
                "radiusField": radius_field,
                "maxValue": max_value,
                "roundCap": is_round_cap,
                "progress": progress_opts,
                "track": track_opts,
                "layoutRadius": layout_radius,
            }
        )

        return self
