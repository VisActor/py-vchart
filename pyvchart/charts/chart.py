from .. import options as opts
from .. import types
from ..charts.base import Base


class Chart(Base):
    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self._chart_type: types.Optional[str] = None

    def set_data(
        self,
        data: types.Union[types.BaseData, types.Sequence[types.BaseData], None] = None,
    ):
        self.options.update(data=data)
        return self

    def set_global_options(
        self,
        width: types.Optional[types.Numeric] = None,
        height: types.Optional[types.Numeric] = None,
        is_auto_fit: types.Optional[bool] = None,
        background: types.Optional[types.Union[str, dict]] = None,
        padding_opts: types.Padding = None,
        color_opts: types.Sequence[types.Color] = None,
        series_field: types.Optional[str] = None,
        series_style: types.Optional[types.Sequence] = None,
        is_stack: types.Optional[bool] = None,
        stack_value: types.Union[str, types.Numeric, None] = None,
        is_percent: types.Optional[bool] = None,
        is_stack_offset_silhouette: types.Optional[bool] = None,
        invalid_type: types.Optional[str] = None,
        data_key: types.Union[str, types.Sequence[str], types.JSFunc] = None,
        extension_mark_opts: types.Optional[types.Sequence[types.CustomMark]] = None,
        hover_opts: types.Optional[types.Hover] = None,
        select_opts: types.Optional[types.Select] = None,
        animation_appear: types.Optional[opts.AnimationOpts] = None,
        animation_enter: types.Optional[opts.AnimationOpts] = None,
        animation_update: types.Optional[opts.AnimationOpts] = None,
        animation_exit: types.Optional[opts.AnimationOpts] = None,
        animation_disappear: types.Optional[opts.AnimationOpts] = None,
        animation_state: types.Optional[opts.AnimationOpts] = None,
        interaction_opts: types.Optional[types.Sequence[types.Interaction]] = None,
        region_opts: types.Optional[types.Sequence[types.Region]] = None,
        title_opts: types.Optional[types.Title] = None,
        indicator_opts: types.Optional[types.Indicator] = None,
        axes_opts: types.Optional[types.Sequence[types.Axes]] = None,
        markline_opts: types.Optional[types.Sequence[types.MarkLine]] = None,
        markarea_opts: types.Optional[types.Sequence[types.MarkArea]] = None,
        makrpoint_opts: types.Sequence[types.MarkPoint] = None,
        legend_opts: types.Optional[types.Sequence[types.Legend]] = None,
        crosshair_opts: types.Optional[types.Sequence[types.CrossHair]] = None,
        tooltip_opts: types.Optional[types.Tooltip] = None,
        layout_opts: types.Optional[types.Layout] = None,
        player_opts: types.Optional[types.Player] = None,
        scroll_bar_opts: types.Optional[types.Sequence[types.ScrollBar]] = None,
        data_zoom_opts: types.Optional[types.Sequence[types.DataZoom]] = None,
        brush_opts: types.Optional[types.Brush] = None,
        zoom_when_empty_opts: types.Optional[types.ZoomWhenEmpty] = None,
        scales_opts: types.Optional[types.Sequence[types.Scales]] = None,
        custom_mark_opts: types.Optional[types.Sequence[types.CustomMark]] = None,
        theme_opts: types.Optional[types.Theme] = None,
    ):
        self.options.update(
            {
                "width": width,
                "height": height,
                "autoFit": is_auto_fit,
                "background": background,
                "padding": padding_opts,
                "color": color_opts,
                "seriesField": series_field,
                "seriesStyle": series_style,
                "stack": is_stack,
                "stackValue": stack_value,
                "percent": is_percent,
                "stackOffsetSilhouette": is_stack_offset_silhouette,
                "invalidType": invalid_type,
                "dataKey": data_key,
                "extensionMark": extension_mark_opts,
                "hover": hover_opts,
                "select": select_opts,
                "animationAppear": animation_appear,
                "animationEnter": animation_enter,
                "animationUpdate": animation_update,
                "animationExit": animation_exit,
                "animationDisappear": animation_disappear,
                "animationState": animation_state,
                "interactions": interaction_opts,
                "region": region_opts,
                "title": title_opts,
                "indicator": indicator_opts,
                "axes": axes_opts,
                "markLine": markline_opts,
                "markArea": markarea_opts,
                "markPoint": makrpoint_opts,
                "legends": legend_opts,
                "crosshair": crosshair_opts,
                "tooltip": tooltip_opts,
                "layout": layout_opts,
                "player": player_opts,
                "scrollBar": scroll_bar_opts,
                "dataZoom": data_zoom_opts,
                "brush": brush_opts,
                "zoomWhenEmpty": zoom_when_empty_opts,
                "scales": scales_opts,
                "customMark": custom_mark_opts,
                "theme": theme_opts,
            }
        )

        return self


class RectChart(Chart):
    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)

    def set_xy_field(
        self,
        x_field_name: types.Union[str, types.Sequence[str]],
        y_field_name: types.Union[str, types.Sequence[str]],
    ):
        self.options["xField"] = x_field_name
        self.options["yField"] = y_field_name
        return self

    def set_z_field(
        self,
        field_name: types.Union[str, types.Sequence[str]],
    ):
        self.options["zField"] = field_name
        return self
