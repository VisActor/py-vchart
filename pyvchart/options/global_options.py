from ..commons.utils import JsCode
from ..globals import CurrentConfig
from ..options.series_options import (
    AnimationOpts,
    BasicOpts,
    JSFunc,
    Numeric,
    Optional,
    Union,
    Sequence,
)


class BaseHtmlOrReactOpts(BasicOpts):
    def __init__(
        self,
        dom: Union[str, JSFunc] = None,
        id_: Optional[str] = None,
        is_pointer_events: bool = False,
        container: Union[str, JSFunc] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        style: Union[str, JSFunc] = None,
        is_visible: bool = False,
        anchor_type: str = "boundsLeftTop",
    ):
        self.opts: dict = {
            "dom": dom,
            "id_": id_,
            "pointerEvents": is_pointer_events,
            "container": container,
            "width": width,
            "height": height,
            "style": style,
            "visible": is_visible,
            "anchorType": anchor_type,
        }


class BaseBorderOpts(BasicOpts):
    def __init__(
        self,
        stroke: Optional[JSFunc] = None,
        stroke_opacity: Optional[int] = None,
        line_dash: Optional[Sequence[int]] = None,
        line_dash_offset: Optional[int] = None,
        line_width: Optional[int] = None,
        distance: Optional[int] = None,
    ):
        self.opts: dict = {
            "stroke": stroke,
            "strokeOpacity": stroke_opacity,
            "lineDash": line_dash,
            "lineDashOffset": line_dash_offset,
            "lineWidth": line_width,
            "distance": distance,
        }


class BaseStyleOpts(BasicOpts):
    def __init__(
        self,
        corner_radius: Optional[Union[Numeric, Sequence[Numeric]]] = None,
        length: Optional[Union[Numeric, Sequence[Numeric]]] = None,
        width: Optional[Numeric] = None,
        height: Optional[Numeric] = None,
        font_size: Optional[Numeric] = None,
        fill: Union[str, dict] = None,
        fill_opacity: Optional[Union[Numeric, JSFunc]] = None,
        shadow_blur: Optional[Numeric] = None,
        shadow_color: Optional[str] = None,
        shadow_offset_x: Optional[Numeric] = None,
        shadow_offset_y: Optional[Numeric] = None,
        background: Optional[JSFunc] = None,
        stroke: Optional[Union[JSFunc, dict]] = None,
        stroke_opacity: Optional[Numeric] = None,
        line_dash: Optional[Sequence[Numeric]] = None,
        line_dash_offset: Optional[Numeric] = None,
        line_width: Optional[Numeric] = None,
        line_cap: Optional[str] = None,
        line_join: Optional[str] = None,
        miter_limit: Optional[Numeric] = None,
        outer_border: Optional[BaseBorderOpts] = None,
        inner_border: Optional[BaseBorderOpts] = None,
        inner_padding: Optional[Numeric] = None,
        outer_padding: Optional[Numeric] = None,
        opacity: Optional[Numeric] = None,
        cursor: Optional[str] = None,
        text: Optional[str] = None,
        texture: Optional[str] = None,
        texture_color: Optional[str] = None,
        texture_size: Optional[Numeric] = None,
        texture_padding: Optional[Numeric] = None,
        is_pickable: Optional[bool] = None,
        is_children_pickable: bool = None,
        is_keep_dir_in_3d: Optional[bool] = None,
        z_index: Optional[Numeric] = None,
        is_visible: Optional[bool] = None,
        dx: Optional[Numeric] = None,
        dy: Optional[Numeric] = None,
        angle: Optional[Numeric] = None,
        scale_x: Optional[Numeric] = None,
        scale_y: Optional[Numeric] = None,
        scale_center: Union[Sequence[Numeric], Sequence[str]] = None,
        pick_stroke_buffer: Optional[Numeric] = None,
        bounds_padding: Union[Numeric, Sequence] = None,
        html: BaseHtmlOrReactOpts = None,
        react: BaseHtmlOrReactOpts = None,
    ):
        self.opts: dict = {
            "cornerRadius": corner_radius,
            "length": length,
            "width": width,
            "height": height,
            "fontSize": font_size,
            "fill": fill,
            "fillOpacity": fill_opacity,
            "shadowBlur": shadow_blur,
            "shadowColor": shadow_color,
            "shadowOffsetX": shadow_offset_x,
            "shadowOffsetY": shadow_offset_y,
            "background": background,
            "stroke": stroke,
            "strokeOpacity": stroke_opacity,
            "lineDash": line_dash,
            "lineDashOffset": line_dash_offset,
            "lineWidth": line_width,
            "lineCap": line_cap,
            "lineJoin": line_join,
            "miterLimit": miter_limit,
            "outerBorder": outer_border,
            "innerBorder": inner_border,
            "innerPadding": inner_padding,
            "outerPadding": outer_padding,
            "opacity": opacity,
            "cursor": cursor,
            "text": text,
            "texture": texture,
            "textureColor": texture_color,
            "textureSize": texture_size,
            "texturePadding": texture_padding,
            "isPickable": is_pickable,
            "isChildrenPickable": is_children_pickable,
            "keepDirIn3d": is_keep_dir_in_3d,
            "zIndex": z_index,
            "visible": is_visible,
            "dx": dx,
            "dy": dy,
            "angle": angle,
            "scaleX": scale_x,
            "scaleY": scale_y,
            "scaleCenter": scale_center,
            "pickStrokeBuffer": pick_stroke_buffer,
            "boundsPadding": bounds_padding,
            "html": html,
            "react": react,
        }


class BaseStateOpts(BasicOpts):
    def __init__(
        self,
        active_opts: BaseStyleOpts = None,
        hover_opts: BaseStyleOpts = None,
        hover_reverse_opts: BaseStyleOpts = None,
        selected_opts: BaseStyleOpts = None,
        selected_reverse_opts: BaseStyleOpts = None,
        # for compatible with the state configuration in DiscreteLegendItem
        unselected_opts: BaseStyleOpts = None,
        selected_hover_opts: BaseStyleOpts = None,
        unselected_reverse_opts: BaseStyleOpts = None,
    ):
        self.opts: dict = {
            "active": active_opts,
            "hover": hover_opts,
            "hover_reverse": hover_reverse_opts,
            "selected": selected_opts,
            "selected_reverse": selected_reverse_opts,
            # for compatible with the state configuration in DiscreteLegendItem
            "unselected": unselected_opts,
            "selectedHover": selected_hover_opts,
            "unSelectedHover": unselected_reverse_opts,
        }


class TextConfigTextOpts(BasicOpts):
    def __init__(
        self,
        text: Union[str, int] = None,
        fill: Optional[str] = None,
        stroke: Optional[str] = None,
        line_width: Optional[Numeric] = None,
        fill_opacity: Optional[Numeric] = None,
        stroke_opacity: Optional[Numeric] = None,
        font_size: Optional[int] = None,
        font_family: Optional[str] = None,
        font_weight: Union[str, Sequence[str]] = None,
        font_style: str = "normal",
        is_underline: Optional[bool] = None,
        is_line_though: Optional[bool] = None,
        text_decoration: Optional[str] = None,
        script: Optional[str] = None,
        direction: Optional[str] = None,
        line_height: Optional[Numeric] = None,
        text_align: Optional[str] = None,
        text_baseline: Optional[str] = None,
        opacity: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "text": text,
            "fill": fill,
            "stroke": stroke,
            "lineWidth": line_width,
            "fillOpacity": fill_opacity,
            "strokeOpacity": stroke_opacity,
            "fontSize": font_size,
            "fontFamily": font_family,
            "fontWeight": font_weight,
            "fontStyle": font_style,
            "underline": is_underline,
            "lineThrough": is_line_though,
            "textDecoration": text_decoration,
            "script": script,
            "direction": direction,
            "lineHeight": line_height,
            "textAlign": text_align,
            "textBaseline": text_baseline,
            "opacity": opacity,
        }


class TextConfigImageOpts(BasicOpts):
    def __init__(
        self,
        image: Optional[JSFunc] = None,
        width: Optional[Numeric] = None,
        height: Optional[Numeric] = None,
        margin: Optional[Union[int, Sequence[int]]] = None,
        background_show_mode: Optional[str] = None,
        background_fill: Optional[str] = None,
        background_fill_opacity: Optional[Numeric] = None,
        background_stroke: Optional[str] = None,
        background_stroke_opacity: Optional[Numeric] = None,
        background_radius: Optional[Numeric] = None,
        background_width: Optional[Numeric] = None,
        background_height: Optional[Numeric] = None,
        hover_image: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "image": image,
            "width": width,
            "height": height,
            "margin": margin,
            "backgroundShowMode": background_show_mode,
            "backgroundFill": background_fill,
            "backgroundFillOpacity": background_fill_opacity,
            "backgroundStroke": background_stroke,
            "backgroundStrokeOpacity": background_stroke_opacity,
            "backgroundRadius": background_radius,
            "backgroundWidth": background_width,
            "backgroundHeight": background_height,
            "hoverImage": hover_image,
        }


class TitleTextCharacterOpts(BasicOpts):
    def __init__(
        self,
        type_: Optional[str] = None,
        text_opts: Optional[TextConfigTextOpts] = None,
        image_opts: Optional[TextConfigImageOpts] = None,
    ):
        self.opts = None
        if type_ == "text" and text_opts:
            self.opts = {"type": type_}
            self.opts.update(text_opts.opts)
        elif type_ == "image" and image_opts:
            self.opts = {"type": type_}
            self.opts.update(image_opts.opts)


class BaseTitleTextStyleOpts(BasicOpts):
    def __init__(
        self,
        type_: Optional[str] = None,
        text: Union[str, int, Sequence[str]] = None,
        font_size: Optional[int] = None,
        font_family: Optional[str] = None,
        font_weight: Union[str, Sequence[str]] = None,
        font_style: Optional[str] = "normal",
        font_variant: Union[str, int] = None,
        line_height: Optional[int] = None,
        text_align: Optional[str] = None,
        text_baseline: Optional[str] = None,
        max_line_width: Optional[int] = None,
        ellipsis_: Optional[str] = "...",
        suffix_position: Optional[str] = "end",
        is_underline: Optional[bool] = None,
        is_line_through: Optional[bool] = None,
        direction: Optional[str] = "horizontal",
        word_break: Optional[str] = "break-word",
        is_keep_dir_in_3d: Optional[bool] = None,
        align: Optional[str] = None,
        vertical_align: Optional[str] = None,
        height_limit: Optional[int] = None,
        line_clamp: Optional[int] = None,
        character: Optional[Sequence[TitleTextCharacterOpts]] = None,
        base_style_opts: BaseStyleOpts = None,
    ):
        self.opts: dict = {}

        if base_style_opts:
            self.opts.update(base_style_opts.opts)

        self.opts.update(
            {
                "type": type_,
                "text": text,
                "fontSize": font_size,
                "fontFamily": font_family,
                "fontWeight": font_weight,
                "fontStyle": font_style,
                "fontVariant": font_variant,
                "lineHeight": line_height,
                "textAlign": text_align,
                "textBaseline": text_baseline,
                "maxLineWidth": max_line_width,
                "ellipsis": ellipsis_,
                "suffixPosition": suffix_position,
                "underline": is_underline,
                "lineThrough": is_line_through,
                "direction": direction,
                "wordBreak": word_break,
                "keepDirIn3D": is_keep_dir_in_3d,
                "align": align,
                "verticalAlign": vertical_align,
                "heightLimit": height_limit,
                "lineClamp": line_clamp,
                "character": character,
            }
        )


class BaseSymbolOpts(BasicOpts):
    def __init__(
        self,
        is_visible: Optional[bool] = None,
        symbol_type: Optional[str] = None,
        size: Optional[Numeric] = None,
        ref_x: Optional[Numeric] = None,
        ref_y: Optional[Numeric] = None,
        ref_angle: Optional[Numeric] = None,
        is_clip: Optional[bool] = None,
        style_opts: BaseStyleOpts = None,
    ):
        self.opts: dict = {
            "visible": is_visible,
            "symbolType": symbol_type,
            "size": size,
            "refX": ref_x,
            "refY": ref_y,
            "refAngle": ref_angle,
            "clip": is_clip,
            "style": style_opts,
        }


class LabelRichTextConfigOpts(BasicOpts):
    def __init__(
        self,
        type_: Optional[str] = None,
        text_opts: Optional[TextConfigTextOpts] = None,
        image_opts: Optional[TextConfigImageOpts] = None,
    ):
        self.opts = None
        if type_ == "text" and text_opts:
            self.opts = {"type": type_}
            self.opts.update(text_opts.opts)
        elif type_ == "image" and image_opts:
            self.opts = {"type": type_}
            self.opts.update(image_opts.opts)


