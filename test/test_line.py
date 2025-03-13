import unittest

from pyvchart import options as opts
from pyvchart.charts import Line
from pyvchart.globals import ChartType

from test import chart_base_test


TEST_LINE_DATA = [
    {"date": "2023-01-01", "type": "Product A", "value": 99.9},
    {"date": "2023-01-01", "type": "Product B", "value": 96.6},
    {"date": "2023-01-01", "type": "Product C", "value": 96.2},
    {"date": "2023-01-02", "type": "Product A", "value": 96.7},
    {"date": "2023-01-02", "type": "Product B", "value": 91.1},
    {"date": "2023-01-02", "type": "Product C", "value": 93.4},
    {"date": "2023-01-03", "type": "Product A", "value": 100.2},
    {"date": "2023-01-03", "type": "Product B", "value": 99.4},
    {"date": "2023-01-03", "type": "Product C", "value": 91.7},
    {"date": "2023-01-04", "type": "Product A", "value": 104.7},
    {"date": "2023-01-04", "type": "Product B", "value": 108.1},
    {"date": "2023-01-04", "type": "Product C", "value": 93.1},
    {"date": "2023-01-05", "type": "Product A", "value": 95.6},
    {"date": "2023-01-05", "type": "Product B", "value": 96},
    {"date": "2023-01-05", "type": "Product C", "value": 92.3},
    {"date": "2023-01-06", "type": "Product A", "value": 95.6},
    {"date": "2023-01-06", "type": "Product B", "value": 89.1},
    {"date": "2023-01-06", "type": "Product C", "value": 92.5},
    {"date": "2023-01-07", "type": "Product A", "value": 95.3},
    {"date": "2023-01-07", "type": "Product B", "value": 89.2},
    {"date": "2023-01-07", "type": "Product C", "value": 95.7},
    {"date": "2023-01-08", "type": "Product A", "value": 96.1},
    {"date": "2023-01-08", "type": "Product B", "value": 97.6},
    {"date": "2023-01-08", "type": "Product C", "value": 99.9},
    {"date": "2023-01-09", "type": "Product A", "value": 96.1},
    {"date": "2023-01-09", "type": "Product B", "value": 100.6},
    {"date": "2023-01-09", "type": "Product C", "value": 103.8},
    {"date": "2023-01-10", "type": "Product A", "value": 101.6},
    {"date": "2023-01-10", "type": "Product B", "value": 108.3},
    {"date": "2023-01-10", "type": "Product C", "value": 108.9},
]


class TestLineChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.LINE)
    def test_line_base(self):
        c = (
            Line()
            .set_data(data=[opts.BaseDataOpts(values=TEST_LINE_DATA)])
            .set_line_spec(point_opts=opts.PointOpts(is_visible=False))
            .set_xy_field(x_field_name="date", y_field_name="date")
            .set_global_options(series_field="type")
        )
        return c
