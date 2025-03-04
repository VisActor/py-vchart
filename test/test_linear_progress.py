import unittest

from pyvchart import options as opts
from pyvchart.charts import LinearProgress
from pyvchart.globals import ChartType

from test import chart_base_test


TEST_LINEAR_PROGRESS_DATA = [
    {"type": "Tradition Industries", "value": 0.795, "text": "79.5%"},
    {"type": "Business Companies", "value": 0.25, "text": "25%"},
    {"type": "Customer-facing Companies", "value": 0.065, "text": "6.5%"},
]


class TestLinearProgressChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.LINEAR_PROGRESS)
    def test_linear_progress_base(self):
        c = (
            LinearProgress()
            .set_data(
                data=[opts.BaseDataOpts(id_="id0", values=TEST_LINEAR_PROGRESS_DATA)]
            )
            .set_xy_field(x_field_name="value", y_field_name="type")
            .set_linear_progress_spec(
                direction="horizontal",
                corner_radius=20,
                band_width=30,
            )
            .set_global_options(
                series_field="type",
                axes_opts=[
                    opts.AxesBandOpts(
                        base_axes_opts=opts.BaseAxesOpts(
                            orient="left",
                            label=opts.AxesLabelOpts(is_visible=True),
                            domain_line=opts.AxesDomainLineOpts(is_visible=False),
                            tick=opts.AxesTickOpts(is_visible=False),
                        )
                    ),
                    opts.AxesLinearOpts(
                        base_axes_opts=opts.BaseAxesOpts(
                            orient="bottom",
                            label=opts.AxesLabelOpts(is_visible=True),
                        ),
                        is_visible=False,
                    ),
                ],
            )
        )
        return c
