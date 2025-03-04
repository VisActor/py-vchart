from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Pie(Chart):
    def set_pie_spec(
        self,
        value_field: types.Union[str, types.Sequence[str]] = None,
        outer_radius: types.Optional[types.Numeric] = None,
        inner_radius: types.Optional[types.Numeric] = None,
        start_angle: types.Optional[types.Numeric] = -90,
        end_angle: types.Optional[types.Numeric] = 270,
        center_x: types.Optional[types.Union[types.Numeric, str]] = None,
        center_y: types.Optional[types.Union[types.Numeric, str]] = None,
        category_field: types.Optional[str] = None,
        center_offset: types.Optional[types.Numeric] = None,
        layout_radius: types.Optional[
            types.Union[str, types.Numeric, types.JSFunc]
        ] = None,
        corner_radius: types.Optional[types.Numeric] = None,
        pad_angle: types.Optional[types.Numeric] = None,
        min_angle: types.Optional[types.Numeric] = None,
        pie_opts: types.Optional[opts.PieOpts] = None,
        label_opts: types.Optional[opts.LabelOpts] = None,
        is_show_empty_circle: types.Optional[bool] = None,
        empty_circle_style_opts: types.Optional[opts.BaseStyleOpts] = None,
        is_show_all_zero: types.Optional[bool] = None,
        is_support_negative: types.Optional[bool] = None,
    ):
        self.options.update(
            {
                "type": ChartType.PIE,
                "valueField": value_field,
                "outerRadius": outer_radius,
                "innerRadius": inner_radius,
                "startAngle": start_angle,
                "endAngle": end_angle,
                "centerX": center_x,
                "centerY": center_y,
                "categoryField": category_field,
                "centerOffset": center_offset,
                "layoutRadius": layout_radius,
                "cornerRadius": corner_radius,
                "padAngle": pad_angle,
                "minAngle": min_angle,
                "pie": pie_opts,
                "label": label_opts,
                "emptyPlaceholder": {
                    "showEmptyCircle": is_show_empty_circle,
                    "emptyCircle": empty_circle_style_opts,
                },
                "showAllZero": is_show_all_zero,
                "supportNegative": is_support_negative,
            }
        )

        return self
