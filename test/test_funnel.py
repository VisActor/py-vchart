import unittest

from pyvchart import options as opts
from pyvchart.charts import Funnel
from pyvchart.globals import ChartType

from test import chart_base_test


TEST_FUNNEL_DATA = [
    {"value": 100, "name": "Step1"},
    {"value": 80, "name": "Step2"},
    {"value": 60, "name": "Step3"},
    {"value": 40, "name": "Step4"},
    {"value": 20, "name": "Step5"},
]


class TestFunnelChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.FUNNEL)
    def test_funnel_base(self):
        c = (
            Funnel()
            .set_data(data=[opts.BaseDataOpts(values=TEST_FUNNEL_DATA)])
            .set_funnel_spec(
                category_field="name",
                value_field="value",
                label_opts=opts.LabelOpts(is_visible=True),
            )
            .set_global_options(
                legend_opts=opts.BaseLegendOpts(
                    is_visible=True,
                    orient="bottom",
                ),
            )
        )
        return c
