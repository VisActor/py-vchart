import unittest

from pyvchart import options as opts
from pyvchart.charts import Radar
from pyvchart.globals import ChartType

from test import chart_base_test


TEST_RADAR_DATA = [
    {"key": "Strength", "value": 5},
    {"key": "Speed", "value": 5},
    {"key": "Shooting", "value": 3},
    {"key": "Endurance", "value": 5},
    {"key": "Precision", "value": 5},
    {"key": "Growth", "value": 5},
]


class TestRadarChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.RADAR)
    def test_radar_base(self):
        c = (
            Radar()
            .set_data(data=[opts.BaseDataOpts(values=TEST_RADAR_DATA)])
            .set_radar_spec(
                category_field="key",
                value_field="value",
                point_opts=opts.PointOpts(is_visible=False),
                area_opts=opts.AreaOpts(
                    is_visible=True,
                    state=opts.BaseStateOpts(
                        hover_opts=opts.BaseStyleOpts(fill_opacity=0.5)
                    ),
                ),
                line_opts=opts.LineOpts(style=opts.BaseStyleOpts(line_width=4)),
            )
            .set_global_options(
                axes_opts=[
                    opts.AxesLinearOpts(
                        min_=0,
                        max_=8,
                        base_axes_opts=opts.BaseAxesOpts(
                            orient="radius",
                            z_index=100,
                            domain_line=opts.AxesDomainLineOpts(is_visible=False),
                            label=opts.AxesLabelOpts(
                                is_visible=True,
                                space=0,
                                style_opts=opts.BaseStyleOpts(
                                    stroke="#fff",
                                    line_width=4,
                                ),
                            ),
                            grid=opts.AxesGridOpts(
                                is_smooth=False,
                                style_opts=opts.BaseStyleOpts(
                                    line_dash=[0],
                                ),
                            ),
                        ),
                    ),
                    opts.AxesBandOpts(
                        base_axes_opts=opts.BaseAxesOpts(
                            orient="angle",
                            z_index=50,
                            tick=opts.AxesTickOpts(is_visible=False),
                            domain_line=opts.AxesDomainLineOpts(is_visible=False),
                            label=opts.AxesLabelOpts(space=20),
                            grid=opts.AxesGridOpts(
                                style_opts=opts.BaseStyleOpts(
                                    line_dash=[0],
                                )
                            ),
                        ),
                    ),
                ]
            )
        )
        return c