class LabelRichStyleOpts(BasicOpts):
    def __init__(
        self,
        width: Optional[Numeric] = None,
        height: Optional[Numeric] = None,
        max_height: Optional[Numeric] = None,
        max_width: Optional[Numeric] = None,
        ellipsis_: Union[bool, str] = False,
        word_break: Optional[str] = "break-word",
        vertical_direction: Optional[str] = None,
        text_align: Optional[str] = None,
        text_baseline: Optional[str] = None,
        layout_direction: Optional[str] = "horizontal",
        is_single_line: Optional[bool] = False,
        text_config_opts: Optional[Sequence[LabelRichTextConfigOpts]] = None,
        font_size: Optional[int] = None,
        font_family: Optional[str] = None,
        font_weight: Union[str, Sequence[str]] = None,
        font_style: Optional[str] = "normal",
        fill: Optional[str] = None,
        stroke: Optional[str] = None,
        line_width: Optional[Numeric] = None,
        fill_opacity: Optional[Numeric] = None,
        stroke_opacity: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "width": width,
            "height": height,
            "maxHeight": max_height,
            "maxWidth": max_width,
            "ellipsis": ellipsis_,
            "wordBreak": word_break,
            "verticalDirection": vertical_direction,
            "textAlign": text_align,
            "textBaseline": text_baseline,
            "layoutDirection": layout_direction,
            "singleLine": is_single_line,
            "textConfig": text_config_opts,
            "fontSize": font_size,
            "fontFamily": font_family,
            "fontWeight": font_weight,
            "fontStyle": font_style,
            "fill": fill,
            "stroke": stroke,
            "lineWidth": line_width,
            "fillOpacity": fill_opacity,
            "strokeOpacity": stroke_opacity,
        }


class LabelStyleOpts(BasicOpts):
    def __init__(
        self,
        type_: Optional[str] = None,
        text_style_opts: BaseStyleOpts = None,
        rich_style_opts: LabelRichStyleOpts = None,
    ):
        self.opts = None
        if type_ == "text" and text_style_opts:
            self.opts = {"type": type_}
            self.opts.update(text_style_opts.opts)
        elif type_ == "rich" and rich_style_opts:
            self.opts = {"type": type_}
            self.opts.update(rich_style_opts.opts)


class LabelSmartInvertOpts(BasicOpts):
    def __init__(
        self,
        mode: Optional[str] = None,
        text_style: Optional[str] = None,
        contrast_ratios_threshold: Optional[Numeric] = None,
        alternative_colors: Union[str, Sequence[str]] = None,
        fill_strategy: Optional[str] = None,
        stroke_strategy: Optional[str] = None,
        bright_color: Optional[str] = None,
        is_outside_enable: Optional[bool] = None,
        interact_invert_type: Optional[str] = None,
    ):
        self.opts: dict = {
            "mode": mode,
            "textStyle": text_style,
            "contrastRatiosThreshold": contrast_ratios_threshold,
            "alternativeColors": alternative_colors,
            "fillStrategy": fill_strategy,
            "strokeStrategy": stroke_strategy,
            "brightColor": bright_color,
            "outsideEnable": is_outside_enable,
            "interactInvertType": interact_invert_type,
        }


class LabelFilterByGroupOpts(BasicOpts):
    def __init__(
        self,
        field: Optional[str] = None,
        type_: Optional[str] = None,
        filter_: Optional[JSFunc] = None,
    ):
        self.opts = {
            "field": field,
            "type": type_,
            "filter": filter_,
        }


class LabelOverlapOpts(BasicOpts):
    def __init__(
        self,
        is_hide_on_hit: Optional[bool] = None,
        is_clamp_force: Optional[bool] = None,
        is_avoid_base_mark: Optional[bool] = None,
        strategy: Optional[Sequence] = None,
    ):
        self.opts = {
            "hideOnHit": is_hide_on_hit,
            "clampForce": is_clamp_force,
            "avoidBaseMark": is_avoid_base_mark,
            "strategy": strategy,
        }


class LabelOpts(BasicOpts):
    def __init__(
        self,
        position: Optional[Union[str, JsCode]] = None,
        filter_by_group_opts: Optional[LabelFilterByGroupOpts] = None,
        is_visible: Optional[bool] = None,
        is_interactive: Optional[bool] = None,
        format_method: Optional[JsCode] = None,
        formatter: Optional[str] = None,
        is_sync_state: Optional[bool] = None,
        offset: Optional[int] = None,
        style_opts: Optional[Union[BaseStyleOpts, LabelStyleOpts]] = None,
        state_opts: Optional[BaseStateOpts] = None,
        overlap_opts: Optional[Union[LabelOverlapOpts, bool]] = None,
        smart_invert: Optional[Union[LabelSmartInvertOpts, bool]] = None,
        data_filter: Optional[JsCode] = None,
        custom_layout_func: Optional[JsCode] = None,
        custom_overlap_func: Optional[JsCode] = None,
        animation: Optional[AnimationOpts] = None,
        stack_data_filter_type: Optional[str] = None,
        value_type: Optional[str] = None,
        is_support3d: Optional[bool] = None,
    ):
        self.opts: dict = {
            "position": position,
            "filterByGroup": filter_by_group_opts,
            "visible": is_visible,
            "interactive": is_interactive,
            "formatMethod": format_method,
            "formatter": formatter,
            "syncState": is_sync_state,
            "offset": offset,
            "style": style_opts,
            "state": state_opts,
            "overlap": overlap_opts,
            "smartInvert": smart_invert,
            "dataFilter": data_filter,
            "customLayoutFunc": custom_layout_func,
            "customOverlapFunc": custom_overlap_func,
            "animation": animation,
            "stackDataFilterType": stack_data_filter_type,
            "valueType": value_type,
            "support3d": is_support3d,
        }


class ColorOpts(BasicOpts):
    def __init__(
        self,
        type_: Union[Sequence, str] = None,
        domain: Optional[Sequence] = None,
        range_: Optional[Sequence] = None,
        specified: Optional[dict] = None,
    ):
        self.opts: dict = {
            "type": type_,
            "domain": domain,
            "range": range_,
            "specified": specified,
        }


class IndicatorTitleOpts(BasicOpts):
    def __init__(
        self,
        is_visible: Optional[bool] = None,
        field: Optional[str] = None,
        space: Optional[int] = None,
        is_auto_limit: Optional[bool] = None,
        is_auto_fit: Optional[bool] = None,
        fit_percent: Optional[None] = None,
        fit_strategy: Optional[str] = None,
        format_method: Optional[JsCode] = None,
        style: Union[BaseStyleOpts, BaseTitleTextStyleOpts] = None,
    ):
        self.opts: dict = {
            "visible": is_visible,
            "field": field,
            "space": space,
            "autoLimit": is_auto_limit,
            "autoFit": is_auto_fit,
            "fitPercent": fit_percent,
            "fitStrategy": fit_strategy,
            "formatMethod": format_method,
            "style": style,
        }


class IndicatorContentOpts(BasicOpts):
    def __init__(
        self,
        is_visible: Optional[bool] = None,
        field: Optional[str] = None,
        space: Optional[int] = None,
        is_auto_limit: Optional[bool] = None,
        is_auto_fit: Optional[bool] = None,
        fit_percent: Optional[Numeric] = None,
        fit_strategy: Optional[str] = None,
        format_method: Optional[JsCode] = None,
        style: Union[BaseStyleOpts, BaseTitleTextStyleOpts] = None,
    ):
        self.opts: dict = {
            "visible": is_visible,
            "field": field,
            "space": space,
            "autoLimit": is_auto_limit,
            "autoFit": is_auto_fit,
            "fitPercent": fit_percent,
            "fitStrategy": fit_strategy,
            "formatMethod": format_method,
            "style": style,
        }


class IndicatorOpts(BasicOpts):
    def __init__(
        self,
        is_visible: Optional[bool] = None,
        is_fixed: Optional[bool] = None,
        trigger: Optional[str] = None,
        offset_x: Optional[Numeric] = None,
        offset_y: Optional[Numeric] = None,
        limit_ratio: Optional[Numeric] = None,
        title_opts: Optional[IndicatorTitleOpts] = None,
        content_opts: Optional[
            Union[IndicatorContentOpts, Sequence[IndicatorContentOpts]]
        ] = None,
    ):
        self.opts: dict = {
            "visible": is_visible,
            "fixed": is_fixed,
            "trigger": trigger,
            "offsetX": offset_x,
            "offsetY": offset_y,
            "limitRatio": limit_ratio,
            "title": title_opts,
            "content": content_opts,
        }


class InitOpts(BasicOpts):
    def __init__(
        self,
        width: str = "900px",
        height: str = "500px",
        is_horizontal_center: bool = False,
        page_title: str = CurrentConfig.PAGE_TITLE,
        bg_color: Union[str, dict] = None,
        is_fill_bg_color: bool = False,
        js_host: str = "",
        is_embed_js: bool = False,
    ):
        self.opts: dict = {
            "width": width,
            "height": height,
            "is_horizontal_center": is_horizontal_center,
            "page_title": page_title,
            "bg_color": bg_color,
            "fill_bg": is_fill_bg_color,
            "js_host": js_host,
            "is_embed_js": is_embed_js,
        }


class PaddingOpts(BasicOpts):
    def __init__(
        self,
        pos_left: Union[str, int, JsCode] = None,
        pos_right: Union[str, int, JsCode] = None,
        pos_top: Union[str, int, JsCode] = None,
        pos_bottom: Union[str, int, JsCode] = None,
    ):
        self.opts: dict = {
            "left": pos_left,
            "right": pos_right,
            "top": pos_top,
            "bottom": pos_bottom,
        }


class RegionOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        coordinate: str = "cartesian",
        width: Union[str, int] = None,
        height: Union[str, int] = None,
        padding_opts: PaddingOpts = None,
        style_opts: BaseStyleOpts = None,
        is_stack_inverse: Optional[bool] = None,
        is_stack_sort: Optional[bool] = None,
        roam: Optional[Union[bool, dict]] = None,
        projection: Optional[dict] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "coordinate": coordinate,
            "width": width,
            "height": height,
            "padding": padding_opts,
            "style": style_opts,
            "stackInverse": is_stack_inverse,
            "stackSort": is_stack_sort,
            "roam": roam,
            "projection": projection,
        }


class Render3DOpts(BasicOpts):
    def __init__(
        self,
        is_enable: Optional[bool] = None,
        is_enable_view_3d_transform: Optional[bool] = None,
        center: Optional[dict] = None,
    ):
        self.opts: dict = {
            "enable": is_enable,
            "enableView3dTransform": is_enable_view_3d_transform,
            "center": center,
        }


class RenderOpts(BasicOpts):
    def __init__(
        self,
        dom: Union[str, JsCode] = None,
        render_canvas: Union[str, JsCode] = None,
        is_auto_fit: Optional[bool] = None,
        is_animation: Optional[bool] = None,
        options3d_opts: Optional[Render3DOpts] = None,
        layout_callback: Optional[JSFunc] = None,
        render_mode: Optional[str] = None,
        render_mode_params: Optional[dict] = None,
        dpr: Optional[Numeric] = None,
        is_interactive: Optional[bool] = None,
        view_box: Optional[dict] = None,
        is_canvas_controled: Optional[bool] = None,
        before_render_func: Optional[JSFunc] = None,
        after_render_func: Optional[JSFunc] = None,
        background: Union[str, JsCode] = None,
        log_level: Optional[int] = None,
        is_disable_dirty_bounds: Optional[bool] = None,
        is_enable_view_3d_transform: Optional[bool] = None,
        is_pop_tip: Optional[bool] = None,
        is_disable_trigger_event: Optional[bool] = None,
        theme: Optional[str] = None,
        is_enable_html_attributes: Optional[bool] = None,
        is_supports_touch_events: Optional[bool] = None,
        is_supports_pointer_events: Optional[bool] = None,
        resize_delay: Optional[int] = None,
        is_auto_refresh_dpr: Optional[bool] = None,
    ):
        self.opts: dict = {
            "dom": dom,
            "renderCanvas": render_canvas,
            "autoFit": is_auto_fit,
            "animation": is_animation,
            "options3d": options3d_opts,
            "layout": layout_callback,
            "mode": render_mode,
            "modeParams": render_mode_params,
            "dpr": dpr,
            "interactive": is_interactive,
            "viewBox": view_box,
            "canvasControled": is_canvas_controled,
            "beforeRender": before_render_func,
            "afterRender": after_render_func,
            "background": background,
            "logLevel": log_level,
            "disableDirtyBounds": is_disable_dirty_bounds,
            "enableView3dTransform": is_enable_view_3d_transform,
            "popTip": is_pop_tip,
            "disableTriggerEvent": is_disable_trigger_event,
            "theme": theme,
            "enableHtmlAttributes": is_enable_html_attributes,
            "supportsTouchEvents": is_supports_touch_events,
            "supportsPointerEvents": is_supports_pointer_events,
            "resizeDelay": resize_delay,
            "autoRefreshDpr": is_auto_refresh_dpr,
        }


class TitleOpts(BasicOpts):
    def __init__(
        self,
        is_visible: bool = True,
        text: Union[str, int, Sequence] = None,
        text_type: Optional[str] = None,
        sub_text: Union[str, int, Sequence] = None,
        sub_text_type: Optional[str] = None,
        orient: str = "top",
        min_width: Union[int, str] = None,
        max_width: Union[int, str] = None,
        min_height: Union[int, str] = None,
        max_height: Union[int, str] = None,
        inner_padding: int = 0,
        align: str = "left",
        vertical_align: str = "top",
        text_style_opts: Optional[BaseTitleTextStyleOpts] = None,
        sub_text_style_opts: Optional[BaseTitleTextStyleOpts] = None,
        layout_type: str = "normal",
        layout_level: int = 50,
        align_self: str = "start",
        padding: Optional[PaddingOpts] = None,
        width: Union[int, str] = None,
        height: Union[int, str] = None,
        offset_x: Union[int, str] = None,
        offset_y: Union[int, str] = None,
        z_index: int = 500,
        is_clip: Optional[bool] = None,
        left: Union[int, str] = None,
        right: Union[int, str] = None,
        top: Union[int, str] = None,
        bottom: Union[int, str] = None,
        is_center: Optional[bool] = None,
    ):
        self.opts: dict = {
            "visible": is_visible,
            "text": text,
            "textType": text_type,
            "subText": sub_text,
            "subTextType": sub_text_type,
            "orient": orient,
            "minWidth": min_width,
            "maxWidth": max_width,
            "minHeight": min_height,
            "maxHeight": max_height,
            "innerPadding": inner_padding,
            "align": align,
            "verticalAlign": vertical_align,
            "textStyle": text_style_opts,
            "subTextStyle": sub_text_style_opts,
            "layoutType": layout_type,
            "layoutLevel": layout_level,
            "alignSelf": align_self,
            "padding": padding,
            "width": width,
            "height": height,
            "offsetX": offset_x,
            "offsetY": offset_y,
            "zIndex": z_index,
            "clip": is_clip,
            "left": left,
            "right": right,
            "top": top,
            "bottom": bottom,
            "center": is_center,
        }


