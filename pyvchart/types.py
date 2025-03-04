from typing import (
    Any,
    Callable,
    Iterable,
    List,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    Union,
)

from . import options as opts
from .options.series_options import JsCode, JSFunc, Numeric

BaseData = Union[opts.BaseDataOpts, dict]
BaseHtmlOrReact = Union[opts.BaseHtmlOrReactOpts, dict]
BaseBorder = Union[opts.BaseBorderOpts, dict]
BaseTitleTextStyle = Union[opts.BaseTitleTextStyleOpts, dict]
Color = Union[opts.ColorOpts, dict]
Indicator = Union[opts.IndicatorOpts, dict]
IndicatorTitle = Union[opts.IndicatorTitleOpts, dict]
IndicatorContent = Union[opts.IndicatorContentOpts, dict]
Init = Union[opts.InitOpts, dict]
Interaction = Union[opts.InteractionOpts, dict]
Padding = Union[opts.PaddingOpts, dict]
Region = Union[opts.RegionOpts, dict]
RenderInit = Union[opts.RenderOpts, dict]
Title = Union[opts.TitleOpts, dict]
LegendTitle = Union[opts.LegendTitleOpts, dict]
BaseLegend = Union[opts.BaseLegendOpts, dict]
DiscreteLegend = Union[opts.DiscreteLegendOpts, dict]
DiscreteLegendItem = Union[opts.DiscreteLegendItemOpts, dict]
DiscreteLegendPager = Union[opts.DiscreteLegendPagerOpts, dict]
ColorLegend = Union[opts.ColorLegendOpts, dict]
SizeLegend = Union[opts.SizeLegendOpts, dict]
Legend = Union[DiscreteLegend, ColorLegend, SizeLegend]
BaseMark = Union[opts.BaseMarkOpts, dict]
MarkCoordinates = Union[opts.MarkCoordinatesOpts, dict]
MarkLine = Union[opts.MarkLineOpts, dict]
MarkArea = Union[opts.MarkAreaOpts, dict]
MarkPoint = Union[opts.MarkPointOpts, dict]
CrossHairField = Union[opts.CrossHairFieldOpts, dict]
CrossHair = Union[opts.CrossHairOpts, dict]
AxesTick = Union[opts.AxesTickOpts, dict]
AxesSubTick = Union[opts.AxesSubTickOpts, dict]
AxesGrid = Union[opts.AxesGridOpts, dict]
AxesBackground = Union[opts.AxesBackgroundOpts, dict]
AxesLabel = Union[opts.AxesLabelOpts, dict]
AxesDomainLine = Union[opts.AxesDomainLineOpts, dict]
BaseAxes = Union[opts.BaseAxesOpts, dict]
AxesBreak = Union[opts.AxesBreakOpts, dict]
AxesLayer = Union[opts.AxesLayerOpts, dict]
AxesLinear = Union[opts.AxesLinearOpts, dict]
AxesBand = Union[opts.AxesBandOpts, dict]
AxesTime = Union[opts.AxesTimeOpts, dict]
AxesLog = Union[opts.AxesLogOpts, dict]
AxesSymlog = Union[opts.AxesSymlogOpts, dict]
Axes = Union[AxesLinear, AxesBand, AxesTime, AxesLog, AxesSymlog]
Tooltip = Union[opts.TooltipOpts, dict]
LayoutColRow = Union[opts.LayoutColRowOpts, dict]
LayoutElement = Union[opts.LayoutElementOpts, dict]
Layout = Union[opts.LayoutOpts, dict]
Player = Union[opts.PlayerOpts, dict]
PlayerSlider = Union[opts.PlayerSliderOpts, dict]
PlayerController = Union[opts.PlayerControllerOpts, dict]
PlayerControllerPosition = Union[opts.PlayerControllerPositionOpts, dict]
ScrollBar = Union[opts.ScrollBarOpts, dict]
DataZoom = Union[opts.DataZoomOpts, dict]
Brush = Union[opts.BrushOpts, dict]
ZoomWhenEmpty = Union[opts.ZoomWhenEmptyOpts, dict]
Scales = Union[opts.ScalesOpts, dict]
BaseCustomMark = Union[opts.BaseCustomMarkOpts, dict]
CustomMarkSymbol = Union[opts.CustomMarkSymbolOpts, dict]
CustomMarkRule = Union[opts.CustomMarkRuleOpts, dict]
CustomMarkText = Union[opts.CustomMarkTextOpts, dict]
CustomMarkRect = Union[opts.CustomMarkRectOpts, dict]
CustomMarkPath = Union[opts.CustomMarkPathOpts, dict]
CustomMarkArc = Union[opts.CustomMarkArcOpts, dict]
CustomMarkPolygon = Union[opts.CustomMarkPolygonOpts, dict]
CustomMarkImage = Union[opts.CustomMarkImageOpts, dict]
CustomMarkGroup = Union[opts.CustomMarkGroupOpts, dict]
CustomMark = Union[
    CustomMarkSymbol,
    CustomMarkText,
    CustomMarkRect,
    CustomMarkPath,
    CustomMarkArc,
    CustomMarkPolygon,
    CustomMarkImage,
    CustomMarkGroup,
]
Theme = Union[opts.ThemeOpts, dict]
Hover = Union[opts.HoverOpts, dict]
Select = Union[opts.SelectOpts, dict]
WaterfallTotal = Union[
    opts.WaterfallTotalCustomOpts,
    opts.WaterfallTotalEndOpts,
    opts.WaterfallTotalFieldOpts,
]
