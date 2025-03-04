import unittest

from pyvchart import options as opts
from pyvchart.charts import Funnel3D
from pyvchart.commons.utils import JsCode
from pyvchart.globals import ChartType

from test import chart_base_test


TEST_FUNNEL3D_DATA = [
    {"value": 100, "name": "Step1"},
    {"value": 80, "name": "Step2"},
    {"value": 60, "name": "Step3"},
    {"value": 40, "name": "Step4"},
    {"value": 20, "name": "Step5"},
]


class TestFunnel3DChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.FUNNEL3D)
    def test_funnel3d_base(self):
        c = (
            Funnel3D(
                render_opts=opts.RenderOpts(
                    is_disable_dirty_bounds=True,
                    options3d_opts=opts.Render3DOpts(
                        is_enable=True,
                        center={"dx": 100, "dy": 100},
                    ),
                ),
            )
            .set_data(data=[opts.BaseDataOpts(id_="data", values=TEST_FUNNEL3D_DATA)])
            .set_funnel3d_spec(
                category_field="name",
                value_field="value",
                min_size=50,
                max_size=400,
                label_opts=opts.LabelOpts(is_visible=True, is_support3d=True),
            )
            .set_global_options(
                padding_opts=opts.PaddingOpts(pos_top=30),
                legend_opts=opts.BaseLegendOpts(is_visible=True, orient="bottom"),
            )
        )
        return c