class LegendTitleOpts(BasicOpts):
    def __init__(
        self,
        is_visible: bool = False,
        text: Union[str, Sequence[str], int, Sequence[int]] = None,
        align: str = "start",
        space: Optional[int] = None,
        padding: Union[int, Sequence[int], JSFunc] = None,
        text_style_opts: BaseTitleTextStyleOpts = None,
        is_shape_visible: bool = False,
        shape_space: Optional[int] = None,
        shape_style: BaseStyleOpts = None,
        is_background_visible: bool = False,
        background_style: BaseStyleOpts = None,
        min_width: Optional[int] = None,
        max_width: Optional[int] = None,
    ):
        self.opts: dict = {
            "visible": is_visible,
            "text": text,
            "align": align,
            "space": space,
            "padding": padding,
            "textStyle": text_style_opts,
            "shape": {
                "visible": is_shape_visible,
                "space": shape_space,
                "style": shape_style,
            },
            "background": {
                "visible": is_background_visible,
                "style": background_style,
            },
            "minWidth": min_width,
            "maxWidth": max_width,
        }


class LegendBackgroundOpts(BasicOpts):
    def __init__(
        self,
        is_visible: bool = False,
        padding: Union[int, Sequence[int], JSFunc] = None,
        style_opts: BaseStyleOpts = None,
    ):
        self.opts: dict = {
            "visible": is_visible,
            "padding": padding,
            "style": style_opts,
        }


class BaseLegendOpts(BasicOpts):
    def __init__(
        self,
        is_visible: bool = True,
        orient: Optional[str] = None,
        position: str = "middle",
        layout: Optional[str] = None,
        is_interactive: bool = True,
        is_filter: bool = True,
        custom_filter: Optional[JsCode] = None,
        title_opts: LegendTitleOpts = None,
        background_opts: LegendBackgroundOpts = None,
        default_selected: Optional[Sequence] = None,
        scale: Optional[str] = None,
        field: Optional[str] = None,
        is_reversed: Optional[bool] = None,
        max_width: Union[int, str] = None,
        max_col: Optional[int] = None,
        max_height: Union[int, str] = None,
        max_row: Optional[int] = None,
        region_index: Union[int, Sequence[int]] = None,
        region_id: Union[int, str, Sequence[int], Sequence[str]] = None,
        series_index: Union[int, Sequence[int]] = None,
        series_id: Union[int, str, Sequence[int], Sequence[str]] = None,
        layout_type: str = "normal",
        layout_level: int = 50,
        align_self: str = "start",
        padding: PaddingOpts = None,
        width: Union[int, str] = None,
        min_width: Union[int, str] = None,
        height: Union[int, str] = None,
        min_height: Union[int, str] = None,
        offset_x: Union[int, str] = None,
        offset_y: Union[int, str] = None,
        z_index: Optional[Numeric] = 500,
        is_clip: Optional[bool] = None,
        left: Union[int, str] = None,
        right: Union[int, str] = None,
        top: Union[int, str] = None,
        bottom: Union[int, str] = None,
        is_center: Optional[bool] = None,
    ):
        self.opts: dict = {
            "visible": is_visible,
            "orient": orient,
            "position": position,
            "layout": layout,
            "interactive": is_interactive,
            "filter": is_filter,
            "customFilter": custom_filter,
            "title": title_opts,
            "background": background_opts,
            "defaultSelected": default_selected,
            "scale": scale,
            "field": field,
            "reversed": is_reversed,
            "maxWidth": max_width,
            "maxCol": max_col,
            "maxHeight": max_height,
            "maxRow": max_row,
            "regionIndex": region_index,
            "regionId": region_id,
            "seriesIndex": series_index,
            "seriesId": series_id,
            "layoutType": layout_type,
            "layoutLevel": layout_level,
            "alignSelf": align_self,
            "padding": padding,
            "width": width,
            "minWidth": min_width,
            "height": height,
            "minHeight": min_height,
            "offsetX": offset_x,
            "offsetY": offset_y,
            "zIndex": z_index,
            "clip": is_clip,
            "left": left,
            "right": right,
            "top": top,
            "bottom": bottom,
            "center": is_center,
        }


class DiscreteLegendItemOpts(BasicOpts):
    def __init__(
        self,
        is_visible: bool = True,
        space_col: Optional[int] = None,
        space_row: Optional[int] = None,
        max_width: Union[int, str] = None,
        width: Union[int, str] = None,
        height: Union[int, str] = None,
        padding: Union[int, Sequence[int], JSFunc] = None,
        align: str = "left",
        auto_ellipsis_strategy: str = "none",
        is_background_visible: bool = False,
        background_style_opts: BaseStyleOpts = None,
        background_state_opts: BaseStateOpts = None,
        is_shape_visible: bool = False,
        shape_space: Optional[Numeric] = None,
        shape_style_opts: BaseStyleOpts = None,
        shape_state_opts: BaseStateOpts = None,
        label_space: Optional[Numeric] = None,
        label_width_ratio: Optional[Numeric] = None,
        label_format_method: Optional[JSFunc] = None,
        label_style_opts: BaseStyleOpts = None,
        label_state_opts: BaseStateOpts = None,
        value_space: Optional[Numeric] = None,
        is_value_align_right: bool = False,
        value_width_ratio: Optional[Numeric] = None,
        value_format_method: Optional[JSFunc] = None,
        value_formatter: Optional[Union[str, Sequence[str]]] = None,
        value_style_opts: BaseStyleOpts = None,
        value_state_opts: BaseStateOpts = None,
        is_focus: bool = False,
        focus_icon_style_opts: BaseStyleOpts = None,
    ):
        self.opts: dict = {
            "visible": is_visible,
            "spaceCol": space_col,
            "spaceRow": space_row,
            "maxWidth": max_width,
            "width": width,
            "height": height,
            "padding": padding,
            "align": align,
            "autoEllipsisStrategy": auto_ellipsis_strategy,
            "background": {
                "visible": is_background_visible,
                "style": background_style_opts,
                "state": background_state_opts,
            },
            "shape": {
                "visible": is_shape_visible,
                "space": shape_space,
                "style": shape_style_opts,
                "state": shape_state_opts,
            },
            "label": {
                "space": label_space,
                "widthRatio": label_width_ratio,
                "formatMethod": label_format_method,
                "style": label_style_opts,
                "state": label_state_opts,
            },
            "value": {
                "space": value_space,
                "alignRight": is_value_align_right,
                "widthRatio": value_width_ratio,
                "formatMethod": value_format_method,
                "formatter": value_formatter,
                "style": value_style_opts,
                "state": value_state_opts,
            },
            "focus": is_focus,
            "focusIconStyle": focus_icon_style_opts,
        }


class DiscreteLegendPagerOpts(BasicOpts):
    def __init__(
        self,
        type_: Optional[str] = None,
        layout: Optional[str] = None,
        default_current: Optional[int] = None,
        padding: Union[int, Sequence[int], JSFunc] = None,
        space: Optional[int] = None,
        is_animation: bool = True,
        animation_duration: int = 450,
        animation_easing: str = "quadIn",
        text_style_opts: BaseTitleTextStyleOpts = None,
        handle_space: int = 8,
        handle_pre_shape: Optional[str] = None,
        handle_next_shape: Optional[str] = None,
        handle_style_opts: BaseStyleOpts = None,
        handle_state_hover_opts: BaseStyleOpts = None,
        handle_state_disabled_opts: BaseStyleOpts = None,
        rail_style_opts: BaseStyleOpts = None,
        slider_style_opts: BaseStyleOpts = None,
        is_scroll_by_position: Optional[bool] = None,
        is_scroll_mask_visible: bool = False,
        scroll_mask_gradient_len: int = 16,
        scroll_mask_gradient_stops: Optional[dict] = None,
    ):
        self.opts: dict = {
            "type": type_,
            "layout": layout,
            "defaultCurrent": default_current,
            "padding": padding,
            "space": space,
            "animation": is_animation,
            "animationDuration": animation_duration,
            "animationEasing": animation_easing,
            "textStyle": text_style_opts,
            "handle": {
                "space": handle_space,
                "preShape": handle_pre_shape,
                "nextShape": handle_next_shape,
                "style": handle_style_opts,
                "state": {
                    "hover": handle_state_hover_opts,
                    "disabled": handle_state_disabled_opts,
                },
            },
            "railStyle": rail_style_opts,
            "sliderStyle": slider_style_opts,
            "scrollByPosition": is_scroll_by_position,
            "scrollMask": {
                "visible": is_scroll_mask_visible,
                "gradientLength": scroll_mask_gradient_len,
                "gradientStops": scroll_mask_gradient_stops,
            },
        }


class DiscreteLegendOpts(BasicOpts):
    def __init__(
        self,
        is_select: bool = True,
        select_mode: str = "multiple",
        scale_name: Optional[str] = None,
        is_hover: bool = True,
        is_allow_all_canceled: Optional[bool] = None,
        item: DiscreteLegendItemOpts = None,
        is_auto_page: bool = True,
        pager: DiscreteLegendPagerOpts = None,
        data: Optional[JSFunc] = None,
        base_legend_opts: BaseLegendOpts = None,
    ):
        self.opts: dict = {}

        if base_legend_opts:
            self.opts.update(base_legend_opts.opts)

        self.opts.update(
            {
                "type": "discrete",
                "select": is_select,
                "selectMode": select_mode,
                "scaleName": scale_name,
                "hover": is_hover,
                "allowAllCanceled": is_allow_all_canceled,
                "item": item,
                "autoPage": is_auto_page,
                "pager": pager,
                "data": data,
            }
        )


class ColorLegendOpts(BasicOpts):
    def __init__(
        self,
        is_slidable: bool = True,
        is_inverse: bool = True,
        rail_width: Optional[int] = None,
        rail_height: Optional[int] = None,
        rail_style_opts: BaseStyleOpts = None,
        is_handle_visible: bool = True,
        handle_style_opts: BaseStyleOpts = None,
        track_style_opts: BaseStyleOpts = None,
        is_start_text_visible: bool = False,
        start_text: str = None,
        start_text_space: int = 6,
        start_text_style_opts: BaseStyleOpts = None,
        is_end_text_visible: bool = False,
        end_text: str = None,
        end_text_space: int = 6,
        end_text_style_opts: BaseStyleOpts = None,
        is_handle_text_visible: bool = False,
        handle_text_precision: Optional[int] = None,
        handle_text_formatter: Optional[JSFunc] = None,
        handle_text_space: int = 6,
        handle_text_style_opts: BaseStyleOpts = None,
        base_legend_opts: BaseLegendOpts = None,
    ):
        self.opts: dict = {}

        if base_legend_opts is not None:
            self.opts.update(base_legend_opts.opts)

        self.opts.update(
            {
                "type": "color",
                "slidable": is_slidable,
                "inverse": is_inverse,
                "rail": {
                    "width": rail_width,
                    "height": rail_height,
                    "style": rail_style_opts,
                },
                "handle": {
                    "visible": is_handle_visible,
                    "style": handle_style_opts,
                },
                "track": {
                    "style": track_style_opts,
                },
                "startText": {
                    "visible": is_start_text_visible,
                    "text": start_text,
                    "space": start_text_space,
                    "style": start_text_style_opts,
                },
                "endText": {
                    "visible": is_end_text_visible,
                    "text": end_text,
                    "space": end_text_space,
                    "style": end_text_style_opts,
                },
                "handleText": {
                    "visible": is_handle_text_visible,
                    "precision": handle_text_precision,
                    "formatter": handle_text_formatter,
                    "space": handle_text_space,
                    "style": handle_text_style_opts,
                },
            }
        )


