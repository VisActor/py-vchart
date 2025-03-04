from ..commons.utils import JsCode
from .series_options import (
    AnimationOpts,
    BasicOpts,
    Numeric,
    Optional,
    Sequence,
    Union,
)
from .global_options import (
    BaseStyleOpts,
    BaseStateOpts,
    PaddingOpts,
    LabelStyleOpts,
    HoverOpts,
    SelectOpts,
    LabelOpts,
)


class BaseDataOpts(BasicOpts):
    def __init__(
        self,
        values: Optional[Sequence],
        *,
        id_: Optional[Union[str, Numeric]] = None,
        from_data_id: Optional[Union[str, Numeric]] = None,
        from_data_index: Optional[Union[str, Numeric]] = None,
        transform: Optional[Union[dict, Sequence[dict]]] = None,
        fields: Optional[dict] = None,
        parser: Optional[dict] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "values": values,
            "fromDataId": from_data_id,
            "fromDataIndex": from_data_index,
            "transform": transform,
            "fields": fields,
            "parser": parser,
        }


class InteractionOpts(BasicOpts):
    def __init__(
        self,
        mark_ids: Optional[Sequence] = None,
        mark_names: Optional[Sequence] = None,
        type_: Optional[str] = None,
        state: Optional[str] = None,
        filter_type: Optional[str] = None,
        filter_field: Optional[str] = None,
        highlight_state: Optional[str] = None,
        blur_state: Optional[str] = None,
        is_multiple: Optional[bool] = None,
        trigger: Optional[Union[str, Sequence[str]]] = None,
        trigger_off: Optional[Union[str, Sequence[str]]] = None,
        graphic_name: Optional[Union[str, Sequence]] = None,
        parse_data: Optional[JsCode] = None,
    ):
        self.opts: dict = {
            "markIds": mark_ids,
            "markNames": mark_names,
            "type": type_,
            "state": state,
            "filterType": filter_type,
            "filterField": filter_field,
            "highlightState": highlight_state,
            "blurState": blur_state,
            "isMultiple": is_multiple,
            "trigger": trigger,
            "triggerOff": trigger_off,
            "graphicName": graphic_name,
            "parseData": parse_data,
        }


class BarOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[dict] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class BarBackgroundOpts(BasicOpts):
    def __init__(
        self,
        field_level: Optional[Numeric] = None,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[dict] = None,
    ):
        self.opts: dict = {
            "fieldLevel": field_level,
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class Bar3DOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class PieOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class LineOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class PointOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
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
        image: Optional[JsCode] = None,
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
        hover_image: Optional[Union[str, JsCode]] = None,
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


class LineCurveLabelOpts(BasicOpts):
    def __init__(
        self,
        position: Union[str, JsCode] = "end",
        is_visible: bool = False,
        is_interactive: bool = False,
        format_method: Optional[JsCode] = None,
        formatter: Optional[str] = None,
        is_sync_state: bool = False,
        offset: Optional[int] = 5,
        style_opts: Optional[LabelStyleOpts] = None,
        state_opts: Optional[BaseStateOpts] = None,
        is_overlap_hide_on_hit: Optional[bool] = None,
        is_overlap_clamp_force: Optional[bool] = None,
        is_overlap_avoid_base_mark: Optional[bool] = None,
        overlap_strategy: Optional[Sequence] = None,
        data_filter: Optional[JsCode] = None,
        custom_layout_func: Optional[JsCode] = None,
        custom_overlap_func: Optional[JsCode] = None,
        animation: Optional[AnimationOpts] = None,
        stack_data_filter_type: Optional[str] = None,
        invalid_type: Optional[str] = None,
    ):
        self.opts: dict = {
            "position": position,
            "visible": is_visible,
            "interactive": is_interactive,
            "formatMethod": format_method,
            "formatter": formatter,
            "syncState": is_sync_state,
            "offset": offset,
            "style": style_opts,
            "state": state_opts,
            "overlap": {
                "hideOnHit": is_overlap_hide_on_hit,
                "clampForce": is_overlap_clamp_force,
                "avoidBaseMark": is_overlap_avoid_base_mark,
                "strategy": overlap_strategy,
            },
            "dataFilter": data_filter,
            "customLayoutFunc": custom_layout_func,
            "customOverlapFunc": custom_overlap_func,
            "animation": animation,
            "stackDataFilterType": stack_data_filter_type,
            "invalidType": invalid_type,
        }


class AreaOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class HeatMapCellOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class HeatMapCellBackgroundOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class ProgressOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        top_padding: Optional[int] = None,
        bottom_padding: Optional[int] = None,
        left_padding: Optional[int] = None,
        right_padding: Optional[int] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "topPadding": top_padding,
            "bottomPadding": bottom_padding,
            "leftPadding": left_padding,
            "rightPadding": right_padding,
            "style": style,
            "state": state,
        }


class TrackOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class SankeyNodeOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class SankeyLinkOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class SankeyEmphasisOpts(BasicOpts):
    def __init__(
        self,
        is_enable: Optional[bool] = None,
        trigger: Optional[str] = None,
        effect: Optional[str] = None,
    ):
        self.opts: dict = {
            "enable": is_enable,
            "trigger": trigger,
            "effect": effect,
        }


class FunnelOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class FunnelTransformOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class Funnel3DOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class WordCloudConfigOpts(BasicOpts):
    def __init__(
        self,
        draw_out_of_bound: Optional[str] = None,
        ellipsis_string: Optional[str] = None,
        ellipsis_limit_length: Optional[str] = None,
        is_zoom_to_fit_shrink: Optional[bool] = None,
        is_zoom_to_fit_enlarge: Optional[bool] = None,
        zoom_to_fit_font_size_limit_min: Optional[int] = None,
        zoom_to_fit_font_size_limit_max: Optional[int] = None,
        layout_mode: Optional[str] = None,
        progressive_time: Optional[Numeric] = None,
        progressive_step: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "drawOutOfBound": draw_out_of_bound,
            "ellipsis": {
                "string": ellipsis_string,
                "limitLength": ellipsis_limit_length,
            },
            "zoomToFit": {
                "shrink": is_zoom_to_fit_shrink,
                "enlarge": is_zoom_to_fit_enlarge,
                "fontSizeLimitMin": zoom_to_fit_font_size_limit_min,
                "fontSizeLimitMax": zoom_to_fit_font_size_limit_max,
            },
            "layoutMode": layout_mode,
            "progressiveTime": progressive_time,
            "progressiveStep": progressive_step,
        }


class WordCloudShapeConfigOpts(BasicOpts):
    def __init__(
        self,
        filling_color_list: Optional[Sequence] = None,
        filling_font_family_field: Optional[str] = None,
        filling_font_weight_field: Optional[str] = None,
        filling_font_style_field: Optional[str] = None,
        filling_color_hex_field: Optional[str] = None,
        filling_rotate_angles: Optional[Sequence] = None,
        ratio: Optional[Numeric] = None,
        is_remove_white_border: Optional[bool] = None,
        layout_mode: Optional[str] = None,
        filling_times: Optional[Numeric] = None,
        filling_x_step: Optional[Numeric] = None,
        filling_y_step: Optional[Numeric] = None,
        filling_x_ratio_step: Optional[Numeric] = None,
        filling_y_ratio_step: Optional[Numeric] = None,
        filling_initial_font_size: Optional[Numeric] = None,
        filling_delta_font_size: Optional[Numeric] = None,
        filling_initial_opacity: Optional[Numeric] = None,
        filling_delta_opacity: Optional[Numeric] = None,
        text_layout_times: Optional[Numeric] = None,
        font_size_shrink_factor: Optional[Numeric] = None,
        step_factor: Optional[Numeric] = None,
        important_word_count: Optional[Numeric] = None,
        global_shink_limit: Optional[Numeric] = None,
        font_size_enlarge_factor: Optional[Numeric] = None,
        filling_delta_font_size_factor: Optional[Numeric] = None,
        filling_ratio: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "fillingColorList": filling_color_list,
            "fillingFontFamilyField": filling_font_family_field,
            "fillingFontWeightField": filling_font_weight_field,
            "fillingFontStyleField": filling_font_style_field,
            "fillingColorHexField": filling_color_hex_field,
            "fillingRotateAnglesField": filling_rotate_angles,
            "ratio": ratio,
            "removeWhiteBorder": is_remove_white_border,
            "layoutMode": layout_mode,
            "fillingTimes": filling_times,
            "fillingXStep": filling_x_step,
            "fillingYStep": filling_y_step,
            "fillingXRatioStep": filling_x_ratio_step,
            "fillingYRatioStep": filling_y_ratio_step,
            "fillingInitialFontSize": filling_initial_font_size,
            "fillingDeltaFontSize": filling_delta_font_size,
            "fillingInitialOpacity": filling_initial_opacity,
            "fillingDeltaOpacity": filling_delta_opacity,
            "textLayoutTimes": text_layout_times,
            "fontSizeShrinkFactor": font_size_shrink_factor,
            "stepFactor": step_factor,
            "importantWordCount": important_word_count,
            "globalShinkLimit": global_shink_limit,
            "fontSizeEnlargeFactor": font_size_enlarge_factor,
            "fillingDeltaFontSizeFactor": filling_delta_font_size_factor,
            "fillingRatio": filling_ratio,
        }


class WordCloudOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        padding: Optional[int] = None,
        format_method: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "padding": padding,
            "formatMethod": format_method,
            "style": style,
            "state": state,
        }


class WordCloud3DFillingWordOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        padding: Optional[int] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "padding": padding,
            "style": style,
            "state": state,
        }


class MapLabelOpts(BasicOpts):
    def __init__(
        self,
        series_id: Optional[str] = None,
        is_visible: Optional[bool] = None,
        name_field: Optional[str] = None,
        value_field: Optional[str] = None,
        trigger: Optional[str] = None,
        offset: Optional[int] = 12,
        space: Optional[int] = 10,
        position: Optional[str] = "top",
        is_name_label_visible: Optional[bool] = None,
        name_label_style_opts: Optional[BaseStyleOpts] = None,
        is_value_label_visible: Optional[bool] = None,
        value_label_style_opts: Optional[BaseStyleOpts] = None,
        is_icon_visible: Optional[bool] = None,
        icon_style_opts: Optional[BaseStyleOpts] = None,
        is_background_visible: Optional[bool] = None,
        background_padding_opts: Optional[PaddingOpts] = None,
        background_style_opts: Optional[BaseStyleOpts] = None,
        is_leader_visible: Optional[bool] = None,
        leader_style_opts: Optional[BaseStyleOpts] = None,
    ):
        self.opts: dict = {
            "seriesId": series_id,
            "visible": is_visible,
            "nameField": name_field,
            "valueField": value_field,
            "trigger": trigger,
            "offset": offset,
            "space": space,
            "position": position,
            "nameLabel": {
                "visible": is_name_label_visible,
                "style": name_label_style_opts,
            },
            "valueLabel": {
                "visible": is_value_label_visible,
                "style": value_label_style_opts,
            },
            "icon": {
                "visible": is_icon_visible,
                "style": icon_style_opts,
            },
            "background": {
                "visible": is_background_visible,
                "padding": background_padding_opts,
                "style": background_style_opts,
            },
            "leader": {
                "visible": is_leader_visible,
                "style": leader_style_opts,
            },
        }


class TreeMapLeafOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class TreeMapNonLeafOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class SunburstOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class CirclePackingOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class WaterfallTotalEndOpts(BasicOpts):
    def __init__(
        self,
        text: Optional[str] = None,
    ):
        self.opts: dict = {
            "type": "end",
            "text": text,
        }


class WaterfallTotalCustomOpts(BasicOpts):
    def __init__(
        self,
        tag_field: Optional[str] = None,
        product: Optional[JsCode] = None,
        text: Optional[str] = None,
    ):
        self.opts: dict = {
            "type": "custom",
            "tagField": tag_field,
            "product": product,
            "text": text,
        }


