import unittest

from pyvchart import options as opts
from pyvchart.charts import Gauge
from pyvchart.globals import ChartType

from test import chart_base_test

TEST_GAUGE_DATA = [{"type": "目标A", "value": 0.6}]


class TestGaugeChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.GAUGE)
    def test_gauge_base(self):
        c = (
            Gauge()
            .set_data(data=[opts.BaseDataOpts(id_="id0", values=TEST_GAUGE_DATA)])
            .set_gauge_spec(
                category_field="type",
                value_field="value",
                outer_radius=0.8,
                inner_radius=0.5,
                start_angle=-180,
                end_angle=0,
            )
        )
        return c
