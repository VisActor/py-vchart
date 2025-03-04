import unittest

from pyvchart.options.charts_options import (
    AreaOpts,
    ArrowOpts,
    BarOpts,
    BarBackgroundOpts,
    Bar3DOpts,
    BaseDataOpts,
    BoxplotOpts,
    CirclePackingOpts,
    CorrelationCenterPointOpts,
    CorrelationRipplePointOpts,
    CorrelationNodePointOpts,
    DotOpts,
    DotGridOpts,
    DotSubTitleOpts,
    DotSymbolOpts,
    DotTitleOpts,
    FunnelOpts,
    Funnel3DOpts,
    FunnelTransformOpts,
    GaugeSegmentOpts,
    GaugeTrackOpts,
    GaugeOpts,
    GaugePinOpts,
    GaugePinBackgroundOpts,
    GaugePointerOpts,
    HeatMapCellOpts,
    HeatMapCellBackgroundOpts,
    InteractionOpts,
    LineOpts,
    LineCurveLabelOpts,
    LinkOpts,
    LiquidOpts,
    LiquidBackgroundOpts,
    MapLabelOpts,
    PictogramOpts,
    PieOpts,
    PointOpts,
    ProgressOpts,
    RoseOpts,
    SankeyEmphasisOpts,
    SankeyLinkOpts,
    SankeyNodeOpts,
    SunburstOpts,
    TrackOpts,
    TreeMapLeafOpts,
    TreeMapNonLeafOpts,
    WaterfallLeaderLineOpts,
    WaterfallTotalCustomOpts,
    WaterfallTotalEndOpts,
    WaterfallTotalFieldOpts,
    WordCloudOpts,
    WordCloudConfigOpts,
    WordCloudShapeConfigOpts,
    WordCloud3DFillingWordOpts,
    VennCircleOpts,
    VennOverlapOpts,
    TextConfigTextOpts,
    TextConfigImageOpts,
)