class SizeLegendOpts(BasicOpts):
    def __init__(
        self,
        is_slidable: bool = True,
        is_inverse: bool = True,
        rail_width: Optional[int] = None,
        rail_height: Optional[int] = None,
        rail_style_opts: BaseStyleOpts = None,
        is_handle_visible: bool = True,
        handle_style_opts: BaseStyleOpts = None,
        track_style_opts: BaseStyleOpts = None,
        is_start_text_visible: bool = False,
        start_text: str = None,
        start_text_space: int = 6,
        start_text_style_opts: BaseStyleOpts = None,
        is_end_text_visible: bool = False,
        end_text: str = None,
        end_text_space: int = 6,
        end_text_style_opts: BaseStyleOpts = None,
        is_handle_text_visible: bool = False,
        handle_text_precision: Optional[int] = None,
        handle_text_formatter: Optional[JSFunc] = None,
        handle_text_space: int = 6,
        handle_text_style_opts: BaseStyleOpts = None,
        size_background: BaseStyleOpts = None,
        base_legend_opts: BaseLegendOpts = None,
    ):
        self.opts: dict = {}

        if base_legend_opts is not None:
            self.opts.update(base_legend_opts.opts)

        self.opts.update(
            {
                "type": "size",
                "slidable": is_slidable,
                "inverse": is_inverse,
                "rail": {
                    "width": rail_width,
                    "height": rail_height,
                    "style": rail_style_opts,
                },
                "handle": {
                    "visible": is_handle_visible,
                    "style": handle_style_opts,
                },
                "track": {
                    "style": track_style_opts,
                },
                "startText": {
                    "visible": is_start_text_visible,
                    "text": start_text,
                    "space": start_text_space,
                    "style": start_text_style_opts,
                },
                "endText": {
                    "visible": is_end_text_visible,
                    "text": end_text,
                    "space": end_text_space,
                    "style": end_text_style_opts,
                },
                "handleText": {
                    "visible": is_handle_text_visible,
                    "precision": handle_text_precision,
                    "formatter": handle_text_formatter,
                    "space": handle_text_space,
                    "style": handle_text_style_opts,
                },
                "sizeBackground": size_background,
            }
        )


class BaseMarkOpts(BasicOpts):
    def __init__(
        self,
        relative_series_index: Optional[int] = None,
        relative_series_id: Optional[str] = None,
        is_visible: bool = True,
        is_clip: Optional[bool] = None,
        is_interactive: bool = True,
        is_auto_range: Optional[bool] = None,
        id_: Union[int, str] = None,
        name: Optional[str] = None,
        coordinate_type: Optional[str] = None,
        layout_type: Optional[str] = None,
        layout_level: Optional[int] = None,
        align_self: str = "start",
        padding: Optional[PaddingOpts] = None,
        width: Union[int, str] = None,
        min_width: Union[int, str] = None,
        max_width: Union[int, str] = None,
        height: Union[int, str] = None,
        min_height: Union[int, str] = None,
        max_height: Union[int, str] = None,
        offset_x: Union[int, str] = None,
        offset_y: Union[int, str] = None,
        z_index: Optional[int] = None,
        left: Union[int, str] = None,
        right: Union[int, str] = None,
        top: Union[int, str] = None,
        bottom: Union[int, str] = None,
        is_center: Optional[bool] = None,
        animation: Optional[AnimationOpts] = None,
        animation_enter: Optional[AnimationOpts] = None,
        animation_update: Optional[AnimationOpts] = None,
        animation_exit: Optional[AnimationOpts] = None,
    ):
        self.opts: dict = {
            "relativeSeriesIndex": relative_series_index,
            "relativeSeriesId": relative_series_id,
            "visible": is_visible,
            "clip": is_clip,
            "interactive": is_interactive,
            "autoRange": is_auto_range,
            "id": id_,
            "name": name,
            "coordinationType": coordinate_type,
            "layoutType": layout_type,
            "layoutLevel": layout_level,
            "alignSelf": align_self,
            "padding": padding,
            "width": width,
            "minWidth": min_width,
            "maxWidth": max_width,
            "height": height,
            "minHeight": min_height,
            "maxHeight": max_height,
            "offsetX": offset_x,
            "offsetY": offset_y,
            "zIndex": z_index,
            "left": left,
            "right": right,
            "top": top,
            "bottom": bottom,
            "center": is_center,
            "animation": animation,
            "animationEnter": animation_enter,
            "animationUpdate": animation_update,
            "animationExit": animation_exit,
        }


class MarkCoordinatesOpts(BasicOpts):
    def __init__(
        self,
        key_field: Optional[str] = None,
        value_field: Optional[Union[str, Numeric, JSFunc]] = None,
        ref_relative_series_index: Optional[int] = None,
        ref_relative_series_id: Optional[str] = None,
        x_field_index: Optional[int] = None,
        x_field_dim: Optional[int] = None,
        y_field_index: Optional[int] = None,
        y_field_dim: Optional[int] = None,
        angle_field_index: Optional[int] = None,
        angle_field_dim: Optional[int] = None,
        radius_field_index: Optional[int] = None,
        radius_field_dim: Optional[int] = None,
    ):
        self.opts: dict = {
            "refRelativeSeriesIndex": ref_relative_series_index,
            "refRelativeSeriesId": ref_relative_series_id,
            "xFieldIndex": x_field_index,
            "xFieldDim": x_field_dim,
            "yFieldIndex": y_field_index,
            "yFieldDim": y_field_dim,
            "angleFieldIndex": angle_field_index,
            "angleFieldDim": angle_field_dim,
            "radiusFieldIndex": radius_field_index,
            "radiusFieldDim": radius_field_dim,
        }
        if key_field and value_field:
            self.opts.update({key_field: value_field})


class MarkLineOpts(BasicOpts):
    def __init__(
        self,
        type_: str = "type-step",
        connect_direction: Optional[str] = None,
        expand_distance: Union[int, str] = None,
        x: Union[int, JSFunc] = None,
        y: Union[int, JSFunc] = None,
        x1: Union[int, JSFunc] = None,
        y1: Union[int, JSFunc] = None,
        angle: Union[int, JSFunc] = None,
        radius: Union[int, JSFunc] = None,
        angle1: Union[int, JSFunc] = None,
        radius1: Union[int, JSFunc] = None,
        coordinates: Optional[Sequence[MarkCoordinatesOpts]] = None,
        coordinates_offset: Optional[Sequence[dict]] = None,
        positions: Optional[Sequence[dict]] = None,
        is_region_relative: bool = False,
        start_relative_series_index: Optional[int] = None,
        start_relative_series_id: Optional[str] = None,
        end_relative_series_index: Optional[int] = None,
        end_relative_series_id: Optional[str] = None,
        relative_relative_series_index: Optional[int] = None,
        relative_relative_series_id: Optional[str] = None,
        specified_data_series_index: Union[str, int, Sequence] = None,
        specified_data_series_id: Union[str, int, Sequence] = None,
        is_line_multi_segment: bool = False,
        line_main_segment_index: Optional[int] = None,
        line_state_opts: BaseStateOpts = None,
        line_style_opts: BaseStyleOpts = None,
        label_opts: LabelOpts = None,
        start_symbol_opts: BaseSymbolOpts = None,
        end_symbol_opts: BaseSymbolOpts = None,
        animation: Optional[AnimationOpts] = None,
        animation_enter: Optional[AnimationOpts] = None,
        animation_update: Optional[AnimationOpts] = None,
        animation_exit: Optional[AnimationOpts] = None,
        base_mark_opts: BaseMarkOpts = None,
    ):
        self.opts: dict = {}

        if base_mark_opts:
            self.opts.update(base_mark_opts.opts)

        self.opts.update(
            {
                "type": type_,
                "connectDirection": connect_direction,
                "expandDistance": expand_distance,
                "x": x,
                "y": y,
                "x1": x1,
                "y1": y1,
                "angle": angle,
                "radius": radius,
                "angle1": angle1,
                "radius1": radius1,
                "coordinates": coordinates,
                "coordinatesOffset": coordinates_offset,
                "positions": positions,
                "regionRelative": is_region_relative,
                "startRelativeSeriesIndex": start_relative_series_index,
                "startRelativeSeriesId": start_relative_series_id,
                "endRelativeSeriesIndex": end_relative_series_index,
                "endRelativeSeriesId": end_relative_series_id,
                "relativeRelativeSeriesIndex": relative_relative_series_index,
                "relativeRelativeSeriesId": relative_relative_series_id,
                "specifiedDataSeriesIndex": specified_data_series_index,
                "specifiedDataSeriesId": specified_data_series_id,
                "line": {
                    "multiSegment": is_line_multi_segment,
                    "mainSegmentIndex": line_main_segment_index,
                    "state": line_state_opts,
                    "style": line_style_opts,
                },
                "label": label_opts,
                "startSymbol": start_symbol_opts,
                "endSymbol": end_symbol_opts,
                "animation": animation,
                "animationEnter": animation_enter,
                "animationUpdate": animation_update,
                "animationExit": animation_exit,
            }
        )


class MarkAreaOpts(BasicOpts):
    def __init__(
        self,
        x: Union[int, JSFunc] = None,
        y: Union[int, JSFunc] = None,
        x1: Union[int, JSFunc] = None,
        y1: Union[int, JSFunc] = None,
        angle: Union[int, JSFunc] = None,
        radius: Union[int, JSFunc] = None,
        angle1: Union[int, JSFunc] = None,
        radius1: Union[int, JSFunc] = None,
        coordinates: Optional[Sequence[MarkCoordinatesOpts]] = None,
        coordinates_offset: Optional[Sequence[dict]] = None,
        positions: Optional[Sequence[dict]] = None,
        is_region_relative: bool = False,
        start_relative_series_index: Optional[int] = None,
        start_relative_series_id: Optional[str] = None,
        end_relative_series_index: Optional[int] = None,
        end_relative_series_id: Optional[str] = None,
        relative_relative_series_index: Optional[int] = None,
        relative_relative_series_id: Optional[str] = None,
        specified_data_series_index: Union[str, int, Sequence] = None,
        specified_data_series_id: Union[str, int, Sequence] = None,
        area_state_opts: BaseStateOpts = None,
        area_style_opts: BaseStyleOpts = None,
        label_opts: LabelOpts = None,
        animation: Optional[AnimationOpts] = None,
        animation_enter: Optional[AnimationOpts] = None,
        animation_update: Optional[AnimationOpts] = None,
        animation_exit: Optional[AnimationOpts] = None,
        base_mark_opts: BaseMarkOpts = None,
    ):
        self.opts: dict = {}

        if base_mark_opts:
            self.opts.update(base_mark_opts.opts)

        self.opts.update(
            {
                "x": x,
                "y": y,
                "x1": x1,
                "y1": y1,
                "angle": angle,
                "radius": radius,
                "angle1": angle1,
                "radius1": radius1,
                "coordinates": coordinates,
                "coordinatesOffset": coordinates_offset,
                "positions": positions,
                "regionRelative": is_region_relative,
                "startRelativeSeriesIndex": start_relative_series_index,
                "startRelativeSeriesId": start_relative_series_id,
                "endRelativeSeriesIndex": end_relative_series_index,
                "endRelativeSeriesId": end_relative_series_id,
                "relativeRelativeSeriesIndex": relative_relative_series_index,
                "relativeRelativeSeriesId": relative_relative_series_id,
                "specifiedDataSeriesIndex": specified_data_series_index,
                "specifiedDataSeriesId": specified_data_series_id,
                "area": {
                    "state": area_state_opts,
                    "style": area_style_opts,
                },
                "label": label_opts,
                "animation": animation,
                "animationEnter": animation_enter,
                "animationUpdate": animation_update,
                "animationExit": animation_exit,
            }
        )


class MarkPointItemLineOpts(BasicOpts):
    def __init__(
        self,
        type_: Optional[str] = None,
        is_visible: Optional[bool] = None,
        arc_ratio: Optional[int] = None,
        is_decorative_line_visible: Optional[bool] = None,
        decorative_line_length: Optional[Numeric] = None,
        start_symbol_opts: Optional[BaseSymbolOpts] = None,
        end_symbol_opts: Optional[BaseSymbolOpts] = None,
        line_state_opts: Optional[BaseStateOpts] = None,
        line_style_opts: Optional[BaseStyleOpts] = None,
    ):
        self.opts: dict = {
            "type": type_,
            "visible": is_visible,
            "arcRatio": arc_ratio,
            "decorativeLine": {
                "visible": is_decorative_line_visible,
                "length": decorative_line_length,
            },
            "startSymbol": start_symbol_opts,
            "endSymbol": end_symbol_opts,
            "line": {
                "state": line_state_opts,
                "style": line_style_opts,
            },
        }


class MarkPointItemContentOpts(BasicOpts):
    def __init__(
        self,
        type_: Optional[str] = None,
        position: Optional[str] = None,
        offset_x: Optional[Numeric] = None,
        offset_y: Optional[Numeric] = None,
        ref_x: Optional[Numeric] = None,
        ref_y: Optional[Numeric] = None,
        ref_angle: Optional[Numeric] = None,
        is_confine: Optional[bool] = None,
        symbol_state_opts: Optional[BaseStateOpts] = None,
        symbol_style_opts: Optional[BaseStyleOpts] = None,
        image_state_opts: Optional[BaseStateOpts] = None,
        image_style_opts: Optional[BaseStyleOpts] = None,
        text_state_opts: Optional[BaseStateOpts] = None,
        text_style_opts: Optional[BaseStyleOpts] = None,
        rich_text_state_opts: Optional[BaseStateOpts] = None,
        rich_text_style_opts: Optional[BaseStyleOpts] = None,
    ):
        self.opts: dict = {
            "type": type_,
            "position": position,
            "offsetX": offset_x,
            "offsetY": offset_y,
            "refX": ref_x,
            "refY": ref_y,
            "refAngle": ref_angle,
            "confine": is_confine,
            "symbol": {
                "state": symbol_state_opts,
                "style": symbol_style_opts,
            },
            "image": {
                "state": image_state_opts,
                "style": image_style_opts,
            },
            "text": {
                "state": text_state_opts,
                "style": text_style_opts,
            },
            "richText": {
                "state": rich_text_state_opts,
                "style": rich_text_style_opts,
            },
        }


