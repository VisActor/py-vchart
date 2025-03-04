import unittest
import urllib.request

from pyvchart import options as opts
from pyvchart.charts import Pictogram
from pyvchart.commons.utils import JsCode
from pyvchart.globals import ChartType

from test import chart_base_test


TEST_PICTOGRAM_DATA = [
    {"name": "Yes", "value": "Love This"},
    {"name": "So-so"},
    {"name": "Forbidden"},
    {"name": "Horror"},
]

req = urllib.request.Request(
    url="https://lf9-dp-fe-cms-tos.byteorg.com/obj/bit-cloud/pictogram/cat.svg"
)
resp = urllib.request.urlopen(req)
TEST_SVG_CONTENT = resp.read().decode("utf-8")


class TestPictogramChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.PICTOGRAM)
    def test_pictogram_base(self):
        c = (
            Pictogram()
            .set_data(data=[opts.BaseDataOpts(id_="data", values=TEST_PICTOGRAM_DATA)])
            .register_svg(name="cat", svg_path=TEST_SVG_CONTENT)
            .set_pictogram_spec(
                name_field="name",
                value_field="value",
                svg="cat",
                pictogram_opts=opts.PictogramOpts(
                    style=opts.BaseStyleOpts(
                        fill={
                            "scale": "color",
                            "field": "name",
                        },
                    ),
                    state=opts.BaseStateOpts(
                        active_opts=opts.BaseStyleOpts(
                            fill_opacity=0.8,
                            stroke={
                                "scale": "color",
                                "field": "name",
                            },
                            line_width=2,
                        ),
                        hover_opts=opts.BaseStyleOpts(
                            fill_opacity=0.8,
                            stroke={
                                "scale": "color",
                                "field": "name",
                            },
                            line_width=2,
                        ),
                    ),
                ),
            )
            .set_global_options(
                series_field="name",
                color_opts=opts.ColorOpts(
                    specified={
                        "Yes": "#009A00",
                        "So-so": "#FEB202",
                        "Forbidden": "#FE3E00",
                        "Horror": "#FE2B09",
                        "undefined": "white",
                    }
                ),
                interaction_opts=[
                    opts.InteractionOpts(
                        type_="element-active-by-legend",
                        filter_field="name",
                    )
                ],
                region_opts=[
                    opts.RegionOpts(roam={"blank": True}),
                ],
                title_opts=opts.TitleOpts(text="Cat Stroking For Beginners"),
                legend_opts=opts.BaseLegendOpts(orient="top", is_filter=False),
            )
        )
        return c
