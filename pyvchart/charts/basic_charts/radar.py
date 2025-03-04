from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Radar(Chart):
    def set_radar_spec(
        self,
        category_field: types.Optional[types.Union[str, types.Sequence[str]]] = None,
        value_field: types.Optional[types.Union[str, types.Sequence[str]]] = None,
        outer_radius: types.Optional[types.Numeric] = 0.6,
        inner_radius: types.Optional[types.Numeric] = 0,
        start_angle: types.Optional[types.Numeric] = -90,
        end_angle: types.Optional[types.Numeric] = 270,
        center_x: types.Optional[types.Union[types.Numeric, str]] = None,
        center_y: types.Optional[types.Union[types.Numeric, str]] = None,
        series_mark: str = "area",
        point_opts: types.Optional[opts.PointOpts] = None,
        line_opts: types.Optional[opts.LineOpts] = None,
        area_opts: types.Optional[opts.AreaOpts] = None,
        label_opts: types.Optional[opts.LabelOpts] = None,
        is_mark_overlap: types.Optional[bool] = False,
        point_dis: types.Optional[types.Numeric] = None,
        point_dis_mul: types.Optional[types.Numeric] = None,
        layout_radius: types.Optional[
            types.Union[str, types.Numeric, types.JSFunc]
        ] = None,
    ):
        self.options.update(
            {
                "type": ChartType.RADAR,
                "categoryField": category_field,
                "valueField": value_field,
                "outerRadius": outer_radius,
                "innerRadius": inner_radius,
                "startAngle": start_angle,
                "endAngle": end_angle,
                "centerX": center_x,
                "centerY": center_y,
                "seriesMark": series_mark,
                "point": point_opts,
                "line": line_opts,
                "area": area_opts,
                "label": label_opts,
                "markOverlap": is_mark_overlap,
                "pointDis": point_dis,
                "pointDisMul": point_dis_mul,
                "layoutRadius": layout_radius,
            }
        )

        return self