class MarkPointOpts(BasicOpts):
    def __init__(
        self,
        x: Union[int, JSFunc] = None,
        y: Union[int, JSFunc] = None,
        angle: Union[int, JSFunc] = None,
        radius: Union[int, JSFunc] = None,
        area_name: Union[int, JSFunc] = None,
        coordinate: Optional[MarkCoordinatesOpts] = None,
        coordinates_offset: Optional[dict] = None,
        position: Optional[dict] = None,
        is_region_relative: bool = False,
        relative_relative_series_index: Optional[int] = None,
        relative_relative_series_id: Optional[str] = None,
        item_line_opts: Optional[MarkPointItemLineOpts] = None,
        item_content_opts: Optional[MarkPointItemContentOpts] = None,
        animation: Optional[AnimationOpts] = None,
        animation_enter: Optional[AnimationOpts] = None,
        animation_update: Optional[AnimationOpts] = None,
        animation_exit: Optional[AnimationOpts] = None,
        target_symbol_offset: Optional[Numeric] = None,
        is_target_symbol_visible: bool = False,
        target_symbol_size: Optional[Numeric] = None,
        target_symbol_style_opts: Optional[Numeric] = None,
        base_mark_opts: BaseMarkOpts = None,
    ):
        self.opts: dict = {}

        if base_mark_opts:
            self.opts.update(base_mark_opts.opts)

        self.opts.update(
            {
                "x": x,
                "y": y,
                "angle": angle,
                "radius": radius,
                "areaName": area_name,
                "coordinate": coordinate,
                "coordinatesOffset": coordinates_offset,
                "position": position,
                "regionRelative": is_region_relative,
                "relativeRelativeSeriesIndex": relative_relative_series_index,
                "relativeRelativeSeriesId": relative_relative_series_id,
                "itemLine": item_line_opts,
                "itemContent": item_content_opts,
                "animation": animation,
                "animationEnter": animation_enter,
                "animationUpdate": animation_update,
                "animationExit": animation_exit,
                "targetSymbol": {
                    "offset": target_symbol_offset,
                    "visible": is_target_symbol_visible,
                    "size": target_symbol_size,
                    "style": target_symbol_style_opts,
                },
            }
        )


class CrossHairFieldOpts(BasicOpts):
    def __init__(
        self,
        is_visible: bool = False,
        is_line_visible: Optional[bool] = None,
        line_type: Optional[str] = None,
        line_width: Union[int, str] = None,
        line_style_opts: BaseStyleOpts = None,
        is_label_visible: Optional[bool] = None,
        label_format_method: Optional[JSFunc] = None,
        label_formatter: Union[str, Sequence[str]] = None,
        label_style_opts: BaseStyleOpts = None,
        is_label_background_visible: Optional[bool] = None,
        label_background_padding: Union[int, Sequence[int], JSFunc] = None,
        label_background_min_width: Optional[int] = 30,
        label_background_max_width: Optional[int] = None,
        label_background_style_opts: BaseStyleOpts = None,
        binding_axes_index: Optional[Sequence[Numeric]] = None,
        default_select_axis_index: Optional[int] = None,
        default_select_datum: Union[str, int] = None,
    ):
        self.opts: dict = {
            "visible": is_visible,
            "line": {
                "visible": is_line_visible,
                "type": line_type,
                "width": line_width,
                "style": line_style_opts,
            },
            "label": {
                "visible": is_label_visible,
                "formatMethod": label_format_method,
                "formatter": label_formatter,
                "style": label_style_opts,
                "labelBackground": {
                    "visible": is_label_background_visible,
                    "padding": label_background_padding,
                    "minWidth": label_background_min_width,
                    "maxWidth": label_background_max_width,
                    "style": label_background_style_opts,
                },
            },
            "bindingAxesIndex": binding_axes_index,
            "defaultSelect": {
                "axisIndex": default_select_axis_index,
                "datum": default_select_datum,
            },
        }


class CrossHairOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[int, str] = None,
        trigger: Optional[str] = "hover",
        trigger_off: Optional[str] = None,
        is_lock_after_click: Optional[bool] = None,
        is_follow_tooltip: Optional[bool] = None,
        label_zindex: Optional[Numeric] = 500,
        grid_zindex: Optional[Numeric] = 100,
        x_field: Optional[CrossHairFieldOpts] = None,
        y_field: Optional[CrossHairFieldOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "trigger": trigger,
            "triggerOff": trigger_off,
            "lockAfterClick": is_lock_after_click,
            "followTooltip": is_follow_tooltip,
            "labelZIndex": label_zindex,
            "gridZIndex": grid_zindex,
            "xField": x_field,
            "yField": y_field,
        }


class AxesTickOpts(BasicOpts):
    def __init__(
        self,
        is_visible: bool = False,
        tick_size: Optional[int] = 4,
        is_inside: bool = False,
        is_align_with_label: bool = True,
        tick_step: Optional[int] = None,
        tick_count: Optional[int] = 5,
        force_tick_count: Optional[int] = None,
        tick_mode: Optional[str] = "average",
        is_no_decimals: bool = False,
        data_filter: Optional[JSFunc] = None,
        style_opts: BaseStyleOpts = None,
        state_opts: BaseStateOpts = None,
    ):
        self.opts: dict = {
            "visible": is_visible,
            "tickSize": tick_size,
            "inside": is_inside,
            "alignWithLabel": is_align_with_label,
            "tickStep": tick_step,
            "tickCount": tick_count,
            "forceTickCount": force_tick_count,
            "tickMode": tick_mode,
            "noDecimals": is_no_decimals,
            "dataFilter": data_filter,
            "style": style_opts,
            "state": state_opts,
        }


class AxesSubTickOpts(BasicOpts):
    def __init__(
        self,
        is_visible: bool = False,
        tick_count: Optional[int] = 4,
        is_inside: bool = False,
        tick_size: Optional[int] = 2,
        style_opts: BaseStyleOpts = None,
        state_opts: BaseStateOpts = None,
    ):
        self.opts: dict = {
            "visible": is_visible,
            "tickCount": tick_count,
            "inside": is_inside,
            "tickSize": tick_size,
            "style": style_opts,
            "state": state_opts,
        }


class AxesGridOpts(BasicOpts):
    def __init__(
        self,
        is_smooth: Optional[bool] = None,
        is_visible: Optional[bool] = None,
        alternate_color: Union[str, Sequence[str]] = None,
        is_align_with_label: Optional[bool] = None,
        style_opts: BaseStyleOpts = None,
    ):
        self.opts: dict = {
            "smooth": is_smooth,
            "visible": is_visible,
            "alternateColor": alternate_color,
            "alignWithLabel": is_align_with_label,
            "style": style_opts,
        }


class AxesBackgroundOpts(BasicOpts):
    def __init__(
        self,
        is_visible: Optional[bool] = None,
        style_opts: BaseStyleOpts = None,
        state_opts: BaseStateOpts = None,
    ):
        self.opts: dict = {
            "visible": is_visible,
            "style": style_opts,
            "state": state_opts,
        }


class AxesLabelOpts(BasicOpts):
    def __init__(
        self,
        is_visible: Optional[bool] = None,
        type_: Optional[str] = None,
        format_method: Optional[JsCode] = None,
        formatter: Union[str, Sequence[str]] = None,
        space: Optional[int] = None,
        is_inside: Optional[bool] = False,
        min_gap: Optional[int] = 4,
        data_filter: Optional[JSFunc] = None,
        style_opts: BaseStyleOpts = None,
        state_opts: BaseStateOpts = None,
        is_flush: Optional[bool] = False,
        is_last_visible: Optional[bool] = None,
        is_auto_rotate: Optional[bool] = None,
        auto_rotate_angle: Optional[Sequence[int]] = None,
        is_auto_hide: Optional[bool] = None,
        auto_hide_method: Optional[str] = None,
        auto_hide_separation: Optional[Numeric] = None,
        is_auto_limit: Optional[bool] = None,
        limit_ellipsis: Optional[str] = "...",
        is_auto_wrap: Optional[bool] = None,
        layout_func: Optional[JSFunc] = None,
        container_align: Optional[str] = None,
    ):
        self.opts: dict = {
            "visible": is_visible,
            "type": type_,
            "formatMethod": format_method,
            "formatter": formatter,
            "space": space,
            "inside": is_inside,
            "minGap": min_gap,
            "dataFilter": data_filter,
            "style": style_opts,
            "state": state_opts,
            "flush": is_flush,
            "lastVisible": is_last_visible,
            "autoRotate": is_auto_rotate,
            "autoRotateAngle": auto_rotate_angle,
            "autoHide": is_auto_hide,
            "autoHideMethod": auto_hide_method,
            "autoHideSeparation": auto_hide_separation,
            "autoLimit": is_auto_limit,
            "limitEllipsis": limit_ellipsis,
            "autoWrap": is_auto_wrap,
            "layoutFunc": layout_func,
            "containerAlign": container_align,
        }


class AxesDomainLineOpts(BasicOpts):
    def __init__(
        self,
        is_visible: Optional[bool] = None,
        style_opts: BaseStyleOpts = None,
        state_opts: BaseStateOpts = None,
        start_symbol_opts: BaseSymbolOpts = None,
        end_symbol_opts: BaseSymbolOpts = None,
        is_on_zero: Optional[bool] = None,
        on_zero_axis_index: Optional[int] = None,
        on_zero_axis_id: Union[int, str] = None,
    ):
        self.opts: dict = {
            "visible": is_visible,
            "style": style_opts,
            "state": state_opts,
            "startSymbol": start_symbol_opts,
            "endSymbol": end_symbol_opts,
            "onZero": is_on_zero,
            "onZeroAxisIndex": on_zero_axis_index,
            "onZeroAxisId": on_zero_axis_id,
        }


class BaseAxesOpts(BasicOpts):
    def __init__(
        self,
        id_: Optional[Union[int, str]] = None,
        is_visible: Optional[bool] = None,
        mode: Optional[str] = None,
        depth: Optional[int] = None,
        is_sampling: Optional[bool] = None,
        orient: Optional[str] = None,
        is_inverse: Optional[bool] = None,
        is_hover: Optional[bool] = None,
        is_select: Optional[bool] = None,
        is_auto_indent: Optional[bool] = None,
        domain_line: Optional[AxesDomainLineOpts] = None,
        label: Optional[AxesLabelOpts] = None,
        title: Optional[TitleOpts] = None,
        background: Optional[AxesBackgroundOpts] = None,
        grid: Optional[AxesGridOpts] = None,
        sub_grid: Optional[AxesGridOpts] = None,
        is_unit_visible: Optional[bool] = None,
        unit_text: Optional[str] = None,
        unit_style_opts: Optional[BaseStyleOpts] = None,
        inner_offset: Optional[PaddingOpts] = None,
        tick: AxesTickOpts = None,
        sub_tick: AxesSubTickOpts = None,
        animation: Optional[AnimationOpts] = None,
        animation_appear: Optional[AnimationOpts] = None,
        animation_enter: Optional[AnimationOpts] = None,
        animation_update: Optional[AnimationOpts] = None,
        animation_exit: Optional[AnimationOpts] = None,
        region_index: Union[int, Sequence[int]] = None,
        region_id: Union[int, str, Sequence[int], Sequence[str]] = None,
        series_index: Union[int, Sequence[int]] = None,
        series_id: Union[int, str, Sequence[int], Sequence[str]] = None,
        layout_type: Optional[str] = None,
        layout_level: Optional[int] = None,
        align_self: Optional[str] = None,
        padding: Optional[PaddingOpts] = None,
        width: Union[int, str, JsCode] = None,
        min_width: Union[int, str] = None,
        max_width: Union[int, str] = None,
        height: Union[int, str, JsCode] = None,
        min_height: Union[int, str] = None,
        max_height: Union[int, str] = None,
        offset_x: Union[int, str] = None,
        offset_y: Union[int, str] = None,
        z_index: Optional[int] = None,
        is_clip: Optional[bool] = None,
        left: Union[int, str] = None,
        right: Union[int, str] = None,
        top: Union[int, str] = None,
        bottom: Union[int, str] = None,
        is_center: Optional[bool] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "visible": is_visible,
            "mode": mode,
            "depth": depth,
            "sampling": is_sampling,
            "orient": orient,
            "inverse": is_inverse,
            "hover": is_hover,
            "select": is_select,
            "autoIndent": is_auto_indent,
            "domainLine": domain_line,
            "label": label,
            "title": title,
            "background": background,
            "grid": grid,
            "subGrid": sub_grid,
            "unit": {
                "visible": is_unit_visible,
                "text": unit_text,
                "style": unit_style_opts,
            },
            "innerOffset": inner_offset,
            "tick": tick,
            "subTick": sub_tick,
            "animation": animation,
            "animationAppear": animation_appear,
            "animationEnter": animation_enter,
            "animationUpdate": animation_update,
            "animationExit": animation_exit,
            "regionIndex": region_index,
            "regionId": region_id,
            "seriesIndex": series_index,
            "seriesId": series_id,
            "layoutType": layout_type,
            "layoutLevel": layout_level,
            "alignSelf": align_self,
            "padding": padding,
            "width": width,
            "minWidth": min_width,
            "maxWidth": max_width,
            "height": height,
            "minHeight": min_height,
            "maxHeight": max_height,
            "offsetX": offset_x,
            "offsetY": offset_y,
            "zIndex": z_index,
            "clip": is_clip,
            "left": left,
            "right": right,
            "top": top,
            "bottom": bottom,
            "center": is_center,
        }


class AxesBreakOpts(BasicOpts):
    def __init__(
        self,
        range_: Optional[Sequence[int]] = None,
        is_break_symbol_visible: Optional[bool] = None,
        break_symbol_gap: Union[int, str] = None,
        break_symbol_angle: Union[int, str] = None,
        break_symbol_style_opts: BaseStyleOpts = None,
    ):
        self.opts = {
            "range": range_,
            "breakSymbol": {
                "visible": is_break_symbol_visible,
                "gap": break_symbol_gap,
                "angle": break_symbol_angle,
                "style": break_symbol_style_opts,
            },
        }


