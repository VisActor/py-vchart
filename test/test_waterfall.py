import unittest

from pyvchart import options as opts
from pyvchart.charts import Waterfall
from pyvchart.commons.utils import JsCode
from pyvchart.globals import ChartType

from test import chart_base_test


TEST_WATERFALL_DATA = [
    {"x": "Feb.4", "total": True, "value": 45},
    {"x": "Feb.11", "y": -5},
    {"x": "Feb.20", "y": 2},
    {"x": "Feb.25", "y": -2},
    {"x": "Mar.4", "y": 2},
    {"x": "Mar.11", "y": 2},
    {"x": "Mar.19", "y": -2},
    {"x": "Mar.26", "y": 1},
    {"x": "Apr.1", "y": 1},
    {"x": "Apr.8", "y": 1},
    {"x": "Apr.15", "y": 2},
    {"x": "Apr.22", "y": 1},
    {"x": "Apr.29", "y": -2},
    {"x": "May.6", "y": -1},
    {"x": '"total"', "total": True},
]


class TestWaterfallChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.WATERFALL)
    def test_waterfall_base(self):
        c = (
            Waterfall()
            .set_data(data=[opts.BaseDataOpts(id_="id0", values=TEST_WATERFALL_DATA)])
            .set_xy_field(x_field_name="x", y_field_name="y")
            .set_waterfall_spec(
                stack_label_opts=opts.LabelOpts(
                    value_type="absolute",
                    format_method=JsCode("text => { return text + '%'; }"),
                ),
                total_opts=opts.WaterfallTotalFieldOpts(
                    tag_field="total",
                    value_field="value",
                ),
            )
            .set_global_options(
                legend_opts=opts.BaseLegendOpts(is_visible=True, orient="bottom"),
                axes_opts=[
                    opts.AxesLinearOpts(
                        min_=30,
                        max_=50,
                        base_axes_opts=opts.BaseAxesOpts(
                            orient="left",
                            title=opts.TitleOpts(is_visible=True, text="favorability"),
                            label=opts.AxesLabelOpts(
                                format_method=JsCode("v => { return v + '%'; }")
                            ),
                        ),
                    ),
                    opts.AxesBandOpts(
                        base_axes_opts=opts.BaseAxesOpts(
                            orient="bottom",
                            label=opts.AxesLabelOpts(is_visible=True),
                            title=opts.TitleOpts(is_visible=True, text="data"),
                        ),
                        padding_inner=0.4,
                    ),
                ],
            )
        )
        return c
