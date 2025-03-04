import unittest

from pyvchart import options as opts
from pyvchart.charts import CircularProgress
from pyvchart.globals import ChartType

from test import chart_base_test


TEST_CIRCLE_PROGRESS_DATA = [
    {"type": "Tradition Industries", "value": 0.795, "text": "79.5%"},
    {"type": "Business Companies", "value": 0.25, "text": "25%"},
    {"type": "Customer-facing Companies", "value": 0.065, "text": "6.5%"},
]


class TestCircularProgressChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.CIRCULAR_PROGRESS)
    def test_circular_progress_base(self):
        c = (
            CircularProgress()
            .set_data(
                data=[opts.BaseDataOpts(id_="id0", values=TEST_CIRCLE_PROGRESS_DATA)]
            )
            .set_circular_progress_spec(
                value_field="value",
                category_field="type",
                radius=0.8,
                inner_radius=0.5,
                is_round_cap=True,
                corner_radius=20,
                progress_opts=opts.ProgressOpts(
                    style=opts.BaseStyleOpts(
                        inner_padding=5,
                        outer_padding=5,
                    )
                ),
            )
            .set_global_options(
                series_field="type",
                axes_opts=[
                    opts.AxesLinearOpts(
                        is_visible=False,
                        base_axes_opts=opts.BaseAxesOpts(orient="angle"),
                    ),
                    opts.AxesBandOpts(
                        base_axes_opts=opts.BaseAxesOpts(
                            is_visible=False, orient="radius"
                        )
                    ),
                ],
                indicator_opts=opts.IndicatorOpts(
                    is_visible=True,
                    trigger="hover",
                    title_opts=opts.IndicatorTitleOpts(
                        is_visible=True,
                        field="type",
                        is_auto_limit=True,
                        style=opts.BaseStyleOpts(font_size=20, fill="black"),
                    ),
                    content_opts=[
                        opts.IndicatorContentOpts(
                            is_visible=True,
                            field="text",
                            style=opts.BaseStyleOpts(font_size=16, fill="gray"),
                        )
                    ],
                ),
                legend_opts=opts.BaseLegendOpts(
                    is_visible=True,
                    orient="right",
                    title_opts=opts.LegendTitleOpts(is_visible=False),
                ),
            )
        )
        return c