class WaterfallTotalFieldOpts(BasicOpts):
    def __init__(
        self,
        tag_field: Optional[str] = None,
        value_field: Optional[str] = None,
        start_field: Optional[str] = None,
        collect_count_field: Optional[str] = None,
        text: Optional[str] = None,
    ):
        self.opts: dict = {
            "type": "field",
            "tagField": tag_field,
            "valueField": value_field,
            "startField": start_field,
            "collectCountField": collect_count_field,
            "text": text,
        }


class WaterfallLeaderLineOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class GaugePointerOpts(BasicOpts):
    def __init__(
        self,
        type_: Optional[str] = None,
        width: Optional[Numeric] = None,
        height: Optional[Numeric] = None,
        inner_padding: Optional[Numeric] = None,
        outer_padding: Optional[Numeric] = None,
        center: Optional[Sequence[Numeric]] = None,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "type": type_,
            "width": width,
            "height": height,
            "innerPadding": inner_padding,
            "outerPadding": outer_padding,
            "center": center,
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class GaugePinOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class GaugePinBackgroundOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class GaugeSegmentOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class GaugeTrackOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class GaugeOpts(BasicOpts):
    def __init__(
        self,
        series_field: Optional[str] = None,
        series_style: Optional[Sequence] = None,
        is_stack: Optional[bool] = None,
        stack_value: Optional[Union[str, Numeric]] = None,
        is_percent: Optional[bool] = None,
        is_stack_offset_silhouette: Optional[bool] = None,
        invalid_type: Optional[str] = None,
        data_key: Optional[Union[str, Sequence[str], JsCode]] = None,
        # types.CustomMark
        extension_mark_opts: Optional[Sequence[dict]] = None,
        hover_opts: Optional[HoverOpts] = None,
        select_opts: Optional[SelectOpts] = None,
        animation_appear: Optional[AnimationOpts] = None,
        animation_enter: Optional[AnimationOpts] = None,
        animation_update: Optional[AnimationOpts] = None,
        animation_exit: Optional[AnimationOpts] = None,
        animation_disappear: Optional[AnimationOpts] = None,
        animation_state: Optional[AnimationOpts] = None,
        interaction_opts: Optional[Sequence[InteractionOpts]] = None,
        category_field: Optional[Union[str, Sequence[str]]] = None,
        value_field: Optional[Union[str, Sequence[str]]] = None,
        outer_radius: Optional[Numeric] = None,
        inner_radius: Optional[Numeric] = None,
        start_angle: Optional[Numeric] = -90,
        end_angle: Optional[Numeric] = 270,
        center_x: Optional[Union[Numeric, str]] = None,
        center_y: Optional[Union[Numeric, str]] = None,
        corner_radius: Optional[Numeric] = None,
        round_cap: Optional[Union[bool, Sequence[bool]]] = None,
        pad_angle: Optional[Numeric] = None,
        segment_opts: Optional[GaugeSegmentOpts] = None,
        track_opts: Optional[GaugeTrackOpts] = None,
        label_opts: Optional[LabelOpts] = None,
    ):
        self.opts: dict = {
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
            "padAngle": pad_angle,
            "segment": segment_opts,
            "track": track_opts,
            "label": label_opts,
        }


class BoxplotOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class RoseOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class CorrelationCenterPointOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class CorrelationRipplePointOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class CorrelationNodePointOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class LiquidOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class LiquidBackgroundOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class VennCircleOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class VennOverlapOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class PictogramOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class DotOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class DotTitleOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: Optional[bool] = None,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class DotSubTitleOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: Optional[bool] = None,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class DotSymbolOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class DotGridOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class LinkOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }


class ArrowOpts(BasicOpts):
    def __init__(
        self,
        id_: Union[str, int] = None,
        is_interactive: bool = True,
        zindex: Optional[int] = None,
        is_visible: Optional[bool] = None,
        custom_shape: Optional[JsCode] = None,
        state_sort: Optional[JsCode] = None,
        style: Optional[BaseStyleOpts] = None,
        state: Optional[BaseStateOpts] = None,
    ):
        self.opts: dict = {
            "id": id_,
            "interactive": is_interactive,
            "zIndex": zindex,
            "visible": is_visible,
            "customShape": custom_shape,
            "stateSort": state_sort,
            "style": style,
            "state": state,
        }