class AxesLayerOpts(BasicOpts):
    def __init__(
        self,
        tick_step: Optional[Numeric] = None,
        time_format: Optional[str] = None,
        time_format_mode: Optional[str] = None,
        tick_count: Optional[Numeric] = None,
        force_tick_count: Optional[Numeric] = None,
    ):
        self.opts = {
            "tickStep": tick_step,
            "timeFormat": time_format,
            "timeFormatMode": time_format_mode,
            "tickCount": tick_count,
            "forceTickCount": force_tick_count,
        }


class AxesLinearOpts(BasicOpts):
    def __init__(
        self,
        is_visible: Optional[bool] = None,
        min_: Optional[Numeric] = None,
        max_: Optional[Numeric] = None,
        soft_min: Optional[Numeric] = None,
        soft_max: Optional[Numeric] = None,
        is_nice: Optional[bool] = True,
        nice_type: Optional[str] = "tickCountFirst",
        is_zero: Optional[bool] = True,
        expand_min: Optional[Numeric] = None,
        expand_max: Optional[Numeric] = None,
        sync_axis_id: Optional[Numeric] = None,
        sync_zero_align: Optional[Numeric] = None,
        sync_tick_align: Optional[Numeric] = None,
        tooltip_filter_range: Union[int, Sequence[int], JSFunc] = None,
        breaks: Sequence[AxesBreakOpts] = None,
        base_axes_opts: BaseAxesOpts = None,
    ):
        self.opts = {}

        if base_axes_opts:
            self.opts.update(base_axes_opts.opts)

        self.opts.update(
            {
                "type": "linear",
                "visible": is_visible,
                "min": min_,
                "max": max_,
                "softMin": soft_min,
                "softMax": soft_max,
                "nice": is_nice,
                "niceType": nice_type,
                "zero": is_zero,
                "expand": {
                    "min": expand_min,
                    "max": expand_max,
                },
                "sync": {
                    "axisId": sync_axis_id,
                    "zeroAlign": sync_zero_align,
                    "tickAlign": sync_tick_align,
                },
                "tooltipFilterRange": tooltip_filter_range,
                "breaks": breaks,
            }
        )


class AxesBandOpts(BasicOpts):
    def __init__(
        self,
        is_trim_padding: Optional[bool] = None,
        band_padding: Union[Numeric, Sequence[Numeric]] = None,
        padding_inner: Union[Numeric, Sequence[Numeric]] = None,
        padding_outer: Union[Numeric, Sequence[Numeric]] = None,
        domain: Optional[Sequence] = None,
        band_size: Optional[Numeric] = None,
        max_band_size: Optional[Numeric] = None,
        min_band_size: Optional[Numeric] = None,
        is_auto_region_size: Optional[bool] = None,
        is_show_all_group_layers: Optional[bool] = None,
        layers: Sequence[AxesLayerOpts] = None,
        base_axes_opts: BaseAxesOpts = None,
    ):
        self.opts = {}

        if base_axes_opts:
            self.opts.update(base_axes_opts.opts)

        self.opts.update(
            {
                "type": "band",
                "trimPadding": is_trim_padding,
                "bandPadding": band_padding,
                "paddingInner": padding_inner,
                "paddingOuter": padding_outer,
                "domain": domain,
                "bandSize": band_size,
                "maxBandSize": max_band_size,
                "minBandSize": min_band_size,
                "autoRegionSize": is_auto_region_size,
                "showAllGroupLayers": is_show_all_group_layers,
                "layers": layers,
            }
        )


class AxesTimeOpts(BasicOpts):
    def __init__(
        self,
        min_: Optional[Numeric] = None,
        max_: Optional[Numeric] = None,
        soft_min: Optional[Numeric] = None,
        soft_max: Optional[Numeric] = None,
        is_nice: Optional[bool] = None,
        nice_type: Optional[str] = None,
        is_zero: Optional[bool] = None,
        expand_min: Optional[Numeric] = None,
        expand_max: Optional[Numeric] = None,
        sync_axis_id: Optional[Numeric] = None,
        sync_zero_align: Optional[Numeric] = None,
        sync_tick_align: Optional[Numeric] = None,
        tooltip_filter_range: Union[int, Sequence[int], JSFunc] = None,
        breaks: Sequence[AxesBreakOpts] = None,
        layers: Sequence[AxesLayerOpts] = None,
        base_axes_opts: BaseAxesOpts = None,
    ):
        self.opts: dict = {}

        if base_axes_opts:
            self.opts.update(base_axes_opts.opts)

        self.opts.update(
            {
                "type": "time",
                "min": min_,
                "max": max_,
                "softMin": soft_min,
                "softMax": soft_max,
                "nice": is_nice,
                "niceType": nice_type,
                "zero": is_zero,
                "expand": {
                    "min": expand_min,
                    "max": expand_max,
                },
                "sync": {
                    "axisId": sync_axis_id,
                    "zeroAlign": sync_zero_align,
                    "tickAlign": sync_tick_align,
                },
                "tooltipFilterRange": tooltip_filter_range,
                "breaks": breaks,
                "layers": layers,
            }
        )


class AxesLogOpts(BasicOpts):
    def __init__(
        self,
        base: Optional[int] = 10,
        base_axes_opts: BaseAxesOpts = None,
    ):
        self.opts: dict = {}

        if base_axes_opts:
            self.opts.update(base_axes_opts.opts)

        self.opts.update(
            {
                "type": "log",
                "base": base,
            }
        )


class AxesSymlogOpts(BasicOpts):
    def __init__(
        self,
        constant: Optional[int] = 10,
        base_axes_opts: BaseAxesOpts = None,
    ):
        self.opts: dict = {}

        if base_axes_opts:
            self.opts.update(base_axes_opts.opts)

        self.opts.update(
            {
                "type": "symlog",
                "constant": constant,
            }
        )


class TooltipStylePanelOpts(BasicOpts):
    def __init__(
        self,
        padding: Optional[Union[Numeric, Sequence[Numeric], dict]] = None,
        background_color: Optional[str] = None,
        border_color: Optional[str] = None,
        border_width: Optional[Numeric] = None,
        border_radius: Optional[Numeric] = None,
        shadow_x: Optional[Numeric] = None,
        shadow_y: Optional[Numeric] = None,
        shadow_blur: Optional[Numeric] = None,
        shadow_spread: Optional[Numeric] = None,
        shadow_color: Optional[str] = None,
    ):
        self.opts: dict = {
            "padding": padding,
            "backgroundColor": background_color,
            "border": {
                "color": border_color,
                "width": border_width,
                "radius": border_radius,
            },
            "shadow": {
                "x": shadow_x,
                "y": shadow_y,
                "blur": shadow_blur,
                "spread": shadow_spread,
                "color": shadow_color,
            },
        }


class TooltipStyleShapeOpts(BasicOpts):
    def __init__(
        self,
        size: Optional[Numeric] = None,
        spacing: Optional[Numeric] = None,
        is_has_shape: Optional[bool] = None,
        shape_type: Optional[str] = None,
        is_shape_hollow: Optional[bool] = None,
        shape_fill: Optional[str] = None,
        shape_stroke: Optional[str] = None,
        shape_line_width: Optional[Numeric] = None,
        shape_size: Optional[Numeric] = None,
        shape_color: Optional[str] = None,
    ):
        self.opts: dict = {
            "size": size,
            "spacing": spacing,
            "hasShape": is_has_shape,
            "shapeType": shape_type,
            "shapeHollow": is_shape_hollow,
            "shapeFill": shape_fill,
            "shapeStroke": shape_stroke,
            "shapeLineWidth": shape_line_width,
            "shapeSize": shape_size,
            "shapeColor": shape_color,
        }


class TooltipStyleOpts(BasicOpts):
    def __init__(
        self,
        panel_opts: Optional[TooltipStylePanelOpts] = None,
        shape_opts: Optional[TooltipStyleShapeOpts] = None,
        title_label_opts: Optional[LabelOpts] = None,
        key_label_opts: Optional[LabelOpts] = None,
        value_label_opts: Optional[LabelOpts] = None,
        space_row: Optional[Numeric] = None,
        max_content_height: Optional[Numeric] = None,
        align: Optional[str] = None,
    ):
        self.opts: dict = {
            "panel": panel_opts,
            "shape": shape_opts,
            "titleLabel": title_label_opts,
            "keyLabel": key_label_opts,
            "valueLabel": value_label_opts,
            "spaceRow": space_row,
            "maxContentHeight": max_content_height,
            "align": align,
        }


class TooltipCustomStyleOpts(BasicOpts):
    def __init__(
        self,
        is_visible: Optional[bool] = None,
        key: Optional[Union[str, JSFunc]] = None,
        key_time_format: Optional[str] = None,
        key_time_format_mode: Optional[str] = None,
        key_formatter: Optional[str] = None,
        value: Optional[Union[str, JSFunc]] = None,
        value_time_format: Optional[str] = None,
        value_time_format_mode: Optional[str] = None,
        value_formatter: Optional[str] = None,
        is_has_shape: Optional[bool] = None,
        shape_type: Optional[str] = None,
        is_shape_hollow: Optional[bool] = None,
        shape_fill: Optional[str] = None,
        shape_stroke: Optional[str] = None,
        shape_line_width: Optional[Numeric] = None,
        shape_size: Optional[Numeric] = None,
        shape_color: Optional[str] = None,
    ):
        self.opts: dict = {
            "visible": is_visible,
            "key": key,
            "keyTimeFormat": key_time_format,
            "keyTimeFormatMode": key_time_format_mode,
            "keyFormatter": key_formatter,
            "value": value,
            "valueTimeFormat": value_time_format,
            "valueTimeFormatMode": value_time_format_mode,
            "valueFormatter": value_formatter,
            "hasShape": is_has_shape,
            "shapeType": shape_type,
            "shapeHollow": is_shape_hollow,
            "shapeFill": shape_fill,
            "shapeStroke": shape_stroke,
            "shapeLineWidth": shape_line_width,
            "shapeSize": shape_size,
            "shapeColor": shape_color,
        }


class TooltipCustomStylePositionOpts(BasicOpts):
    def __init__(
        self,
        left: Optional[Union[Numeric, JSFunc]] = None,
        right: Optional[Union[Numeric, JSFunc]] = None,
        top: Optional[Union[Numeric, JSFunc]] = None,
        bottom: Optional[Union[Numeric, JSFunc]] = None,
        x_orient: Optional[str] = None,
        x_mode: Optional[str] = None,
        x_offset: Optional[Numeric] = None,
        y_orient: Optional[str] = None,
        y_mode: Optional[str] = None,
        y_offset: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "left": left,
            "right": right,
            "top": top,
            "bottom": bottom,
            "x": {
                "orient": x_orient,
                "mode": x_mode,
                "offset": x_offset,
            },
            "y": {
                "orient": y_orient,
                "mode": y_mode,
                "offset": y_offset,
            },
        }


class TooltipCustomOpts(BasicOpts):
    def __init__(
        self,
        is_visible: Optional[bool] = None,
        trigger_mask: Optional[Union[str, Sequence[str]]] = None,
        is_title_visible: Optional[bool] = None,
        title_value: Optional[Union[str, JSFunc]] = None,
        title_value_time_format: Optional[str] = None,
        title_value_time_format_mode: Optional[str] = None,
        title_value_formatter: Optional[str] = None,
        content: Optional[
            Union[TooltipCustomStyleOpts, Sequence[TooltipCustomStyleOpts]]
        ] = None,
        position: Optional[TooltipCustomStylePositionOpts] = None,
        position_mode: Optional[str] = None,
        update_content: Optional[JSFunc] = None,
        update_title: Optional[JSFunc] = None,
        max_line_count: Optional[Numeric] = None,
        is_has_shape: Optional[bool] = None,
        shape_type: Optional[Union[str, JSFunc]] = None,
        shape_hollow: Optional[Union[str, JSFunc]] = None,
        shape_stroke: Optional[Union[str, JSFunc]] = None,
        shape_line_width: Optional[Union[Numeric, JSFunc]] = None,
        shape_size: Optional[Union[Numeric, JSFunc]] = None,
        shape_color: Optional[Union[str, JSFunc]] = None,
        others_line_opts: Optional[TooltipCustomStyleOpts] = None,
    ):
        self.opts: dict = {
            "visible": is_visible,
            "triggerMask": trigger_mask,
            "title": {
                "visible": is_title_visible,
                "value": title_value,
                "valueTimeFormat": title_value_time_format,
                "valueTimeFormatMode": title_value_time_format_mode,
                "valueFormatter": title_value_formatter,
            },
            "content": content,
            "position": position,
            "positionMode": position_mode,
            "updateContent": update_content,
            "updateTitle": update_title,
            "maxLineCount": max_line_count,
            "hasShape": is_has_shape,
            "shapeType": shape_type,
            "shapeHollow": shape_hollow,
            "shapeStroke": shape_stroke,
            "shapeLineWidth": shape_line_width,
            "shapeSize": shape_size,
            "shapeColor": shape_color,
            "othersLine": others_line_opts,
        }


