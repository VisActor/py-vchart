import unittest

from pyvchart import options as opts
from pyvchart.charts import Bar
from pyvchart.globals import ChartType

from test import chart_base_test


TEST_BAR_DATA = [
    {"month": "Monday", "sales": 22},
    {"month": "Tuesday", "sales": 13},
    {"month": "Wednesday", "sales": 25},
    {"month": "Thursday", "sales": 29},
    {"month": "Friday", "sales": 38},
]


class TestBarChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.BAR)
    def test_bar_base(self):
        c = (
            Bar()
            .set_bar_spec()
            .set_data(data=[opts.BaseDataOpts(values=TEST_BAR_DATA)])
            .set_xy_field(
                x_field_name="time",
                y_field_name="value",
            )
        )
        return c
