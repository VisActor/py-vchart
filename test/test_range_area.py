import unittest

from pyvchart import options as opts
from pyvchart.charts import RangeArea
from pyvchart.globals import ChartType

from test import chart_base_test


TEST_RANGE_AREA_DATA = [
    {"type": "Category One", "min": 76, "max": 100},
    {"type": "Category Two", "min": 56, "max": 108},
    {"type": "Category Three", "min": 38, "max": 129},
    {"type": "Category Four", "min": 58, "max": 155},
    {"type": "Category Five", "min": 45, "max": 120},
    {"type": "Category Six", "min": 23, "max": 99},
    {"type": "Category Seven", "min": 18, "max": 56},
    {"type": "Category Eight", "min": 18, "max": 34},
]


class TestRangeAreaChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.RANGE_AREA)
    def test_range_area_base(self):
        c = (
            RangeArea()
            .set_data(data=[opts.BaseDataOpts(values=TEST_RANGE_AREA_DATA)])
            .set_xy_field(x_field_name="type", y_field_name=["min", "max"])
            .set_range_area_spec(
                area_opts=opts.AreaOpts(style=opts.BaseStyleOpts(fill_opacity=0.15)),
            )
            .set_global_options(
                is_stack=False,
                axes_opts=[
                    opts.AxesLinearOpts(
                        base_axes_opts=opts.BaseAxesOpts(
                            orient="left",
                            label=opts.AxesLabelOpts(is_visible=True),
                        ),
                    ),
                ],
                crosshair_opts=opts.CrossHairOpts(
                    x_field=opts.CrossHairFieldOpts(is_visible=True),
                ),
            )
        )
        return c