class TooltipOpts(BasicOpts):
    def __init__(
        self,
        is_visible: Optional[bool] = True,
        active_type: Optional[Sequence[str]] = None,
        trigger: Optional[str] = None,
        is_lock_after_click: Optional[bool] = None,
        hide_timer: Optional[Numeric] = None,
        show_delay: Optional[Numeric] = None,
        mark_opts: Optional[TooltipCustomOpts] = None,
        dimension_opts: Optional[TooltipCustomOpts] = None,
        group_opts: Optional[TooltipCustomOpts] = None,
        render_mode: Optional[str] = None,
        is_confine: Optional[bool] = None,
        class_name: Optional[str] = None,
        parent_element: Union[str, JSFunc] = None,
        is_enterable: Optional[bool] = None,
        transition_duration: Optional[Numeric] = None,
        throttle_interval: Optional[Numeric] = None,
        update_element: Optional[JSFunc] = None,
        style_opts: Optional[TooltipStyleOpts] = None,
        offset_x: Optional[Numeric] = None,
        offset_y: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "visible": is_visible,
            "activeType": active_type,
            "trigger": trigger,
            "lockAfterClick": is_lock_after_click,
            "hideTimer": hide_timer,
            "showDelay": show_delay,
            "mark": mark_opts,
            "dimension": dimension_opts,
            "group": group_opts,
            "renderMode": render_mode,
            "confine": is_confine,
            "className": class_name,
            "parentElement": parent_element,
            "enterable": is_enterable,
            "transitionDuration": transition_duration,
            "throttleInterval": throttle_interval,
            "updateElement": update_element,
            "style": style_opts,
            "offset": {
                "x": offset_x,
                "y": offset_y,
            },
        }


class LayoutColRowOpts(BasicOpts):
    def __init__(
        self,
        index_: Optional[int] = None,
        size: Optional[int] = None,
    ):
        self.opts: dict = {
            "index": index_,
            "size": size,
        }


class LayoutElementOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        col: Optional[int] = None,
        row: Optional[int] = None,
        col_span: Optional[int] = 1,
        row_span: Optional[int] = 1,
    ):
        self.opts: dict = {
            "id": id_,
            "col": col,
            "row": row,
            "colSpan": col_span,
            "rowSpan": row_span,
        }


class LayoutOpts(BasicOpts):
    def __init__(
        self,
        type_: Optional[str] = "grid",
        col: Optional[int] = None,
        row: Optional[int] = None,
        col_width: Optional[Sequence[LayoutColRowOpts]] = None,
        row_height: Optional[Sequence[LayoutColRowOpts]] = None,
        elements: Optional[Sequence[LayoutElementOpts]] = None,
    ):
        self.opts: dict = {
            "type": type_,
            "col": col,
            "row": row,
            "colWidth": col_width,
            "rowHeight": row_height,
            "elements": elements,
        }


class PlayerSliderOpts(BasicOpts):
    def __init__(
        self,
        is_visible: Optional[bool] = None,
        space: Optional[int] = None,
        dx: Optional[int] = None,
        dy: Optional[int] = None,
        rail_style_opts: BaseStyleOpts = None,
        track_style_opts: BaseStyleOpts = None,
        handler_style_opts: BaseStyleOpts = None,
    ):
        self.opts: dict = {
            "visible": is_visible,
            "space": space,
            "dx": dx,
            "dy": dy,
            "railStyle": rail_style_opts,
            "trackStyle": track_style_opts,
            "handlerStyle": handler_style_opts,
        }


class PlayerControllerPositionOpts(BasicOpts):
    def __init__(
        self,
        space: Optional[int] = None,
        order: Optional[int] = None,
        position: Optional[str] = None,
        style_opts: Optional[BaseStyleOpts] = None,
    ):
        self.opts: dict = {
            "space": space,
            "order": order,
            "position": position,
            "style": style_opts,
        }


class PlayerControllerOpts(BasicOpts):
    def __init__(
        self,
        is_visible: Optional[bool] = None,
        start_opts: Optional[PlayerControllerPositionOpts] = None,
        pause_opts: Optional[PlayerControllerPositionOpts] = None,
        backward_opts: Optional[PlayerControllerPositionOpts] = None,
        forward_opts: Optional[PlayerControllerPositionOpts] = None,
    ):
        self.opts: dict = {
            "visible": is_visible,
            "start": start_opts,
            "pause": pause_opts,
            "backward": backward_opts,
            "forward": forward_opts,
        }


class PlayerSpecOpts(BasicOpts):
    def __init__(
        self,
        data_id: Optional[str] = None,
        data_values: Optional[Union[Sequence, dict]] = None,
    ):
        self.opts: dict = {
            "data": {
                "id": data_id,
                "values": data_values,
            }
        }


class PlayerOpts(BasicOpts):
    def __init__(
        self,
        specs: Optional[Sequence[PlayerSpecOpts]] = None,
        type_: Optional[str] = None,
        interval: Optional[int] = 1000,
        total_duration: Optional[Numeric] = None,
        direction: Optional[str] = "default",
        is_auto: Optional[bool] = None,
        is_loop: Optional[bool] = None,
        is_alternate: Optional[bool] = None,
        is_visible: Optional[bool] = None,
        dx: Optional[int] = None,
        dy: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        position: Optional[str] = None,
        orient: Optional[str] = None,
        slider: PlayerSliderOpts = None,
        controller: PlayerControllerOpts = None,
    ):
        self.opts: dict = {
            "specs": specs,
            "type": type_,
            "interval": interval,
            "totalDuration": total_duration,
            "direction": direction,
            "auto": is_auto,
            "loop": is_loop,
            "alternate": is_alternate,
            "visible": is_visible,
            "dx": dx,
            "dy": dy,
            "width": width,
            "height": height,
            "position": position,
            "orient": orient,
            "slider": slider,
            "controller": controller,
        }


class ScrollBarOpts(BasicOpts):
    def __init__(
        self,
        is_round: Optional[bool] = None,
        is_inner_padding: Optional[bool] = None,
        range_: Optional[Sequence[Numeric]] = None,
        limit_range: Optional[Sequence[Numeric]] = None,
        rail_style_opts: Optional[BaseStyleOpts] = None,
        slider_style_opts: Optional[BaseStyleOpts] = None,
        is_visible: Optional[bool] = None,
        orient: Optional[str] = None,
        width: Union[str, int] = None,
        height: Union[str, int] = None,
        field: Optional[str] = None,
        axis_id: Optional[str] = None,
        axis_index: Optional[int] = None,
        region_id: Optional[str] = None,
        region_index: Optional[int] = None,
        filter_mode: Optional[str] = None,
        start: Optional[Numeric] = None,
        end: Optional[Numeric] = None,
        start_value: Union[str, int] = None,
        end_value: Union[str, int] = None,
        range_mode: Optional[Sequence[str]] = None,
        is_auto_indent: Optional[bool] = None,
        is_auto: Optional[bool] = None,
        is_zoom_lock: Optional[bool] = None,
        min_span: Optional[Numeric] = None,
        max_span: Optional[Numeric] = None,
        min_value_span: Optional[Numeric] = None,
        max_value_span: Optional[Numeric] = None,
        delay_type: Optional[str] = None,
        delay_time: Optional[Numeric] = None,
        is_roam_zoom_focus: Optional[bool] = None,
        is_roam_zoom_enable: Optional[bool] = None,
        roam_zoom_rate: Optional[Numeric] = None,
        is_roam_drag_reverse: Optional[bool] = None,
        is_roam_drag_enable: Optional[bool] = None,
        roam_drag_rate: Optional[Numeric] = None,
        is_roam_scroll_reverse: Optional[bool] = None,
        is_realtime: Optional[bool] = None,
        custom_domain: Optional[Sequence] = None,
        is_update_data_after_change_enable: Optional[bool] = None,
        update_data_after_change_rate: Optional[Numeric] = None,
        layout_type: Optional[str] = None,
        layout_level: Optional[int] = None,
        align_self: Optional[str] = None,
        padding: Optional[PaddingOpts] = None,
        min_width: Union[int, str] = None,
        max_width: Union[int, str] = None,
        min_height: Union[int, str] = None,
        max_height: Union[int, str] = None,
        offset_x: Union[int, str] = None,
        offset_y: Union[int, str] = None,
        z_index: Optional[int] = None,
        is_clip: Optional[bool] = None,
        left: Union[int, str] = None,
        right: Union[int, str] = None,
        top: Union[int, str] = None,
        bottom: Union[int, str] = None,
        is_center: Optional[bool] = None,
    ):
        self.opts: dict = {
            "round": is_round,
            "innerPadding": is_inner_padding,
            "range": range_,
            "limitRange": limit_range,
            "rail": {
                "style": rail_style_opts,
            },
            "slider": {
                "style": slider_style_opts,
            },
            "visible": is_visible,
            "orient": orient,
            "width": width,
            "height": height,
            "field": field,
            "axisId": axis_id,
            "axisIndex": axis_index,
            "regionId": region_id,
            "regionIndex": region_index,
            "filterMode": filter_mode,
            "start": start,
            "end": end,
            "startValue": start_value,
            "endValue": end_value,
            "rangeMode": range_mode,
            "autoIndent": is_auto_indent,
            "auto": is_auto,
            "zoomLock": is_zoom_lock,
            "minSpan": min_span,
            "maxSpan": max_span,
            "minValueSpan": min_value_span,
            "maxValueSpan": max_value_span,
            "delayType": delay_type,
            "delayTime": delay_time,
            "roamZoom": {
                "focus": is_roam_zoom_focus,
                "enable": is_roam_zoom_enable,
                "rate": roam_zoom_rate,
            },
            "roamDrag": {
                "reverse": is_roam_drag_reverse,
                "enable": is_roam_drag_enable,
                "rate": roam_drag_rate,
            },
            "roamScroll": {
                "reverse": is_roam_scroll_reverse,
            },
            "realTime": is_realtime,
            "customDomain": custom_domain,
            "updateDataAfterChange": {
                "enable": is_update_data_after_change_enable,
                "rate": update_data_after_change_rate,
            },
            "layoutType": layout_type,
            "layoutLevel": layout_level,
            "alignSelf": align_self,
            "padding": padding,
            "minWidth": min_width,
            "maxWidth": max_width,
            "minHeight": min_height,
            "maxHeight": max_height,
            "offsetX": offset_x,
            "offsetY": offset_y,
            "zIndex": z_index,
            "clip": is_clip,
            "left": left,
            "right": right,
            "top": top,
            "bottom": bottom,
            "center": is_center,
        }