class TestChartOptions(unittest.TestCase):

    def test_base_data_opts(self):
        obj = BaseDataOpts(values=None)
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "values": None,
                "fromDataId": None,
                "fromDataIndex": None,
                "transform": None,
                "fields": None,
                "parser": None,
            },
        )

    def test_interaction_opts(self):
        obj = InteractionOpts()
        self.assertEqual(
            obj.opts,
            {
                "markIds": None,
                "markNames": None,
                "type": None,
                "state": None,
                "filterType": None,
                "filterField": None,
                "highlightState": None,
                "blurState": None,
                "isMultiple": None,
                "trigger": None,
                "triggerOff": None,
                "graphicName": None,
                "parseData": None,
            },
        )

    def test_bar_opts(self):
        obj = BarOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_bar_background_opts(self):
        obj = BarBackgroundOpts()
        self.assertEqual(
            obj.opts,
            {
                "fieldLevel": None,
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_bar3d_opts(self):
        obj = Bar3DOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_pie_opts(self):
        obj = PieOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_line_opts(self):
        obj = LineOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_point_opts(self):
        obj = PointOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_line_curve_label_opts(self):
        obj = LineCurveLabelOpts()
        self.assertEqual(
            obj.opts,
            {
                "position": "end",
                "visible": False,
                "interactive": False,
                "formatMethod": None,
                "formatter": None,
                "syncState": False,
                "offset": 5,
                "style": None,
                "state": None,
                "overlap": {
                    "hideOnHit": None,
                    "clampForce": None,
                    "avoidBaseMark": None,
                    "strategy": None,
                },
                "dataFilter": None,
                "customLayoutFunc": None,
                "customOverlapFunc": None,
                "animation": None,
                "stackDataFilterType": None,
                "invalidType": None,
            },
        )

    def test_area_opts(self):
        obj = AreaOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_heat_map_cell_opts(self):
        obj = HeatMapCellOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_heat_map_cell_background_opts(self):
        obj = HeatMapCellBackgroundOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_progress_opts(self):
        obj = ProgressOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "topPadding": None,
                "bottomPadding": None,
                "leftPadding": None,
                "rightPadding": None,
                "style": None,
                "state": None,
            },
        )

    def test_track_opts(self):
        obj = TrackOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_sankey_node_opts(self):
        obj = SankeyNodeOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_sankey_link_opts(self):
        obj = SankeyLinkOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_sankey_emphasis_opts(self):
        obj = SankeyEmphasisOpts()
        self.assertEqual(
            obj.opts,
            {
                "enable": None,
                "trigger": None,
                "effect": None,
            },
        )

    def test_funnel_opts(self):
        obj = FunnelOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_funnel_transform_opts(self):
        obj = FunnelTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_funnel3d_opts(self):
        obj = Funnel3DOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_word_cloud_config_opts(self):
        obj = WordCloudConfigOpts()
        self.assertEqual(
            obj.opts,
            {
                "drawOutOfBound": None,
                "ellipsis": {
                    "string": None,
                    "limitLength": None,
                },
                "zoomToFit": {
                    "shrink": None,
                    "enlarge": None,
                    "fontSizeLimitMin": None,
                    "fontSizeLimitMax": None,
                },
                "layoutMode": None,
                "progressiveTime": None,
                "progressiveStep": None,
            },
        )

    def test_word_cloud_shape_config_opts(self):
        obj = WordCloudShapeConfigOpts()
        self.assertEqual(
            obj.opts,
            {
                "fillingColorList": None,
                "fillingFontFamilyField": None,
                "fillingFontWeightField": None,
                "fillingFontStyleField": None,
                "fillingColorHexField": None,
                "fillingRotateAnglesField": None,
                "ratio": None,
                "removeWhiteBorder": None,
                "layoutMode": None,
                "fillingTimes": None,
                "fillingXStep": None,
                "fillingYStep": None,
                "fillingXRatioStep": None,
                "fillingYRatioStep": None,
                "fillingInitialFontSize": None,
                "fillingDeltaFontSize": None,
                "fillingInitialOpacity": None,
                "fillingDeltaOpacity": None,
                "textLayoutTimes": None,
                "fontSizeShrinkFactor": None,
                "stepFactor": None,
                "importantWordCount": None,
                "globalShinkLimit": None,
                "fontSizeEnlargeFactor": None,
                "fillingDeltaFontSizeFactor": None,
                "fillingRatio": None,
            },
        )

    def test_word_cloud_opts(self):
        obj = WordCloudOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "padding": None,
                "formatMethod": None,
                "style": None,
                "state": None,
            },
        )

    def test_word_cloud3d_filling_word_opts(self):
        obj = WordCloud3DFillingWordOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "padding": None,
                "style": None,
                "state": None,
            },
        )

    def test_map_label_opts(self):
        obj = MapLabelOpts()
        self.assertEqual(
            obj.opts,
            {
                "seriesId": None,
                "visible": None,
                "nameField": None,
                "valueField": None,
                "trigger": None,
                "offset": 12,
                "space": 10,
                "position": "top",
                "nameLabel": {
                    "visible": None,
                    "style": None,
                },
                "valueLabel": {
                    "visible": None,
                    "style": None,
                },
                "icon": {
                    "visible": None,
                    "style": None,
                },
                "background": {
                    "visible": None,
                    "padding": None,
                    "style": None,
                },
                "leader": {
                    "visible": None,
                    "style": None,
                },
            },
        )

    def test_tree_map_leaf_opts(self):
        obj = TreeMapLeafOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_tree_map_non_leaf_opts(self):
        obj = TreeMapNonLeafOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_sunburst_opts(self):
        obj = SunburstOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_circle_packing_opts(self):
        obj = CirclePackingOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_waterfall_total_end_opts(self):
        obj = WaterfallTotalEndOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "end",
                "text": None,
            },
        )

    def test_waterfall_total_custom_opts(self):
        obj = WaterfallTotalCustomOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "custom",
                "tagField": None,
                "product": None,
                "text": None,
            },
        )

    def test_waterfall_total_field_opts(self):
        obj = WaterfallTotalFieldOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "field",
                "tagField": None,
                "valueField": None,
                "startField": None,
                "collectCountField": None,
                "text": None,
            },
        )

    def test_waterfall_leader_line_opts(self):
        obj = WaterfallLeaderLineOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_gauge_pointer_opts(self):
        obj = GaugePointerOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": None,
                "width": None,
                "height": None,
                "innerPadding": None,
                "outerPadding": None,
                "center": None,
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_gauge_pin_opts(self):
        obj = GaugePinOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_gauge_pin_background_opts(self):
        obj = GaugePinBackgroundOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_gauge_segment_opts(self):
        obj = GaugeSegmentOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_gauge_track_opts(self):
        obj = GaugeTrackOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_arrow_opts(self):
        obj = ArrowOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_boxplot_opts(self):
        obj = BoxplotOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_correlation_center_point_opts(self):
        obj = CorrelationCenterPointOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_correlation_ripple_point_opts(self):
        obj = CorrelationRipplePointOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_correlation_node_point_opts(self):
        obj = CorrelationNodePointOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_dot_opts(self):
        obj = DotOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_dot_grid_opts(self):
        obj = DotGridOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_dot_sub_title_opts(self):
        obj = DotSubTitleOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": None,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_dot_symbol_opts(self):
        obj = DotSymbolOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_dot_title_opts(self):
        obj = DotTitleOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": None,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_gauge_opts(self):
        obj = GaugeOpts()
        self.assertEqual(
            obj.opts,
            {
                "seriesField": None,
                "seriesStyle": None,
                "stack": None,
                "stackValue": None,
                "percent": None,
                "stackOffsetSilhouette": None,
                "invalidType": None,
                "dataKey": None,
                "extensionMark": None,
                "hover": None,
                "select": None,
                "animationAppear": None,
                "animationEnter": None,
                "animationUpdate": None,
                "animationExit": None,
                "animationDisappear": None,
                "animationState": None,
                "interactions": None,
                "categoryField": None,
                "valueField": None,
                "outerRadius": None,
                "innerRadius": None,
                "startAngle": -90,
                "endAngle": 270,
                "centerX": None,
                "centerY": None,
                "cornerRadius": None,
                "roundCap": None,
                "padAngle": None,
                "segment": None,
                "track": None,
                "label": None,
            },
        )

    def test_link_opts(self):
        obj = LinkOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_liquid_opts(self):
        obj = LiquidOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_liquid_background_opts(self):
        obj = LiquidBackgroundOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_pictogram_opts(self):
        obj = PictogramOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_rose_opts(self):
        obj = RoseOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_venn_circle_opts(self):
        obj = VennCircleOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_venn_overlap_opts(self):
        obj = VennOverlapOpts()
        self.assertEqual(
            obj.opts,
            {
                "id": None,
                "interactive": True,
                "zIndex": None,
                "visible": None,
                "customShape": None,
                "stateSort": None,
                "style": None,
                "state": None,
            },
        )

    def test_text_config_text_opts(self):
        opts = TextConfigTextOpts()
        assert opts.opts == {
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

    def test_text_config_image_opts(self):
        # 测试所有参数均为默认值
        opts = TextConfigImageOpts()
        assert opts.opts == {
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
