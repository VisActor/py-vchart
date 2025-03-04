import unittest

from pyvchart import options as opts
from pyvchart.charts import Bar3D
from pyvchart.globals import ChartType

from test import chart_base_test

TEST_BAR3D_DATA = [
    {"month": "Monday", "sales": 22},
    {"month": "Tuesday", "sales": 13},
    {"month": "Wednesday", "sales": 25},
    {"month": "Thursday", "sales": 29},
    {"month": "Friday", "sales": 38},
]


class TestBar3DChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.BAR3D)
    def test_bar3d_base(self):
        c = (
            Bar3D()
            .set_data(
                data=[
                    opts.BaseDataOpts(
                        id_="bar3DData",
                        values=TEST_BAR3D_DATA,
                    )
                ]
            )
            .set_bar3d_spec(
                bar3d_opts=opts.Bar3DOpts(
                    style=opts.BaseStyleOpts(
                        length=20,
                    ),
                    state=opts.BaseStateOpts(
                        selected_opts=opts.BaseStyleOpts(
                            stroke="#000",
                        ),
                    ),
                ),
            )
            .set_xy_field(x_field_name="month", y_field_name="sales")
            .set_global_options(
                axes_opts=[
                    opts.AxesBandOpts(
                        base_axes_opts=opts.BaseAxesOpts(
                            orient="bottom",
                            tick=opts.AxesTickOpts(tick_size=20),
                            mode="3d",
                        ),
                    ),
                    opts.AxesLinearOpts(
                        base_axes_opts=opts.BaseAxesOpts(
                            orient="left",
                            tick=opts.AxesTickOpts(tick_size=20),
                            mode="3d",
                        ),
                    ),
                ]
            )
        )

        return c