class DataZoomOpts(BasicOpts):
    def __init__(
        self,
        value_field: Optional[str] = None,
        start_text_padding: Union[int, Sequence[int]] = None,
        start_text_style_opts: Optional[BaseTitleTextStyleOpts] = None,
        start_text_format_method: Optional[JSFunc] = None,
        end_text_padding: Union[int, Sequence[int]] = None,
        end_text_style_opts: Optional[BaseTitleTextStyleOpts] = None,
        end_text_format_method: Optional[JSFunc] = None,
        is_brush_select: Optional[bool] = None,
        show_detail: Union[bool, str] = None,
        is_middle_handler_visible: Optional[bool] = None,
        middle_handler_icon_style_opts: Optional[BaseStyleOpts] = None,
        middle_handler_background_size: Optional[int] = None,
        middle_handler_background_style_opts: Optional[BaseStyleOpts] = None,
        background_size: Union[int, dict] = None,
        background_style_opts: Optional[BaseStyleOpts] = None,
        start_handler_style_opts: Optional[BaseStyleOpts] = None,
        end_handler_style_opts: Optional[BaseStyleOpts] = None,
        drag_mask_style_opts: Optional[BaseStyleOpts] = None,
        selected_background_style_opts: Optional[BaseStyleOpts] = None,
        is_show_background_chart: Optional[bool] = None,
        background_chart_line_style_opts: Optional[BaseStyleOpts] = None,
        background_chart_area_style_opts: Optional[BaseStyleOpts] = None,
        selected_background_chart_line_style_opts: Optional[BaseStyleOpts] = None,
        selected_background_chart_area_style_opts: Optional[BaseStyleOpts] = None,
        is_ignore_band_size: Optional[bool] = None,
        tolerance: Optional[int] = None,
        is_visible: Optional[bool] = None,
        orient: Optional[str] = None,
        width: Union[str, int] = None,
        height: Union[str, int] = None,
        field: Optional[str] = None,
        axis_id: Optional[str] = None,
        axis_index: Optional[int] = None,
        region_id: Optional[str] = None,
        region_index: Optional[Union[Numeric, Sequence[Numeric]]] = None,
        filter_mode: Optional[str] = None,
        start: Optional[Numeric] = None,
        end: Optional[Numeric] = None,
        start_value: Union[str, int] = None,
        end_value: Union[str, int] = None,
        range_mode: Optional[Sequence[str]] = None,
        is_auto_indent: Optional[bool] = None,
        is_auto: Optional[bool] = None,
        is_zoom_lock: Optional[bool] = None,
        min_span: Optional[Numeric] = None,
        max_span: Optional[Numeric] = None,
        min_value_span: Optional[Numeric] = None,
        max_value_span: Optional[Numeric] = None,
        delay_type: Optional[str] = None,
        delay_time: Optional[Numeric] = None,
        is_roam_zoom_focus: Optional[bool] = None,
        is_roam_zoom_enable: Optional[bool] = None,
        roam_zoom_rate: Optional[Numeric] = None,
        is_roam_drag_reverse: Optional[bool] = None,
        is_roam_drag_enable: Optional[bool] = None,
        roam_drag_rate: Optional[Numeric] = None,
        is_roam_scroll_reverse: Optional[bool] = None,
        is_realtime: Optional[bool] = None,
        custom_domain: Optional[Sequence] = None,
        is_update_data_after_change_enable: Optional[bool] = None,
        update_data_after_change_rate: Optional[Numeric] = None,
        layout_type: Optional[str] = None,
        layout_level: Optional[int] = None,
        align_self: Optional[str] = None,
        padding: Optional[PaddingOpts] = None,
        min_width: Union[int, str] = None,
        max_width: Union[int, str] = None,
        min_height: Union[int, str] = None,
        max_height: Union[int, str] = None,
        offset_x: Union[int, str] = None,
        offset_y: Union[int, str] = None,
        z_index: Optional[int] = None,
        is_clip: Optional[bool] = None,
        left: Union[int, str] = None,
        right: Union[int, str] = None,
        top: Union[int, str] = None,
        bottom: Union[int, str] = None,
        is_center: Optional[bool] = None,
    ):
        self.opts = {
            "valueField": value_field,
            "startText": {
                "padding": start_text_padding,
                "style": start_text_style_opts,
                "formatMethod": start_text_format_method,
            },
            "endText": {
                "padding": end_text_padding,
                "style": end_text_style_opts,
                "formatMethod": end_text_format_method,
            },
            "brushSelect": is_brush_select,
            "showDetail": show_detail,
            "middleHandler": {
                "visible": is_middle_handler_visible,
                "icon": {
                    "style": middle_handler_icon_style_opts,
                },
                "background": {
                    "size": middle_handler_background_size,
                    "style": middle_handler_background_style_opts,
                },
            },
            "background": {
                "size": background_size,
                "style": background_style_opts,
            },
            "startHandler": {
                "style": start_handler_style_opts,
            },
            "endHandler": {
                "style": end_handler_style_opts,
            },
            "dragMask": {
                "style": drag_mask_style_opts,
            },
            "selectedBackground": {
                "style": selected_background_style_opts,
            },
            "showBackgroundChart": is_show_background_chart,
            "backgroundChart": {
                "line": {
                    "style": background_chart_line_style_opts,
                },
                "area": {
                    "style": background_chart_area_style_opts,
                },
            },
            "selectedBackgroundChart": {
                "line": {
                    "style": selected_background_chart_line_style_opts,
                },
                "area": {
                    "style": selected_background_chart_area_style_opts,
                },
            },
            "ignoreBandSize": is_ignore_band_size,
            "tolerance": tolerance,
            "visible": is_visible,
            "orient": orient,
            "width": width,
            "height": height,
            "field": field,
            "axisId": axis_id,
            "axisIndex": axis_index,
            "regionId": region_id,
            "regionIndex": region_index,
            "filterMode": filter_mode,
            "start": start,
            "end": end,
            "startValue": start_value,
            "endValue": end_value,
            "rangeMode": range_mode,
            "autoIndent": is_auto_indent,
            "auto": is_auto,
            "zoomLock": is_zoom_lock,
            "minSpan": min_span,
            "maxSpan": max_span,
            "minValueSpan": min_value_span,
            "maxValueSpan": max_value_span,
            "delayType": delay_type,
            "delayTime": delay_time,
            "roamZoom": {
                "focus": is_roam_zoom_focus,
                "enable": is_roam_zoom_enable,
                "rate": roam_zoom_rate,
            },
            "roamDrag": {
                "reverse": is_roam_drag_reverse,
                "enable": is_roam_drag_enable,
                "rate": roam_drag_rate,
            },
            "roamScroll": {
                "reverse": is_roam_scroll_reverse,
            },
            "realTime": is_realtime,
            "customDomain": custom_domain,
            "updateDataAfterChange": {
                "enable": is_update_data_after_change_enable,
                "rate": update_data_after_change_rate,
            },
            "layoutType": layout_type,
            "layoutLevel": layout_level,
            "alignSelf": align_self,
            "padding": padding,
            "minWidth": min_width,
            "maxWidth": max_width,
            "minHeight": min_height,
            "maxHeight": max_height,
            "offsetX": offset_x,
            "offsetY": offset_y,
            "zIndex": z_index,
            "clip": is_clip,
            "left": left,
            "right": right,
            "top": top,
            "bottom": bottom,
            "center": is_center,
        }


class BrushOpts(BasicOpts):
    def __init__(
        self,
        is_visible: Optional[bool] = None,
        region_index: Union[int, Sequence[int]] = None,
        region_id: Union[int, str, Sequence[int], Sequence[str]] = None,
        series_index: Union[int, Sequence[int]] = None,
        series_id: Union[int, str, Sequence[int], Sequence[str]] = None,
        brush_link_series_index: Union[int, Sequence[int]] = None,
        brush_link_series_id: Union[int, str, Sequence[int], Sequence[str]] = None,
        in_brush: Optional[BaseStyleOpts] = None,
        out_of_brush: Optional[BaseStyleOpts] = None,
        brush_mode: Optional[str] = None,
        brush_type: Optional[str] = None,
        is_brush_moved: Optional[bool] = None,
        is_remove_onclick: Optional[bool] = None,
        delay_type: Optional[str] = None,
        delay_time: Optional[Numeric] = None,
        size_threshold: Optional[int] = None,
        is_zoom_after_brush: Optional[bool] = None,
    ):
        self.opts = {
            "visible": is_visible,
            "regionIndex": region_index,
            "regionId": region_id,
            "seriesIndex": series_index,
            "seriesId": series_id,
            "brushLinkSeriesIndex": brush_link_series_index,
            "brushLinkSeriesId": brush_link_series_id,
            "inBrush": in_brush,
            "outOfBrush": out_of_brush,
            "brushMode": brush_mode,
            "brushType": brush_type,
            "brushMoved": is_brush_moved,
            "removeOnClick": is_remove_onclick,
            "delayType": delay_type,
            "delayTime": delay_time,
            "sizeThreshold": size_threshold,
            "zoomAfterBrush": is_zoom_after_brush,
        }


class ZoomWhenEmptyOpts(BasicOpts):
    def __init__(
        self,
        axis_id: Optional[str] = None,
        axis_index: Optional[int] = None,
        axis_range_expand: Optional[int] = None,
        style_opts: Optional[BaseStyleOpts] = None,
    ):
        self.opts = {
            "axisId": axis_id,
            "axisIndex": axis_index,
            "axisRangeExpand": axis_range_expand,
            "style": style_opts,
        }


class ScalesOpts(BasicOpts):
    def __init__(
        self,
        id_: Optional[str] = None,
        type_: Optional[str] = None,
        domain: Optional[Sequence] = None,
        range_: Optional[Sequence] = None,
        specified: Optional[dict] = None,
    ):
        self.opts = {
            "id": id_,
            "type": type_,
            "domain": domain,
            "range": range_,
            "specified": specified,
        }


class BaseCustomMarkOpts(BasicOpts):
    def __init__(
        self,
        type_: Optional[str] = None,
        data_index: Optional[Numeric] = None,
        data_id: Optional[str] = None,
        data_key: Union[str, JSFunc] = None,
        component_type: Optional[str] = None,
        id_: Union[str, Numeric] = None,
        is_interactive: Optional[bool] = None,
        z_index: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JSFunc] = None,
        state_sort: Optional[JSFunc] = None,
        animation: Optional[AnimationOpts] = None,
        animation_appear: Optional[AnimationOpts] = None,
        animation_enter: Optional[AnimationOpts] = None,
        animation_update: Optional[AnimationOpts] = None,
        animation_exit: Optional[AnimationOpts] = None,
        style_opts: Optional[BaseStyleOpts] = None,
        layout_type: Optional[str] = None,
        layout_level: Optional[int] = None,
        align_self: Optional[str] = None,
        padding: Optional[PaddingOpts] = None,
        width: Union[int, str] = None,
        min_width: Union[int, str] = None,
        max_width: Union[int, str] = None,
        height: Union[int, str] = None,
        min_height: Union[int, str] = None,
        max_height: Union[int, str] = None,
        offset_x: Union[int, str] = None,
        offset_y: Union[int, str] = None,
        is_clip: Optional[bool] = None,
        left: Union[int, str] = None,
        right: Union[int, str] = None,
        top: Union[int, str] = None,
        bottom: Union[int, str] = None,
        is_center: Optional[bool] = None,
    ):
        self.opts = {
            "type": type_,
            "dataIndex": data_index,
            "dataId": data_id,
            "dataKey": data_key,
            "componentType": component_type,
            "id": id_,
            "interactive": is_interactive,
            "zIndex": z_index,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "animation": animation,
            "animationAppear": animation_appear,
            "animationEnter": animation_enter,
            "animationUpdate": animation_update,
            "animationExit": animation_exit,
            "style": style_opts,
            "layoutType": layout_type,
            "layoutLevel": layout_level,
            "alignSelf": align_self,
            "padding": padding,
            "width": width,
            "minWidth": min_width,
            "maxWidth": max_width,
            "height": height,
            "minHeight": min_height,
            "maxHeight": max_height,
            "offsetX": offset_x,
            "offsetY": offset_y,
            "clip": is_clip,
            "left": left,
            "right": right,
            "top": top,
            "bottom": bottom,
            "center": is_center,
        }


class CustomMarkSymbolOpts(BasicOpts):
    def __init__(
        self,
        base_custom_mark_opts: Optional[BaseCustomMarkOpts] = None,
    ):
        self.opts = {}

        if base_custom_mark_opts:
            self.opts.update(base_custom_mark_opts.opts)

        self.opts.update({"type": "symbol"})


class CustomMarkRuleOpts(BasicOpts):
    def __init__(
        self,
        base_custom_mark_opts: Optional[BaseCustomMarkOpts] = None,
    ):
        self.opts = {}

        if base_custom_mark_opts:
            self.opts.update(base_custom_mark_opts.opts)

        self.opts.update({"type": "rule"})


class CustomMarkTextOpts(BasicOpts):
    def __init__(
        self,
        base_custom_mark_opts: Optional[BaseCustomMarkOpts] = None,
    ):
        self.opts = {}

        if base_custom_mark_opts:
            self.opts.update(base_custom_mark_opts.opts)

        self.opts.update({"type": "text"})


class CustomMarkRectOpts(BasicOpts):
    def __init__(
        self,
        base_custom_mark_opts: Optional[BaseCustomMarkOpts] = None,
    ):
        self.opts = {}

        if base_custom_mark_opts:
            self.opts.update(base_custom_mark_opts.opts)

        self.opts.update({"type": "rect"})


class CustomMarkPathOpts(BasicOpts):
    def __init__(
        self,
        base_custom_mark_opts: Optional[BaseCustomMarkOpts] = None,
    ):
        self.opts = {}

        if base_custom_mark_opts:
            self.opts.update(base_custom_mark_opts.opts)

        self.opts.update({"type": "path"})


class CustomMarkArcOpts(BasicOpts):
    def __init__(
        self,
        base_custom_mark_opts: Optional[BaseCustomMarkOpts] = None,
    ):
        self.opts = {}

        if base_custom_mark_opts:
            self.opts.update(base_custom_mark_opts.opts)

        self.opts.update({"type": "arc"})


class CustomMarkPolygonOpts(BasicOpts):
    def __init__(
        self,
        base_custom_mark_opts: Optional[BaseCustomMarkOpts] = None,
    ):
        self.opts = {}

        if base_custom_mark_opts:
            self.opts.update(base_custom_mark_opts.opts)

        self.opts.update({"type": "polygon"})


class CustomMarkImageOpts(BasicOpts):
    def __init__(
        self,
        base_custom_mark_opts: Optional[BaseCustomMarkOpts] = None,
    ):
        self.opts = {}

        if base_custom_mark_opts:
            self.opts.update(base_custom_mark_opts.opts)

        self.opts.update({"type": "image"})


class CustomMarkGroupOpts(BasicOpts):
    def __init__(
        self,
        children: Optional[Sequence[BaseCustomMarkOpts]] = None,
        base_custom_mark_opts: Optional[BaseCustomMarkOpts] = None,
    ):
        self.opts = {}

        if base_custom_mark_opts:
            self.opts.update(base_custom_mark_opts.opts)

        self.opts.update(
            {
                "type": "group",
                "children": children,
            }
        )


class ThemeOpts(BasicOpts):
    def __init__(
        self,
        name: Optional[str] = None,
        background: Union[str, dict] = None,
        padding: Union[int, Sequence[int], JSFunc] = None,
        font_family: Optional[str] = None,
        color_scheme: Optional[Union[Sequence[str], dict]] = None,
        series: Optional[dict] = None,
        component: Optional[dict] = None,
    ):
        self.opts = {
            "name": name,
            "background": background,
            "padding": padding,
            "fontFamily": font_family,
            "colorScheme": color_scheme,
            "series": series,
            "component": component,
        }


class HoverOpts(BasicOpts):
    def __init__(
        self,
        is_enable: Optional[bool] = None,
        trigger: Optional[Union[str, Sequence[str]]] = None,
        trigger_off: Optional[Union[str, Sequence[str]]] = None,
    ):
        self.opts = {
            "enable": is_enable,
            "trigger": trigger,
            "triggerOff": trigger_off,
        }


class SelectOpts(BasicOpts):
    def __init__(
        self,
        is_enable: Optional[bool] = None,
        mode: Optional[str] = None,
        trigger: Optional[Union[str, Sequence[str]]] = None,
        trigger_off: Optional[Union[str, Sequence[str]]] = None,
    ):
        self.opts = {
            "enable": is_enable,
            "mode": mode,
            "trigger": trigger,
            "triggerOff": trigger_off,
        }
