import unittest

from pyvchart import options as opts
from pyvchart.charts import Boxplot
from pyvchart.globals import ChartType

from test import chart_base_test

TEST_BOXPLOT_DATA = [
    {
        "x": "Sub-Saharan Africa",
        "y1": 8.72,
        "y2": 9.73,
        "y3": 10.17,
        "y4": 10.51,
        "y5": 11.64,
    },
    {"x": "South Asia", "y1": 9.4, "y2": 10.06, "y3": 10.75, "y4": 11.56, "y5": 12.5},
    {
        "x": "Middle East & North Africa",
        "y1": 9.54,
        "y2": 10.6,
        "y3": 11.05,
        "y4": 11.5,
        "y5": 11.92,
    },
    {
        "x": "Latin America & Caribbean",
        "y1": 8.74,
        "y2": 9.46,
        "y3": 10.35,
        "y4": 10.94,
        "y5": 12.21,
    },
    {
        "x": "East Asia & Pacific",
        "y1": 7.8,
        "y2": 8.95,
        "y3": 10.18,
        "y4": 11.57,
        "y5": 13.25,
    },
    {
        "x": "Europe & Central Asia",
        "y1": 9.52,
        "y2": 10.39,
        "y3": 10.93,
        "y4": 11.69,
        "y5": 12.63,
    },
]


class TestBoxplotChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.BOXPLOT)
    def test_boxplot_base(self):
        c = (
            Boxplot()
            .set_data(data=[opts.BaseDataOpts(values=TEST_BOXPLOT_DATA)])
            .set_boxplot_spec(
                min_field="y1",
                q1_field="y2",
                median_field="y3",
                q3_field="y4",
                max_field="y5",
                direction="vertical",
                boxplot_opts=opts.BoxplotOpts(style=opts.BaseStyleOpts(line_width=2)),
            )
            .set_xy_field(
                x_field_name="x",
                y_field_name=None,
            )
        )
        return c
