import os

from jinja2 import Environment, FileSystemLoader


class _FileType:
    SVG: str = "svg"
    PNG: str = "png"
    JPEG: str = "jpeg"
    HTML: str = "html"


class _ChartType:
    AREA: str = "area"
    BAR: str = "bar"
    BAR3D: str = "bar3d"
    BOXPLOT: str = "boxPlot"
    CIRCLE_PACKING: str = "circlePacking"
    CIRCULAR_PROGRESS: str = "circularProgress"
    CORRELATION: str = "correlation"
    COMMON: str = "common"
    DOT: str = "dot"
    FUNNEL: str = "funnel"
    FUNNEL3D: str = "funnel3d"
    GAUGE: str = "gauge"
    HEATMAP: str = "heatmap"
    HISTOGRAM: str = "histogram"
    LINE: str = "line"
    LINEAR_PROGRESS: str = "linearProgress"
    LINK: str = "link"
    LIQUID: str = "liquid"
    MAP: str = "map"
    MOSAIC: str = "mosaic"
    PICTOGRAM: str = "pictogram"
    PIE: str = "pie"
    RADAR: str = "radar"
    RANGE_AREA: str = "rangeArea"
    RANGE_COLUMN: str = "rangeColumn"
    ROSE: str = "rose"
    SANKEY: str = "sankey"
    SEQUENCE: str = "sequence"
    SCATTER: str = "scatter"
    SUNBURST: str = "sunburst"
    TREEMAP: str = "treemap"
    VENN: str = "venn"
    WATERFALL: str = "waterfall"
    WORDCLOUD: str = "wordCloud"
    WORDCLOUD3D: str = "wordCloud3d"


class _NotebookType:
    JUPYTER_NOTEBOOK = "jupyter_notebook"
    JUPYTER_LAB = "jupyter_lab"
    NTERACT = "nteract"
    ZEPPELIN = "zeppelin"


class _OnlineHost:
    DEFAULT_HOST = "https://unpkg.com/@visactor/vchart@1.13.5/build/"
    NOTEBOOK_HOST = "http://localhost:8888/nbextensions/assets/"


class _RenderSepType:
    SepType = os.linesep


class _RegisterFunctionType:
    Liquid = "VChart.registerLiquidChart();"
    Venn = "VChart.registerVennChart();"
    Mosaic = "VChart.registerMosaicChart();"
    Pictogram = "VChart.registerPictogramChart();"


FileType = _FileType()
ChartType = _ChartType
NotebookType = _NotebookType()
OnlineHostType = _OnlineHost()
RenderSepType = _RenderSepType()
RegisterFunctionType = _RegisterFunctionType()


class _CurrentConfig:
    PAGE_TITLE = "Awesome-pyvchart"
    ONLINE_HOST = OnlineHostType.DEFAULT_HOST
    NOTEBOOK_TYPE = NotebookType.JUPYTER_NOTEBOOK
    GLOBAL_ENV = Environment(
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
        loader=FileSystemLoader(
            os.path.join(
                os.path.abspath(os.path.dirname(__file__)), "render", "templates"
            )
        ),
    )


CurrentConfig = _CurrentConfig()
