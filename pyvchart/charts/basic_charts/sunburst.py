from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Sunburst(Chart):
    def set_sunburst_spec(
        self,
        category_field: types.Optional[str] = None,
        value_field: types.Optional[str] = None,
        center_x: types.Optional[types.Union[types.Numeric, str]] = None,
        center_y: types.Optional[types.Union[types.Numeric, str]] = None,
        offset_x: types.Optional[types.Numeric] = None,
        offset_y: types.Optional[types.Numeric] = None,
        start_angle: types.Optional[types.Numeric] = -90,
        end_angle: types.Optional[types.Numeric] = 270,
        inner_radius: types.Optional[types.Numeric] = None,
        outer_radius: types.Optional[types.Numeric] = None,
        gap: types.Optional[
            types.Union[types.Numeric, types.Sequence[types.Numeric]]
        ] = None,
        label_layout_align: types.Optional[str] = None,
        label_layout_rotate: types.Optional[str] = None,
        label_layout_offset: types.Optional[types.Numeric] = None,
        is_label_auto_visible_enable: types.Optional[bool] = None,
        label_auto_visible_circumference: types.Optional[types.Numeric] = None,
        is_drill: types.Optional[bool] = None,
        drill_field: types.Optional[str] = None,
        label_opts: types.Optional[opts.LabelOpts] = None,
        sunburst_opts: types.Optional[opts.SunburstOpts] = None,
    ):
        self.options.update(
            {
                "type": ChartType.SUNBURST,
                "categoryField": category_field,
                "valueField": value_field,
                "centerX": center_x,
                "centerY": center_y,
                "offsetX": offset_x,
                "offsetY": offset_y,
                "startAngle": start_angle,
                "endAngle": end_angle,
                "innerRadius": inner_radius,
                "outerRadius": outer_radius,
                "gap": gap,
                "labelLayout": {
                    "align": label_layout_align,
                    "rotate": label_layout_rotate,
                    "offset": label_layout_offset,
                },
                "labelAutoVisible": {
                    "enable": is_label_auto_visible_enable,
                    "circumference": label_auto_visible_circumference,
                },
                "drill": is_drill,
                "drillField": drill_field,
                "label": label_opts,
                "sunburst": sunburst_opts,
            }
        )

        return self
