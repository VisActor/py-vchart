import unittest

from pyvchart.globals import CurrentConfig
from pyvchart.commons.utils import remove_key_with_none_value
from pyvchart.options.global_options import (
    BaseHtmlOrReactOpts,
    BaseBorderOpts,
    BaseStateOpts,
    BaseStyleOpts,
    BaseSymbolOpts,
    BaseTitleTextStyleOpts,
    ColorOpts,
    IndicatorTitleOpts,
    IndicatorContentOpts,
    IndicatorOpts,
    InitOpts,
    PaddingOpts,
    RegionOpts,
    Render3DOpts,
    RenderOpts,
    TextConfigTextOpts,
    TextConfigImageOpts,
    TitleTextCharacterOpts,
    TitleOpts,
    LabelFilterByGroupOpts,
    LabelOpts,
    LabelRichTextConfigOpts,
    LabelRichStyleOpts,
    LabelStyleOpts,
    LabelSmartInvertOpts,
    LegendTitleOpts,
    LegendBackgroundOpts,
    BaseLegendOpts,
    DiscreteLegendItemOpts,
    DiscreteLegendPagerOpts,
    DiscreteLegendOpts,
    ColorLegendOpts,
    SizeLegendOpts,
    BaseMarkOpts,
    MarkCoordinatesOpts,
    MarkLineOpts,
    MarkAreaOpts,
    MarkPointItemLineOpts,
    MarkPointItemContentOpts,
    MarkPointOpts,
    CrossHairFieldOpts,
    CrossHairOpts,
    AxesTickOpts,
    AxesSubTickOpts,
    AxesGridOpts,
    AxesBackgroundOpts,
    AxesLabelOpts,
    AxesDomainLineOpts,
    BaseAxesOpts,
    AxesBreakOpts,
    AxesLayerOpts,
    AxesLinearOpts,
    AxesBandOpts,
    AxesTimeOpts,
    AxesLogOpts,
    AxesSymlogOpts,
    TooltipStylePanelOpts,
    TooltipStyleOpts,
    TooltipCustomStyleOpts,
    TooltipCustomStylePositionOpts,
    TooltipCustomOpts,
    TooltipOpts,
    LayoutColRowOpts,
    LayoutElementOpts,
    LayoutOpts,
    PlayerSpecOpts,
    PlayerOpts,
    PlayerSliderOpts,
    PlayerControllerPositionOpts,
    PlayerControllerOpts,
    ScrollBarOpts,
    DataZoomOpts,
    BrushOpts,
    ZoomWhenEmptyOpts,
    ScalesOpts,
    BaseCustomMarkOpts,
    CustomMarkSymbolOpts,
    CustomMarkRuleOpts,
    CustomMarkTextOpts,
    CustomMarkRectOpts,
    CustomMarkPathOpts,
    CustomMarkArcOpts,
    CustomMarkPolygonOpts,
    CustomMarkImageOpts,
    CustomMarkGroupOpts,
    ThemeOpts,
    HoverOpts,
    SelectOpts,
    LabelOverlapOpts,
    TooltipStyleShapeOpts,
)


