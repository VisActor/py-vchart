import unittest

from pyvchart import options as opts
from pyvchart.charts import Rose
from pyvchart.globals import ChartType

from test import chart_base_test


TEST_ROSE_DATA = [
    {"value": "159", "type": "Tradition Industries"},
    {"value": "50", "type": "Business Companies"},
    {"value": "13", "type": "Customer-facing Companies"},
]


class TestRoseChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.ROSE)
    def test_rose_base(self):
        c = (
            Rose()
            .set_data(data=[opts.BaseDataOpts(values=TEST_ROSE_DATA)])
            .set_rose_spec(
                outer_radius=0.8,
                inner_radius=0.2,
                category_field="type",
                value_field="value",
                label_opts=opts.LabelOpts(
                    is_visible=True,
                ),
            )
            .set_global_options(
                series_field="type",
            )
        )
        return c
