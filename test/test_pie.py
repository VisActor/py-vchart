import unittest

from pyvchart import options as opts
from pyvchart.charts import Pie
from pyvchart.commons.utils import JsCode
from pyvchart.globals import ChartType

from test import chart_base_test

TEST_PIE_DATA = [
    {"type": "oxygen", "value": "46.60"},
    {"type": "silicon", "value": "27.72"},
    {"type": "aluminum", "value": "8.13"},
    {"type": "iron", "value": "5"},
    {"type": "calcium", "value": "3.63"},
    {"type": "sodium", "value": "2.83"},
    {"type": "potassium", "value": "2.59"},
    {"type": "others", "value": "3.5"},
]


class TestPieChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.PIE)
    def test_pie_base(self):
        c = (
            Pie()
            .set_data(data=[opts.BaseDataOpts(values=TEST_PIE_DATA)])
            .set_pie_spec(
                outer_radius=0.8,
                value_field="value",
                category_field="type",
                label_opts=opts.LabelOpts(is_visible=True),
            )
            .set_global_options(
                title_opts=opts.TitleOpts(
                    is_visible=True,
                    text="Statistics of Surface Element Content",
                ),
                legend_opts=opts.BaseLegendOpts(
                    is_visible=True,
                    orient="left",
                ),
                tooltip_opts=opts.TooltipOpts(
                    mark_opts=opts.TooltipCustomOpts(
                        content=[
                            opts.TooltipCustomStyleOpts(
                                key=JsCode("datum => datum['type']"),
                                value=JsCode("datum => datum['value'] + '%'"),
                            )
                        ]
                    )
                ),
            )
        )
        return c