class TestGlobalOptions(unittest.TestCase):

    def test_base_html_or_react_opts(self):
        opts = BaseHtmlOrReactOpts()
        expected = {
            "dom": None,
            "id_": None,
            "pointerEvents": False,
            "container": None,
            "width": None,
            "height": None,
            "style": None,
            "visible": False,
            "anchorType": "boundsLeftTop",
        }
        self.assertEqual(opts.opts, expected)

    def test_base_border_opts(self):
        opts = BaseBorderOpts()
        expected = {
            "stroke": None,
            "strokeOpacity": None,
            "lineDash": None,
            "lineDashOffset": None,
            "lineWidth": None,
            "distance": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_axes_grid_opts(self):
        opts = AxesGridOpts()
        expected = {
            "smooth": None,
            "visible": None,
            "alternateColor": None,
            "alignWithLabel": None,
            "style": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_axes_background_opts(self):
        opts = AxesBackgroundOpts()
        expected = {
            "visible": None,
            "style": None,
            "state": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_padding_opts(self):
        opts = PaddingOpts()
        expected = {
            "left": None,
            "right": None,
            "top": None,
            "bottom": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_cross_hair_opts(self):
        opts = CrossHairOpts()
        expected = {
            "id": None,
            "trigger": "hover",
            "triggerOff": None,
            "lockAfterClick": None,
            "followTooltip": None,
            "labelZIndex": 500,
            "gridZIndex": 100,
            "xField": None,
            "yField": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_axes_break_opts(self):
        opts = AxesBreakOpts()
        expected = {
            "range": None,
            "breakSymbol": {
                "visible": None,
                "gap": None,
                "angle": None,
                "style": None,
            },
        }
        self.assertEqual(opts.opts, expected)

    def test_region_opts(self):
        opts = RegionOpts()
        expected = {
            "id": None,
            "coordinate": "cartesian",
            "width": None,
            "height": None,
            "padding": None,
            "style": None,
            "stackInverse": None,
            "stackSort": None,
            "roam": None,
            "projection": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_zoom_when_empty_opts(self):
        opts = ZoomWhenEmptyOpts()
        expected = {
            "axisId": None,
            "axisIndex": None,
            "axisRangeExpand": None,
            "style": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_scales_opts(self):
        opts = ScalesOpts()
        expected = {
            "id": None,
            "type": None,
            "domain": None,
            "range": None,
            "specified": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_custom_mark_symbol_opts(self):
        opts = CustomMarkSymbolOpts()
        expected = {
            "type": "symbol",
        }
        self.assertEqual(opts.opts, expected)

        base_custom_mark_opts = BaseCustomMarkOpts()
        opts = CustomMarkSymbolOpts(base_custom_mark_opts=base_custom_mark_opts)
        expected = {
            "alignSelf": None,
            "animation": None,
            "animationAppear": None,
            "animationEnter": None,
            "animationExit": None,
            "animationUpdate": None,
            "bottom": None,
            "center": None,
            "clip": None,
            "componentType": None,
            "customShape": None,
            "dataId": None,
            "dataIndex": None,
            "dataKey": None,
            "height": None,
            "id": None,
            "interactive": None,
            "layoutLevel": None,
            "layoutType": None,
            "left": None,
            "maxHeight": None,
            "maxWidth": None,
            "minHeight": None,
            "minWidth": None,
            "offsetX": None,
            "offsetY": None,
            "padding": None,
            "right": None,
            "stateSort": None,
            "style": None,
            "top": None,
            "type": "symbol",
            "visible": None,
            "width": None,
            "zIndex": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_custom_mark_rule_opts(self):
        opts = CustomMarkRuleOpts()
        expected = {
            "type": "rule",
        }
        self.assertEqual(opts.opts, expected)

        base_custom_mark_opts = BaseCustomMarkOpts()
        opts = CustomMarkRuleOpts(base_custom_mark_opts=base_custom_mark_opts)
        expected = {
            "alignSelf": None,
            "animation": None,
            "animationAppear": None,
            "animationEnter": None,
            "animationExit": None,
            "animationUpdate": None,
            "bottom": None,
            "center": None,
            "clip": None,
            "componentType": None,
            "customShape": None,
            "dataId": None,
            "dataIndex": None,
            "dataKey": None,
            "height": None,
            "id": None,
            "interactive": None,
            "layoutLevel": None,
            "layoutType": None,
            "left": None,
            "maxHeight": None,
            "maxWidth": None,
            "minHeight": None,
            "minWidth": None,
            "offsetX": None,
            "offsetY": None,
            "padding": None,
            "right": None,
            "stateSort": None,
            "style": None,
            "top": None,
            "type": "rule",
            "visible": None,
            "width": None,
            "zIndex": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_custom_mark_text_opts(self):
        opts = CustomMarkTextOpts()
        expected = {
            "type": "text",
        }
        self.assertEqual(opts.opts, expected)

        base_custom_mark_opts = BaseCustomMarkOpts()
        opts = CustomMarkTextOpts(base_custom_mark_opts=base_custom_mark_opts)
        expected = {
            "alignSelf": None,
            "animation": None,
            "animationAppear": None,
            "animationEnter": None,
            "animationExit": None,
            "animationUpdate": None,
            "bottom": None,
            "center": None,
            "clip": None,
            "componentType": None,
            "customShape": None,
            "dataId": None,
            "dataIndex": None,
            "dataKey": None,
            "height": None,
            "id": None,
            "interactive": None,
            "layoutLevel": None,
            "layoutType": None,
            "left": None,
            "maxHeight": None,
            "maxWidth": None,
            "minHeight": None,
            "minWidth": None,
            "offsetX": None,
            "offsetY": None,
            "padding": None,
            "right": None,
            "stateSort": None,
            "style": None,
            "top": None,
            "type": "text",
            "visible": None,
            "width": None,
            "zIndex": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_axes_domain_line_opts(self):
        opts = AxesDomainLineOpts()
        expected = {
            "visible": None,
            "style": None,
            "state": None,
            "startSymbol": None,
            "endSymbol": None,
            "onZero": None,
            "onZeroAxisIndex": None,
            "onZeroAxisId": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_player_controller_opts(self):
        opts = PlayerControllerOpts()
        expected = {
            "visible": None,
            "start": None,
            "pause": None,
            "backward": None,
            "forward": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_player_spec_opts(self):
        opts = PlayerSpecOpts()
        expected = {
            "data": {
                "id": None,
                "values": None,
            }
        }
        self.assertEqual(opts.opts, expected)

    def test_init_opts(self):
        opts = InitOpts()
        expected = {
            "width": "900px",
            "height": "500px",
            "is_horizontal_center": False,
            "page_title": CurrentConfig.PAGE_TITLE,
            "bg_color": None,
            "fill_bg": False,
            "js_host": "",
            "is_embed_js": False,
        }
        self.assertEqual(opts.opts, expected)

    def test_axes_tick_opts(self):
        opts = AxesTickOpts()
        expected = {
            "visible": False,
            "tickSize": 4,
            "inside": False,
            "alignWithLabel": True,
            "tickStep": None,
            "tickCount": 5,
            "forceTickCount": None,
            "tickMode": "average",
            "noDecimals": False,
            "dataFilter": None,
            "style": None,
            "state": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_axes_sub_tick_opts(self):
        opts = AxesSubTickOpts()
        expected = {
            "visible": False,
            "tickCount": 4,
            "inside": False,
            "tickSize": 2,
            "style": None,
            "state": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_custom_mark_rect_opts(self):
        opts = CustomMarkRectOpts()
        expected = {
            "type": "rect",
        }
        self.assertEqual(opts.opts, expected)

        base_custom_mark_opts = BaseCustomMarkOpts()
        opts = CustomMarkRectOpts(base_custom_mark_opts=base_custom_mark_opts)
        expected = {
            "alignSelf": None,
            "animation": None,
            "animationAppear": None,
            "animationEnter": None,
            "animationExit": None,
            "animationUpdate": None,
            "bottom": None,
            "center": None,
            "clip": None,
            "componentType": None,
            "customShape": None,
            "dataId": None,
            "dataIndex": None,
            "dataKey": None,
            "height": None,
            "id": None,
            "interactive": None,
            "layoutLevel": None,
            "layoutType": None,
            "left": None,
            "maxHeight": None,
            "maxWidth": None,
            "minHeight": None,
            "minWidth": None,
            "offsetX": None,
            "offsetY": None,
            "padding": None,
            "right": None,
            "stateSort": None,
            "style": None,
            "top": None,
            "type": "rect",
            "visible": None,
            "width": None,
            "zIndex": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_custom_mark_path_opts(self):
        opts = CustomMarkPathOpts()
        expected = {
            "type": "path",
        }
        self.assertEqual(opts.opts, expected)

        base_custom_mark_opts = BaseCustomMarkOpts()
        opts = CustomMarkPathOpts(base_custom_mark_opts=base_custom_mark_opts)
        expected = {
            "alignSelf": None,
            "animation": None,
            "animationAppear": None,
            "animationEnter": None,
            "animationExit": None,
            "animationUpdate": None,
            "bottom": None,
            "center": None,
            "clip": None,
            "componentType": None,
            "customShape": None,
            "dataId": None,
            "dataIndex": None,
            "dataKey": None,
            "height": None,
            "id": None,
            "interactive": None,
            "layoutLevel": None,
            "layoutType": None,
            "left": None,
            "maxHeight": None,
            "maxWidth": None,
            "minHeight": None,
            "minWidth": None,
            "offsetX": None,
            "offsetY": None,
            "padding": None,
            "right": None,
            "stateSort": None,
            "style": None,
            "top": None,
            "type": "path",
            "visible": None,
            "width": None,
            "zIndex": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_custom_mark_arc_opts(self):
        opts = CustomMarkArcOpts()
        expected = {
            "type": "arc",
        }
        self.assertEqual(opts.opts, expected)

        base_custom_mark_opts = BaseCustomMarkOpts()
        opts = CustomMarkArcOpts(base_custom_mark_opts=base_custom_mark_opts)
        expected = {
            "alignSelf": None,
            "animation": None,
            "animationAppear": None,
            "animationEnter": None,
            "animationExit": None,
            "animationUpdate": None,
            "bottom": None,
            "center": None,
            "clip": None,
            "componentType": None,
            "customShape": None,
            "dataId": None,
            "dataIndex": None,
            "dataKey": None,
            "height": None,
            "id": None,
            "interactive": None,
            "layoutLevel": None,
            "layoutType": None,
            "left": None,
            "maxHeight": None,
            "maxWidth": None,
            "minHeight": None,
            "minWidth": None,
            "offsetX": None,
            "offsetY": None,
            "padding": None,
            "right": None,
            "stateSort": None,
            "style": None,
            "top": None,
            "type": "arc",
            "visible": None,
            "width": None,
            "zIndex": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_custom_mark_polygon_opts(self):
        opts = CustomMarkPolygonOpts()
        expected = {
            "type": "polygon",
        }
        self.assertEqual(opts.opts, expected)

        base_custom_mark_opts = BaseCustomMarkOpts()
        opts = CustomMarkPolygonOpts(base_custom_mark_opts=base_custom_mark_opts)
        expected = {
            "alignSelf": None,
            "animation": None,
            "animationAppear": None,
            "animationEnter": None,
            "animationExit": None,
            "animationUpdate": None,
            "bottom": None,
            "center": None,
            "clip": None,
            "componentType": None,
            "customShape": None,
            "dataId": None,
            "dataIndex": None,
            "dataKey": None,
            "height": None,
            "id": None,
            "interactive": None,
            "layoutLevel": None,
            "layoutType": None,
            "left": None,
            "maxHeight": None,
            "maxWidth": None,
            "minHeight": None,
            "minWidth": None,
            "offsetX": None,
            "offsetY": None,
            "padding": None,
            "right": None,
            "stateSort": None,
            "style": None,
            "top": None,
            "type": "polygon",
            "visible": None,
            "width": None,
            "zIndex": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_custom_mark_image_opts(self):
        opts = CustomMarkImageOpts()
        expected = {
            "type": "image",
        }
        self.assertEqual(opts.opts, expected)

        base_custom_mark_opts = BaseCustomMarkOpts()
        opts = CustomMarkImageOpts(base_custom_mark_opts=base_custom_mark_opts)
        expected = {
            "alignSelf": None,
            "animation": None,
            "animationAppear": None,
            "animationEnter": None,
            "animationExit": None,
            "animationUpdate": None,
            "bottom": None,
            "center": None,
            "clip": None,
            "componentType": None,
            "customShape": None,
            "dataId": None,
            "dataIndex": None,
            "dataKey": None,
            "height": None,
            "id": None,
            "interactive": None,
            "layoutLevel": None,
            "layoutType": None,
            "left": None,
            "maxHeight": None,
            "maxWidth": None,
            "minHeight": None,
            "minWidth": None,
            "offsetX": None,
            "offsetY": None,
            "padding": None,
            "right": None,
            "stateSort": None,
            "style": None,
            "top": None,
            "type": "image",
            "visible": None,
            "width": None,
            "zIndex": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_custom_mark_group_opts(self):
        opts = CustomMarkGroupOpts()
        expected = {
            "type": "group",
            "children": None,
        }
        self.assertEqual(opts.opts, expected)

        base_custom_mark_opts = BaseCustomMarkOpts()
        opts = CustomMarkGroupOpts(base_custom_mark_opts=base_custom_mark_opts)
        expected = {
            "alignSelf": None,
            "animation": None,
            "animationAppear": None,
            "animationEnter": None,
            "animationExit": None,
            "animationUpdate": None,
            "bottom": None,
            "center": None,
            "clip": None,
            "componentType": None,
            "customShape": None,
            "dataId": None,
            "dataIndex": None,
            "dataKey": None,
            "height": None,
            "id": None,
            "interactive": None,
            "layoutLevel": None,
            "layoutType": None,
            "left": None,
            "maxHeight": None,
            "maxWidth": None,
            "minHeight": None,
            "minWidth": None,
            "offsetX": None,
            "offsetY": None,
            "padding": None,
            "right": None,
            "stateSort": None,
            "style": None,
            "top": None,
            "type": "group",
            "children": None,
            "visible": None,
            "width": None,
            "zIndex": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_layout_col_row_opts(self):
        opts = LayoutColRowOpts()
        expected = {
            "index": None,
            "size": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_layout_element_opts(self):
        opts = LayoutElementOpts()
        expected = {
            "id": None,
            "col": None,
            "row": None,
            "colSpan": 1,
            "rowSpan": 1,
        }
        self.assertEqual(opts.opts, expected)

    def test_axes_symlog_opts(self):
        opts = AxesSymlogOpts()
        expected = {
            "type": "symlog",
            "constant": 10,
        }
        self.assertEqual(opts.opts, expected)

        base_axes_opts = BaseAxesOpts()
        opts = AxesSymlogOpts(base_axes_opts=base_axes_opts)
        expected = {
            "alignSelf": None,
            "animation": None,
            "animationAppear": None,
            "animationEnter": None,
            "animationExit": None,
            "animationUpdate": None,
            "autoIndent": None,
            "background": None,
            "bottom": None,
            "center": None,
            "clip": None,
            "constant": 10,
            "depth": None,
            "domainLine": None,
            "grid": None,
            "height": None,
            "hover": None,
            "id": None,
            "innerOffset": None,
            "inverse": None,
            "label": None,
            "layoutLevel": None,
            "layoutType": None,
            "left": None,
            "maxHeight": None,
            "maxWidth": None,
            "minHeight": None,
            "minWidth": None,
            "mode": None,
            "offsetX": None,
            "offsetY": None,
            "orient": None,
            "padding": None,
            "regionId": None,
            "regionIndex": None,
            "right": None,
            "sampling": None,
            "select": None,
            "seriesId": None,
            "seriesIndex": None,
            "subGrid": None,
            "subTick": None,
            "tick": None,
            "title": None,
            "top": None,
            "type": "symlog",
            "unit": {"style": None, "text": None, "visible": None},
            "visible": None,
            "width": None,
            "zIndex": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_title_opts(self):
        opts = TitleOpts()
        expected = {
            "visible": True,
            "text": None,
            "textType": None,
            "subText": None,
            "subTextType": None,
            "orient": "top",
            "minWidth": None,
            "maxWidth": None,
            "minHeight": None,
            "maxHeight": None,
            "innerPadding": 0,
            "align": "left",
            "verticalAlign": "top",
            "textStyle": None,
            "subTextStyle": None,
            "layoutType": "normal",
            "layoutLevel": 50,
            "alignSelf": "start",
            "padding": None,
            "width": None,
            "height": None,
            "offsetX": None,
            "offsetY": None,
            "zIndex": 500,
            "clip": None,
            "left": None,
            "right": None,
            "top": None,
            "bottom": None,
            "center": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_theme_opts(self):
        opts = ThemeOpts()
        expected = {
            "name": None,
            "background": None,
            "padding": None,
            "fontFamily": None,
            "colorScheme": None,
            "series": None,
            "component": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_hover_opts(self):
        opts = HoverOpts()
        expected = {
            "enable": None,
            "trigger": None,
            "triggerOff": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_mark_area_opts(self):
        opts = MarkAreaOpts()
        expected = {
            "x": None,
            "y": None,
            "x1": None,
            "y1": None,
            "angle": None,
            "radius": None,
            "angle1": None,
            "radius1": None,
            "coordinates": None,
            "coordinatesOffset": None,
            "positions": None,
            "regionRelative": False,
            "startRelativeSeriesIndex": None,
            "startRelativeSeriesId": None,
            "endRelativeSeriesIndex": None,
            "endRelativeSeriesId": None,
            "relativeRelativeSeriesIndex": None,
            "relativeRelativeSeriesId": None,
            "specifiedDataSeriesIndex": None,
            "specifiedDataSeriesId": None,
            "area": {
                "state": None,
                "style": None,
            },
            "label": None,
            "animation": None,
            "animationEnter": None,
            "animationUpdate": None,
            "animationExit": None,
        }
        self.assertEqual(opts.opts, expected)

        base_mark_opts = BaseMarkOpts(is_visible=True)
        opts = MarkAreaOpts(base_mark_opts=base_mark_opts)
        expected = {
            "alignSelf": "start",
            "angle": None,
            "angle1": None,
            "animation": None,
            "animationEnter": None,
            "animationExit": None,
            "animationUpdate": None,
            "area": {"state": None, "style": None},
            "autoRange": None,
            "bottom": None,
            "center": None,
            "clip": None,
            "coordinates": None,
            "coordinatesOffset": None,
            "coordinationType": None,
            "endRelativeSeriesId": None,
            "endRelativeSeriesIndex": None,
            "height": None,
            "id": None,
            "interactive": True,
            "label": None,
            "layoutLevel": None,
            "layoutType": None,
            "left": None,
            "maxHeight": None,
            "maxWidth": None,
            "minHeight": None,
            "minWidth": None,
            "name": None,
            "offsetX": None,
            "offsetY": None,
            "padding": None,
            "positions": None,
            "radius": None,
            "radius1": None,
            "regionRelative": False,
            "relativeRelativeSeriesId": None,
            "relativeRelativeSeriesIndex": None,
            "relativeSeriesId": None,
            "relativeSeriesIndex": None,
            "right": None,
            "specifiedDataSeriesId": None,
            "specifiedDataSeriesIndex": None,
            "startRelativeSeriesId": None,
            "startRelativeSeriesIndex": None,
            "top": None,
            "visible": True,
            "width": None,
            "x": None,
            "x1": None,
            "y": None,
            "y1": None,
            "zIndex": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_base_symbol_opts(self):
        opts = BaseSymbolOpts()
        expected = {
            "visible": None,
            "symbolType": None,
            "size": None,
            "refX": None,
            "refY": None,
            "refAngle": None,
            "clip": None,
            "style": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_mark_coordinates_opts(self):
        opts = MarkCoordinatesOpts()
        expected = {
            "refRelativeSeriesIndex": None,
            "refRelativeSeriesId": None,
            "xFieldIndex": None,
            "xFieldDim": None,
            "yFieldIndex": None,
            "yFieldDim": None,
            "angleFieldIndex": None,
            "angleFieldDim": None,
            "radiusFieldIndex": None,
            "radiusFieldDim": None,
        }
        self.assertEqual(opts.opts, expected)

        opts = MarkCoordinatesOpts(key_field="x", value_field="100")
        expected = {
            "refRelativeSeriesIndex": None,
            "refRelativeSeriesId": None,
            "xFieldIndex": None,
            "xFieldDim": None,
            "yFieldIndex": None,
            "yFieldDim": None,
            "angleFieldIndex": None,
            "angleFieldDim": None,
            "radiusFieldIndex": None,
            "radiusFieldDim": None,
            "x": "100",
        }
        self.assertEqual(opts.opts, expected)

    def test_tooltip_style_opts(self):
        opts = TooltipStyleOpts()
        expected = {
            "panel": None,
            "shape": None,
            "titleLabel": None,
            "keyLabel": None,
            "valueLabel": None,
            "spaceRow": None,
            "maxContentHeight": None,
            "align": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_base_axes_opts(self):
        opts = BaseAxesOpts()
        expected = {
            "id": None,
            "visible": None,
            "mode": None,
            "depth": None,
            "sampling": None,
            "orient": None,
            "inverse": None,
            "hover": None,
            "select": None,
            "autoIndent": None,
            "domainLine": None,
            "label": None,
            "title": None,
            "background": None,
            "grid": None,
            "subGrid": None,
            "unit": {
                "visible": None,
                "text": None,
                "style": None,
            },
            "innerOffset": None,
            "tick": None,
            "subTick": None,
            "animation": None,
            "animationAppear": None,
            "animationEnter": None,
            "animationUpdate": None,
            "animationExit": None,
            "regionIndex": None,
            "regionId": None,
            "seriesIndex": None,
            "seriesId": None,
            "layoutType": None,
            "layoutLevel": None,
            "alignSelf": None,
            "padding": None,
            "width": None,
            "minWidth": None,
            "maxWidth": None,
            "height": None,
            "minHeight": None,
            "maxHeight": None,
            "offsetX": None,
            "offsetY": None,
            "zIndex": None,
            "clip": None,
            "left": None,
            "right": None,
            "top": None,
            "bottom": None,
            "center": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_size_legend_opts(self):
        opts = SizeLegendOpts()
        expected = {
            "type": "size",
            "slidable": True,
            "inverse": True,
            "rail": {
                "width": None,
                "height": None,
                "style": None,
            },
            "handle": {
                "visible": True,
                "style": None,
            },
            "track": {
                "style": None,
            },
            "startText": {
                "visible": False,
                "text": None,
                "space": 6,
                "style": None,
            },
            "endText": {
                "visible": False,
                "text": None,
                "space": 6,
                "style": None,
            },
            "handleText": {
                "visible": False,
                "precision": None,
                "formatter": None,
                "space": 6,
                "style": None,
            },
            "sizeBackground": None,
        }
        self.assertEqual(opts.opts, expected)

        base_legend_opts = BaseLegendOpts(is_visible=True)
        opts = SizeLegendOpts(base_legend_opts=base_legend_opts)
        expected = {
            "alignSelf": "start",
            "background": None,
            "bottom": None,
            "center": None,
            "clip": None,
            "customFilter": None,
            "defaultSelected": None,
            "endText": {"space": 6, "style": None, "text": None, "visible": False},
            "field": None,
            "filter": True,
            "handle": {"style": None, "visible": True},
            "handleText": {
                "formatter": None,
                "precision": None,
                "space": 6,
                "style": None,
                "visible": False,
            },
            "height": None,
            "interactive": True,
            "inverse": True,
            "layout": None,
            "layoutLevel": 50,
            "layoutType": "normal",
            "left": None,
            "maxCol": None,
            "maxHeight": None,
            "maxRow": None,
            "maxWidth": None,
            "minHeight": None,
            "minWidth": None,
            "offsetX": None,
            "offsetY": None,
            "orient": None,
            "padding": None,
            "position": "middle",
            "rail": {"height": None, "style": None, "width": None},
            "regionId": None,
            "regionIndex": None,
            "reversed": None,
            "right": None,
            "scale": None,
            "seriesId": None,
            "seriesIndex": None,
            "sizeBackground": None,
            "slidable": True,
            "startText": {"space": 6, "style": None, "text": None, "visible": False},
            "title": None,
            "top": None,
            "track": {"style": None},
            "type": "size",
            "visible": True,
            "width": None,
            "zIndex": 500,
        }
        self.assertEqual(opts.opts, expected)

    def test_color_legend_opts(self):
        opts = ColorLegendOpts()
        expected = {
            "type": "color",
            "slidable": True,
            "inverse": True,
            "rail": {
                "width": None,
                "height": None,
                "style": None,
            },
            "handle": {
                "visible": True,
                "style": None,
            },
            "track": {
                "style": None,
            },
            "startText": {
                "visible": False,
                "text": None,
                "space": 6,
                "style": None,
            },
            "endText": {
                "visible": False,
                "text": None,
                "space": 6,
                "style": None,
            },
            "handleText": {
                "visible": False,
                "precision": None,
                "formatter": None,
                "space": 6,
                "style": None,
            },
        }
        self.assertEqual(opts.opts, expected)

    def test_player_opts(self):
        opts = PlayerOpts()
        expected = {
            "specs": None,
            "type": None,
            "interval": 1000,
            "totalDuration": None,
            "direction": "default",
            "auto": None,
            "loop": None,
            "alternate": None,
            "visible": None,
            "dx": None,
            "dy": None,
            "width": None,
            "height": None,
            "position": None,
            "orient": None,
            "slider": None,
            "controller": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_brush_opts(self):
        opts = BrushOpts()
        expected = {
            "visible": None,
            "regionIndex": None,
            "regionId": None,
            "seriesIndex": None,
            "seriesId": None,
            "brushLinkSeriesIndex": None,
            "brushLinkSeriesId": None,
            "inBrush": None,
            "outOfBrush": None,
            "brushMode": None,
            "brushType": None,
            "brushMoved": None,
            "removeOnClick": None,
            "delayType": None,
            "delayTime": None,
            "sizeThreshold": None,
            "zoomAfterBrush": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_mark_line_opts(self):
        opts = MarkLineOpts()
        expected = {
            "type": "type-step",
            "connectDirection": None,
            "expandDistance": None,
            "x": None,
            "y": None,
            "x1": None,
            "y1": None,
            "angle": None,
            "radius": None,
            "angle1": None,
            "radius1": None,
            "coordinates": None,
            "coordinatesOffset": None,
            "positions": None,
            "regionRelative": False,
            "startRelativeSeriesIndex": None,
            "startRelativeSeriesId": None,
            "endRelativeSeriesIndex": None,
            "endRelativeSeriesId": None,
            "relativeRelativeSeriesIndex": None,
            "relativeRelativeSeriesId": None,
            "specifiedDataSeriesIndex": None,
            "specifiedDataSeriesId": None,
            "line": {
                "multiSegment": False,
                "mainSegmentIndex": None,
                "state": None,
                "style": None,
            },
            "label": None,
            "startSymbol": None,
            "endSymbol": None,
            "animation": None,
            "animationEnter": None,
            "animationUpdate": None,
            "animationExit": None,
        }
        self.assertEqual(opts.opts, expected)

        base_mark_opts = BaseMarkOpts(is_visible=True)
        opts = MarkLineOpts(base_mark_opts=base_mark_opts)
        expected = {
            "alignSelf": "start",
            "angle": None,
            "angle1": None,
            "animation": None,
            "animationEnter": None,
            "animationExit": None,
            "animationUpdate": None,
            "autoRange": None,
            "bottom": None,
            "center": None,
            "clip": None,
            "connectDirection": None,
            "coordinates": None,
            "coordinatesOffset": None,
            "coordinationType": None,
            "endRelativeSeriesId": None,
            "endRelativeSeriesIndex": None,
            "endSymbol": None,
            "expandDistance": None,
            "height": None,
            "id": None,
            "interactive": True,
            "label": None,
            "layoutLevel": None,
            "layoutType": None,
            "left": None,
            "line": {
                "mainSegmentIndex": None,
                "multiSegment": False,
                "state": None,
                "style": None,
            },
            "maxHeight": None,
            "maxWidth": None,
            "minHeight": None,
            "minWidth": None,
            "name": None,
            "offsetX": None,
            "offsetY": None,
            "padding": None,
            "positions": None,
            "radius": None,
            "radius1": None,
            "regionRelative": False,
            "relativeRelativeSeriesId": None,
            "relativeRelativeSeriesIndex": None,
            "relativeSeriesId": None,
            "relativeSeriesIndex": None,
            "right": None,
            "specifiedDataSeriesId": None,
            "specifiedDataSeriesIndex": None,
            "startRelativeSeriesId": None,
            "startRelativeSeriesIndex": None,
            "startSymbol": None,
            "top": None,
            "type": "type-step",
            "visible": True,
            "width": None,
            "x": None,
            "x1": None,
            "y": None,
            "y1": None,
            "zIndex": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_base_state_opts(self):
        opts = BaseStateOpts()
        expected = {
            "active": None,
            "hover": None,
            "hover_reverse": None,
            "selected": None,
            "selected_reverse": None,
            "unselected": None,
            "selectedHover": None,
            "unSelectedHover": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_base_style_opts(self):
        opts = BaseStyleOpts()
        expected = {
            "cornerRadius": None,
            "length": None,
            "width": None,
            "height": None,
            "fontSize": None,
            "fill": None,
            "fillOpacity": None,
            "shadowBlur": None,
            "shadowColor": None,
            "shadowOffsetX": None,
            "shadowOffsetY": None,
            "background": None,
            "stroke": None,
            "strokeOpacity": None,
            "lineDash": None,
            "lineDashOffset": None,
            "lineWidth": None,
            "lineCap": None,
            "lineJoin": None,
            "miterLimit": None,
            "outerBorder": None,
            "innerBorder": None,
            "innerPadding": None,
            "outerPadding": None,
            "opacity": None,
            "cursor": None,
            "text": None,
            "texture": None,
            "textureColor": None,
            "textureSize": None,
            "texturePadding": None,
            "isPickable": None,
            "isChildrenPickable": None,
            "keepDirIn3d": None,
            "zIndex": None,
            "visible": None,
            "dx": None,
            "dy": None,
            "angle": None,
            "scaleX": None,
            "scaleY": None,
            "scaleCenter": None,
            "pickStrokeBuffer": None,
            "boundsPadding": None,
            "html": None,
            "react": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_base_title_text_style_opts(self):
        opts = BaseTitleTextStyleOpts()
        expected = {
            "type": None,
            "text": None,
            "fontSize": None,
            "fontFamily": None,
            "fontWeight": None,
            "fontStyle": "normal",
            "fontVariant": None,
            "lineHeight": None,
            "textAlign": None,
            "textBaseline": None,
            "maxLineWidth": None,
            "ellipsis": "...",
            "suffixPosition": "end",
            "underline": None,
            "lineThrough": None,
            "direction": "horizontal",
            "wordBreak": "break-word",
            "keepDirIn3D": None,
            "align": None,
            "verticalAlign": None,
            "heightLimit": None,
            "lineClamp": None,
            "character": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_color_opts(self):
        opts = ColorOpts()
        expected = {
            "type": None,
            "domain": None,
            "range": None,
            "specified": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_indicator_title_opts(self):
        opts = IndicatorTitleOpts()
        expected = {
            "visible": None,
            "field": None,
            "space": None,
            "autoLimit": None,
            "autoFit": None,
            "fitPercent": None,
            "fitStrategy": None,
            "formatMethod": None,
            "style": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_indicator_content_opts(self):
        opts = IndicatorContentOpts()
        expected = {
            "visible": None,
            "field": None,
            "space": None,
            "autoLimit": None,
            "autoFit": None,
            "fitPercent": None,
            "fitStrategy": None,
            "formatMethod": None,
            "style": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_indicator_opts(self):
        opts = IndicatorOpts()
        expected = {
            "visible": None,
            "fixed": None,
            "trigger": None,
            "offsetX": None,
            "offsetY": None,
            "limitRatio": None,
            "title": None,
            "content": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_render_opts(self):
        opts = RenderOpts()
        expected = {
            "afterRender": None,
            "animation": None,
            "autoFit": None,
            "autoRefreshDpr": None,
            "background": None,
            "beforeRender": None,
            "canvasControled": None,
            "disableDirtyBounds": None,
            "disableTriggerEvent": None,
            "dom": None,
            "dpr": None,
            "enableHtmlAttributes": None,
            "enableView3dTransform": None,
            "interactive": None,
            "layout": None,
            "logLevel": None,
            "mode": None,
            "modeParams": None,
            "options3d": None,
            "popTip": None,
            "renderCanvas": None,
            "resizeDelay": None,
            "supportsPointerEvents": None,
            "supportsTouchEvents": None,
            "theme": None,
            "viewBox": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_render_3d_opts(self):
        opts = Render3DOpts()
        expected = {
            "enable": None,
            "enableView3dTransform": None,
            "center": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_text_config_text_opts(self):
        opts = TextConfigTextOpts()
        expected = {
            "text": None,
            "fill": None,
            "stroke": None,
            "lineWidth": None,
            "fillOpacity": None,
            "strokeOpacity": None,
            "fontSize": None,
            "fontFamily": None,
            "fontWeight": None,
            "fontStyle": "normal",
            "underline": None,
            "lineThrough": None,
            "textDecoration": None,
            "script": None,
            "direction": None,
            "lineHeight": None,
            "textAlign": None,
            "textBaseline": None,
            "opacity": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_text_config_image_opts(self):
        opts = TextConfigImageOpts()
        expected = {
            "image": None,
            "width": None,
            "height": None,
            "margin": None,
            "backgroundShowMode": None,
            "backgroundFill": None,
            "backgroundFillOpacity": None,
            "backgroundStroke": None,
            "backgroundStrokeOpacity": None,
            "backgroundRadius": None,
            "backgroundWidth": None,
            "backgroundHeight": None,
            "hoverImage": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_label_filter_by_group_opts(self):
        opts = LabelFilterByGroupOpts()
        expected = {
            "field": None,
            "type": None,
            "filter": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_label_opts(self):
        opts = LabelOpts()
        expected = {
            "position": None,
            "filterByGroup": None,
            "visible": None,
            "interactive": None,
            "formatMethod": None,
            "formatter": None,
            "syncState": None,
            "offset": None,
            "style": None,
            "state": None,
            "overlap": None,
            "smartInvert": None,
            "dataFilter": None,
            "customLayoutFunc": None,
            "customOverlapFunc": None,
            "animation": None,
            "stackDataFilterType": None,
            "valueType": None,
            "support3d": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_label_rich_style_opts(self):
        opts = LabelRichStyleOpts()
        expected = {
            "width": None,
            "height": None,
            "maxHeight": None,
            "maxWidth": None,
            "ellipsis": False,
            "wordBreak": "break-word",
            "verticalDirection": None,
            "textAlign": None,
            "textBaseline": None,
            "layoutDirection": "horizontal",
            "singleLine": False,
            "textConfig": None,
            "fontSize": None,
            "fontFamily": None,
            "fontWeight": None,
            "fontStyle": "normal",
            "fill": None,
            "stroke": None,
            "lineWidth": None,
            "fillOpacity": None,
            "strokeOpacity": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_label_smart_invert_opts(self):
        opts = LabelSmartInvertOpts()
        expected = {
            "mode": None,
            "textStyle": None,
            "contrastRatiosThreshold": None,
            "alternativeColors": None,
            "fillStrategy": None,
            "strokeStrategy": None,
            "brightColor": None,
            "outsideEnable": None,
            "interactInvertType": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_legend_title_opts(self):
        opts = LegendTitleOpts()
        expected = {
            "visible": False,
            "text": None,
            "align": "start",
            "space": None,
            "padding": None,
            "textStyle": None,
            "shape": {
                "visible": False,
                "space": None,
                "style": None,
            },
            "background": {
                "visible": False,
                "style": None,
            },
            "minWidth": None,
            "maxWidth": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_legend_background_opts(self):
        opts = LegendBackgroundOpts()
        expected = {
            "visible": False,
            "padding": None,
            "style": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_base_legend_opts(self):
        opts = BaseLegendOpts()
        expected = {
            "visible": True,
            "orient": None,
            "position": "middle",
            "layout": None,
            "interactive": True,
            "filter": True,
            "customFilter": None,
            "title": None,
            "background": None,
            "defaultSelected": None,
            "scale": None,
            "field": None,
            "reversed": None,
            "maxWidth": None,
            "maxCol": None,
            "maxHeight": None,
            "maxRow": None,
            "regionIndex": None,
            "regionId": None,
            "seriesIndex": None,
            "seriesId": None,
            "layoutType": "normal",
            "layoutLevel": 50,
            "alignSelf": "start",
            "padding": None,
            "width": None,
            "minWidth": None,
            "height": None,
            "minHeight": None,
            "offsetX": None,
            "offsetY": None,
            "zIndex": 500,
            "clip": None,
            "left": None,
            "right": None,
            "top": None,
            "bottom": None,
            "center": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_discrete_legend_item_opts(self):
        opts = DiscreteLegendItemOpts()
        expected = {
            "visible": True,
            "spaceCol": None,
            "spaceRow": None,
            "maxWidth": None,
            "width": None,
            "height": None,
            "padding": None,
            "align": "left",
            "autoEllipsisStrategy": "none",
            "background": {
                "visible": False,
                "style": None,
                "state": None,
            },
            "shape": {
                "visible": False,
                "space": None,
                "style": None,
                "state": None,
            },
            "label": {
                "space": None,
                "widthRatio": None,
                "formatMethod": None,
                "style": None,
                "state": None,
            },
            "value": {
                "space": None,
                "alignRight": False,
                "widthRatio": None,
                "formatMethod": None,
                "formatter": None,
                "style": None,
                "state": None,
            },
            "focus": False,
            "focusIconStyle": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_discrete_legend_pager_opts(self):
        opts = DiscreteLegendPagerOpts()
        expected = {
            "type": None,
            "layout": None,
            "defaultCurrent": None,
            "padding": None,
            "space": None,
            "animation": True,
            "animationDuration": 450,
            "animationEasing": "quadIn",
            "textStyle": None,
            "handle": {
                "space": 8,
                "preShape": None,
                "nextShape": None,
                "style": None,
                "state": {
                    "hover": None,
                    "disabled": None,
                },
            },
            "railStyle": None,
            "sliderStyle": None,
            "scrollByPosition": None,
            "scrollMask": {
                "visible": False,
                "gradientLength": 16,
                "gradientStops": None,
            },
        }
        self.assertEqual(opts.opts, expected)

    def test_discrete_legend_opts(self):
        opts = DiscreteLegendOpts()
        expected = {
            "type": "discrete",
            "select": True,
            "selectMode": "multiple",
            "scaleName": None,
            "hover": True,
            "allowAllCanceled": None,
            "item": None,
            "autoPage": True,
            "pager": None,
            "data": None,
        }
        self.assertEqual(opts.opts, expected)

        base_opts = BaseLegendOpts(is_visible=True)
        opts = DiscreteLegendOpts(base_legend_opts=base_opts)
        expected = {
            "alignSelf": "start",
            "allowAllCanceled": None,
            "autoPage": True,
            "background": None,
            "bottom": None,
            "center": None,
            "clip": None,
            "customFilter": None,
            "data": None,
            "defaultSelected": None,
            "field": None,
            "filter": True,
            "height": None,
            "hover": True,
            "interactive": True,
            "item": None,
            "layout": None,
            "layoutLevel": 50,
            "layoutType": "normal",
            "left": None,
            "maxCol": None,
            "maxHeight": None,
            "maxRow": None,
            "maxWidth": None,
            "minHeight": None,
            "minWidth": None,
            "offsetX": None,
            "offsetY": None,
            "orient": None,
            "padding": None,
            "pager": None,
            "position": "middle",
            "regionId": None,
            "regionIndex": None,
            "reversed": None,
            "right": None,
            "scale": None,
            "scaleName": None,
            "select": True,
            "selectMode": "multiple",
            "seriesId": None,
            "seriesIndex": None,
            "title": None,
            "top": None,
            "type": "discrete",
            "visible": True,
            "width": None,
            "zIndex": 500,
        }
        self.assertEqual(opts.opts, expected)

    def test_mark_point_item_content_opts(self):
        opts = MarkPointItemContentOpts()
        expected = {
            "type": None,
            "position": None,
            "offsetX": None,
            "offsetY": None,
            "refX": None,
            "refY": None,
            "refAngle": None,
            "confine": None,
            "symbol": {
                "state": None,
                "style": None,
            },
            "image": {
                "state": None,
                "style": None,
            },
            "text": {
                "state": None,
                "style": None,
            },
            "richText": {
                "state": None,
                "style": None,
            },
        }
        self.assertEqual(opts.opts, expected)

    def test_mark_point_opts(self):
        opts = MarkPointOpts()
        expected = {
            "x": None,
            "y": None,
            "angle": None,
            "radius": None,
            "areaName": None,
            "coordinate": None,
            "coordinatesOffset": None,
            "position": None,
            "regionRelative": False,
            "relativeRelativeSeriesIndex": None,
            "relativeRelativeSeriesId": None,
            "itemLine": None,
            "itemContent": None,
            "animation": None,
            "animationEnter": None,
            "animationUpdate": None,
            "animationExit": None,
            "targetSymbol": {
                "offset": None,
                "visible": False,
                "size": None,
                "style": None,
            },
        }
        self.assertEqual(opts.opts, expected)

        base_mark_opts = BaseMarkOpts()
        opts = MarkPointOpts(base_mark_opts=base_mark_opts)
        expected = {
            "alignSelf": "start",
            "angle": None,
            "animation": None,
            "animationEnter": None,
            "animationExit": None,
            "animationUpdate": None,
            "areaName": None,
            "autoRange": None,
            "bottom": None,
            "center": None,
            "clip": None,
            "coordinate": None,
            "coordinatesOffset": None,
            "coordinationType": None,
            "height": None,
            "id": None,
            "interactive": True,
            "itemContent": None,
            "itemLine": None,
            "layoutLevel": None,
            "layoutType": None,
            "left": None,
            "maxHeight": None,
            "maxWidth": None,
            "minHeight": None,
            "minWidth": None,
            "name": None,
            "offsetX": None,
            "offsetY": None,
            "padding": None,
            "position": None,
            "radius": None,
            "regionRelative": False,
            "relativeRelativeSeriesId": None,
            "relativeRelativeSeriesIndex": None,
            "relativeSeriesId": None,
            "relativeSeriesIndex": None,
            "right": None,
            "targetSymbol": {
                "offset": None,
                "size": None,
                "style": None,
                "visible": False,
            },
            "top": None,
            "visible": True,
            "width": None,
            "x": None,
            "y": None,
            "zIndex": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_cross_hair_field_opts(self):
        opts = CrossHairFieldOpts()
        expected = {
            "visible": False,
            "line": {
                "visible": None,
                "type": None,
                "width": None,
                "style": None,
            },
            "label": {
                "visible": None,
                "formatMethod": None,
                "formatter": None,
                "style": None,
                "labelBackground": {
                    "visible": None,
                    "padding": None,
                    "minWidth": 30,
                    "maxWidth": None,
                    "style": None,
                },
            },
            "bindingAxesIndex": None,
            "defaultSelect": {
                "axisIndex": None,
                "datum": None,
            },
        }
        self.assertEqual(opts.opts, expected)

    def test_base_mark_opts(self):
        opts = BaseMarkOpts()
        expected = {
            "relativeSeriesIndex": None,
            "relativeSeriesId": None,
            "visible": True,
            "clip": None,
            "interactive": True,
            "autoRange": None,
            "id": None,
            "name": None,
            "coordinationType": None,
            "layoutType": None,
            "layoutLevel": None,
            "alignSelf": "start",
            "padding": None,
            "width": None,
            "minWidth": None,
            "maxWidth": None,
            "height": None,
            "minHeight": None,
            "maxHeight": None,
            "offsetX": None,
            "offsetY": None,
            "zIndex": None,
            "left": None,
            "right": None,
            "top": None,
            "bottom": None,
            "center": None,
            "animation": None,
            "animationEnter": None,
            "animationUpdate": None,
            "animationExit": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_mark_point_item_line_opts(self):
        opts = MarkPointItemLineOpts()
        expected = {
            "type": None,
            "visible": None,
            "arcRatio": None,
            "decorativeLine": {"visible": None, "length": None},
            "startSymbol": None,
            "endSymbol": None,
            "line": {"state": None, "style": None},
        }
        self.assertEqual(opts.opts, expected)

    def test_axes_label_opts(self):
        opts = AxesLabelOpts()
        expected = {
            "visible": None,
            "type": None,
            "formatMethod": None,
            "formatter": None,
            "space": None,
            "inside": False,
            "minGap": 4,
            "dataFilter": None,
            "style": None,
            "state": None,
            "flush": False,
            "lastVisible": None,
            "autoRotate": None,
            "autoRotateAngle": None,
            "autoHide": None,
            "autoHideMethod": None,
            "autoHideSeparation": None,
            "autoLimit": None,
            "limitEllipsis": "...",
            "autoWrap": None,
            "layoutFunc": None,
            "containerAlign": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_axes_layer_opts(self):
        opts = AxesLayerOpts()
        expected = {
            "tickStep": None,
            "timeFormat": None,
            "timeFormatMode": None,
            "tickCount": None,
            "forceTickCount": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_axes_linear_opts(self):
        opts = AxesLinearOpts()
        expected = {
            "type": "linear",
            "visible": None,
            "min": None,
            "max": None,
            "softMin": None,
            "softMax": None,
            "nice": True,
            "niceType": "tickCountFirst",
            "zero": True,
            "expand": {"min": None, "max": None},
            "sync": {"axisId": None, "zeroAlign": None, "tickAlign": None},
            "tooltipFilterRange": None,
            "breaks": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_axes_band_opts(self):
        opts = AxesBandOpts()
        expected = {
            "trimPadding": None,
            "bandPadding": None,
            "paddingInner": None,
            "paddingOuter": None,
            "domain": None,
            "bandSize": None,
            "maxBandSize": None,
            "minBandSize": None,
            "autoRegionSize": None,
            "showAllGroupLayers": None,
            "layers": None,
            "type": "band",
        }
        self.assertEqual(opts.opts, expected)

    def test_axes_time_opts(self):
        opts = AxesTimeOpts()
        expected = {
            "type": "time",
            "min": None,
            "max": None,
            "softMin": None,
            "softMax": None,
            "nice": None,
            "niceType": None,
            "zero": None,
            "expand": {"min": None, "max": None},
            "sync": {"axisId": None, "zeroAlign": None, "tickAlign": None},
            "tooltipFilterRange": None,
            "breaks": None,
            "layers": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_axes_log_opts(self):
        opts = AxesLogOpts()
        expected = {
            "type": "log",
            "base": 10,
        }
        self.assertEqual(opts.opts, expected)

        base_axes_opts = BaseAxesOpts()
        opts = AxesLogOpts(base_axes_opts=base_axes_opts)
        expected = {
            "alignSelf": None,
            "animation": None,
            "animationAppear": None,
            "animationEnter": None,
            "animationExit": None,
            "animationUpdate": None,
            "autoIndent": None,
            "background": None,
            "base": 10,
            "bottom": None,
            "center": None,
            "clip": None,
            "depth": None,
            "domainLine": None,
            "grid": None,
            "height": None,
            "hover": None,
            "id": None,
            "innerOffset": None,
            "inverse": None,
            "label": None,
            "layoutLevel": None,
            "layoutType": None,
            "left": None,
            "maxHeight": None,
            "maxWidth": None,
            "minHeight": None,
            "minWidth": None,
            "mode": None,
            "offsetX": None,
            "offsetY": None,
            "orient": None,
            "padding": None,
            "regionId": None,
            "regionIndex": None,
            "right": None,
            "sampling": None,
            "select": None,
            "seriesId": None,
            "seriesIndex": None,
            "subGrid": None,
            "subTick": None,
            "tick": None,
            "title": None,
            "top": None,
            "type": "log",
            "unit": {"style": None, "text": None, "visible": None},
            "visible": None,
            "width": None,
            "zIndex": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_tooltip_style_panel_opts(self):
        opts = TooltipStylePanelOpts()
        expected = {
            "padding": None,
            "backgroundColor": None,
            "border": {
                "color": None,
                "width": None,
                "radius": None,
            },
            "shadow": {
                "x": None,
                "y": None,
                "blur": None,
                "spread": None,
                "color": None,
            },
        }
        self.assertEqual(opts.opts, expected)

    def test_tooltip_custom_style_opts(self):
        opts = TooltipCustomStyleOpts()
        expected = {
            "visible": None,
            "key": None,
            "keyTimeFormat": None,
            "keyTimeFormatMode": None,
            "keyFormatter": None,
            "value": None,
            "valueTimeFormat": None,
            "valueTimeFormatMode": None,
            "valueFormatter": None,
            "hasShape": None,
            "shapeType": None,
            "shapeHollow": None,
            "shapeFill": None,
            "shapeStroke": None,
            "shapeLineWidth": None,
            "shapeSize": None,
            "shapeColor": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_tooltip_custom_style_position_opts(self):
        opts = TooltipCustomStylePositionOpts()
        expected = {
            "left": None,
            "right": None,
            "top": None,
            "bottom": None,
            "x": {
                "orient": None,
                "mode": None,
                "offset": None,
            },
            "y": {
                "orient": None,
                "mode": None,
                "offset": None,
            },
        }
        self.assertEqual(opts.opts, expected)

    def test_tooltip_custom_opts(self):
        opts = TooltipCustomOpts()
        expected = {
            "visible": None,
            "triggerMask": None,
            "title": {
                "visible": None,
                "value": None,
                "valueTimeFormat": None,
                "valueTimeFormatMode": None,
                "valueFormatter": None,
            },
            "content": None,
            "position": None,
            "positionMode": None,
            "updateContent": None,
            "updateTitle": None,
            "maxLineCount": None,
            "hasShape": None,
            "shapeType": None,
            "shapeHollow": None,
            "shapeStroke": None,
            "shapeLineWidth": None,
            "shapeSize": None,
            "shapeColor": None,
            "othersLine": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_tooltip_opts(self):
        opts = TooltipOpts()
        expected = {
            "offset": {},
            "visible": True,
        }
        self.assertEqual(expected, remove_key_with_none_value(opts.opts))

    def test_layout_opts(self):
        opts = LayoutOpts()
        expected = {
            "type": "grid",
            "col": None,
            "row": None,
            "colWidth": None,
            "rowHeight": None,
            "elements": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_player_slider_opts(self):
        opts = PlayerSliderOpts()
        expected = {
            "visible": None,
            "space": None,
            "dx": None,
            "dy": None,
            "railStyle": None,
            "trackStyle": None,
            "handlerStyle": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_player_controller_position_opts(self):
        opts = PlayerControllerPositionOpts()
        expected = {
            "space": None,
            "order": None,
            "position": None,
            "style": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_scroll_bar_opts(self):
        opts = ScrollBarOpts()
        expected = {
            "round": None,
            "innerPadding": None,
            "range": None,
            "limitRange": None,
            "rail": {
                "style": None,
            },
            "slider": {
                "style": None,
            },
            "visible": None,
            "orient": None,
            "width": None,
            "height": None,
            "field": None,
            "axisId": None,
            "axisIndex": None,
            "regionId": None,
            "regionIndex": None,
            "filterMode": None,
            "start": None,
            "end": None,
            "startValue": None,
            "endValue": None,
            "rangeMode": None,
            "autoIndent": None,
            "auto": None,
            "zoomLock": None,
            "minSpan": None,
            "maxSpan": None,
            "minValueSpan": None,
            "maxValueSpan": None,
            "delayType": None,
            "delayTime": None,
            "roamZoom": {
                "focus": None,
                "enable": None,
                "rate": None,
            },
            "roamDrag": {
                "reverse": None,
                "enable": None,
                "rate": None,
            },
            "roamScroll": {
                "reverse": None,
            },
            "realTime": None,
            "customDomain": None,
            "updateDataAfterChange": {
                "enable": None,
                "rate": None,
            },
            "layoutType": None,
            "layoutLevel": None,
            "alignSelf": None,
            "padding": None,
            "minWidth": None,
            "maxWidth": None,
            "minHeight": None,
            "maxHeight": None,
            "offsetX": None,
            "offsetY": None,
            "zIndex": None,
            "clip": None,
            "left": None,
            "right": None,
            "top": None,
            "bottom": None,
            "center": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_data_zoom_opts(self):
        opts = DataZoomOpts()
        expected = {
            "valueField": None,
            "startText": {
                "padding": None,
                "style": None,
                "formatMethod": None,
            },
            "endText": {
                "padding": None,
                "style": None,
                "formatMethod": None,
            },
            "brushSelect": None,
            "showDetail": None,
            "middleHandler": {
                "visible": None,
                "icon": {
                    "style": None,
                },
                "background": {
                    "size": None,
                    "style": None,
                },
            },
            "background": {
                "size": None,
                "style": None,
            },
            "startHandler": {
                "style": None,
            },
            "endHandler": {
                "style": None,
            },
            "dragMask": {
                "style": None,
            },
            "selectedBackground": {
                "style": None,
            },
            "showBackgroundChart": None,
            "backgroundChart": {
                "line": {
                    "style": None,
                },
                "area": {
                    "style": None,
                },
            },
            "selectedBackgroundChart": {
                "line": {
                    "style": None,
                },
                "area": {
                    "style": None,
                },
            },
            "ignoreBandSize": None,
            "tolerance": None,
            "visible": None,
            "orient": None,
            "width": None,
            "height": None,
            "field": None,
            "axisId": None,
            "axisIndex": None,
            "regionId": None,
            "regionIndex": None,
            "filterMode": None,
            "start": None,
            "end": None,
            "startValue": None,
            "endValue": None,
            "rangeMode": None,
            "autoIndent": None,
            "auto": None,
            "zoomLock": None,
            "minSpan": None,
            "maxSpan": None,
            "minValueSpan": None,
            "maxValueSpan": None,
            "delayType": None,
            "delayTime": None,
            "roamZoom": {
                "focus": None,
                "enable": None,
                "rate": None,
            },
            "roamDrag": {
                "reverse": None,
                "enable": None,
                "rate": None,
            },
            "roamScroll": {
                "reverse": None,
            },
            "realTime": None,
            "customDomain": None,
            "updateDataAfterChange": {
                "enable": None,
                "rate": None,
            },
            "layoutType": None,
            "layoutLevel": None,
            "alignSelf": None,
            "padding": None,
            "minWidth": None,
            "maxWidth": None,
            "minHeight": None,
            "maxHeight": None,
            "offsetX": None,
            "offsetY": None,
            "zIndex": None,
            "clip": None,
            "left": None,
            "right": None,
            "top": None,
            "bottom": None,
            "center": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_base_custom_mark_opts(self):
        opts = BaseCustomMarkOpts()
        expected = {
            "type": None,
            "dataIndex": None,
            "dataId": None,
            "dataKey": None,
            "componentType": None,
            "id": None,
            "interactive": None,
            "zIndex": None,
            "visible": None,
            "customShape": None,
            "stateSort": None,
            "animation": None,
            "animationAppear": None,
            "animationEnter": None,
            "animationUpdate": None,
            "animationExit": None,
            "style": None,
            "layoutType": None,
            "layoutLevel": None,
            "alignSelf": None,
            "padding": None,
            "width": None,
            "minWidth": None,
            "maxWidth": None,
            "height": None,
            "minHeight": None,
            "maxHeight": None,
            "offsetX": None,
            "offsetY": None,
            "clip": None,
            "left": None,
            "right": None,
            "top": None,
            "bottom": None,
            "center": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_select_opts(self):
        opts = SelectOpts()
        expected = {
            "enable": None,
            "mode": None,
            "trigger": None,
            "triggerOff": None,
        }
        self.assertEqual(opts.opts, expected)

    def test_title_text_character_opts(self):
        # 测试 text 类型
        text_opts = TextConfigTextOpts(text="Sample Text")
        opts = TitleTextCharacterOpts(type_="text", text_opts=text_opts)
        expected = {
            "type": "text",
            "text": "Sample Text",
            "fontStyle": "normal",
        }
        self.assertEqual(remove_key_with_none_value(opts.opts), expected)

        # 测试 image 类型
        image_opts = TextConfigImageOpts(image="data:image/png;base64,...")
        opts = TitleTextCharacterOpts(type_="image", image_opts=image_opts)
        expected = {"type": "image", "image": "data:image/png;base64,..."}
        self.assertEqual(remove_key_with_none_value(opts.opts), expected)

        # 测试未指定类型的情况
        opts = TitleTextCharacterOpts()
        self.assertIsNone(opts.opts)

    def test_label_rich_text_config_opts(self):
        # 测试 text 类型
        text_opts = TextConfigTextOpts(text="Sample Text")
        opts = LabelRichTextConfigOpts(type_="text", text_opts=text_opts)
        expected = {
            "type": "text",
            "text": "Sample Text",
            "fontStyle": "normal",
        }
        self.assertEqual(remove_key_with_none_value(opts.opts), expected)

        # 测试 image 类型
        image_opts = TextConfigImageOpts(image="data:image/png;base64,...")
        opts = LabelRichTextConfigOpts(type_="image", image_opts=image_opts)
        expected = {"type": "image", "image": "data:image/png;base64,..."}
        self.assertEqual(remove_key_with_none_value(opts.opts), expected)

        # 测试未指定类型的情况
        opts = LabelRichTextConfigOpts()
        self.assertIsNone(opts.opts)

    def test_label_style_opts(self):
        # 测试 text 类型
        text_style_opts = BaseStyleOpts(fill="red")
        opts = LabelStyleOpts(type_="text", text_style_opts=text_style_opts)
        expected = {"type": "text", "fill": "red"}
        self.assertEqual(remove_key_with_none_value(opts.opts), expected)

        # 测试 rich 类型
        rich_style_opts = LabelRichStyleOpts(width=100, height=50)
        opts = LabelStyleOpts(type_="rich", rich_style_opts=rich_style_opts)
        expected = {
            "ellipsis": False,
            "fontStyle": "normal",
            "height": 50,
            "layoutDirection": "horizontal",
            "singleLine": False,
            "type": "rich",
            "width": 100,
            "wordBreak": "break-word",
        }
        self.assertEqual(remove_key_with_none_value(opts.opts), expected)

        # 测试未指定类型的情况
        opts = LabelStyleOpts()
        self.assertIsNone(opts.opts)

    def test_label_overlap_opts(self):
        opts = LabelOverlapOpts()
        self.assertEqual(
            opts.opts,
            {
                "hideOnHit": None,
                "clampForce": None,
                "avoidBaseMark": None,
                "strategy": None,
            },
        )

    def test_tooltip_style_shape_opts(self):
        opts = TooltipStyleShapeOpts()
        expected = {
            "size": None,
            "spacing": None,
            "hasShape": None,
            "shapeType": None,
            "shapeHollow": None,
            "shapeFill": None,
            "shapeStroke": None,
            "shapeLineWidth": None,
            "shapeSize": None,
            "shapeColor": None,
        }
        self.assertEqual(opts.opts, expected)
