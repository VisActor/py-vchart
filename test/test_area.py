import sys
import unittest
from io import StringIO
from test import stdout_redirect
from unittest.mock import patch

from pyvchart import options as opts
from pyvchart.charts import Area
from pyvchart.commons.utils import JsCode
from pyvchart.globals import CurrentConfig, NotebookType, ChartType
from pyvchart.render.display import HTML

from test import chart_base_test


TEST_AREA_DATA = [
    {"time": "2:00", "value": 8},
    {"time": "4:00", "value": 9},
    {"time": "6:00", "value": 11},
    {"time": "8:00", "value": 14},
    {"time": "10:00", "value": 16},
    {"time": "12:00", "value": 17},
    {"time": "14:00", "value": 17},
    {"time": "16:00", "value": 16},
    {"time": "18:00", "value": 15},
]


class TestAreaChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.AREA)
    def test_area_base(self):
        c = (
            Area()
            .set_area_spec()
            .set_data(data=[opts.BaseDataOpts(values=TEST_AREA_DATA)])
            .set_xy_field(
                x_field_name="time",
                y_field_name="value",
            )
        )
        return c

    @chart_base_test(chart_type=ChartType.AREA)
    def test_area3d_base(self):
        TEST_AREA3D_DATA = [
            {"type": "Nail polish", "country": "Africa", "value": 4229},
            {"type": "Nail polish", "country": "EU", "value": 4376},
            {"type": "Nail polish", "country": "China", "value": 3054},
            {"type": "Nail polish", "country": "USA", "value": 12814},
            {"type": "Eyebrow pencil", "country": "Africa", "value": 3932},
            {"type": "Eyebrow pencil", "country": "EU", "value": 3987},
            {"type": "Eyebrow pencil", "country": "China", "value": 5067},
            {"type": "Eyebrow pencil", "country": "USA", "value": 13012},
            {"type": "Rouge", "country": "Africa", "value": 5221},
            {"type": "Rouge", "country": "EU", "value": 3574},
            {"type": "Rouge", "country": "China", "value": 7004},
            {"type": "Rouge", "country": "USA", "value": 11624},
            {"type": "Lipstick", "country": "Africa", "value": 9256},
            {"type": "Lipstick", "country": "EU", "value": 4376},
            {"type": "Lipstick", "country": "China", "value": 9054},
            {"type": "Lipstick", "country": "USA", "value": 8814},
            {"type": "Eyeshadows", "country": "Africa", "value": 3308},
            {"type": "Eyeshadows", "country": "EU", "value": 4572},
            {"type": "Eyeshadows", "country": "China", "value": 12043},
            {"type": "Eyeshadows", "country": "USA", "value": 12998},
            {"type": "Eyeliner", "country": "Africa", "value": 5432},
            {"type": "Eyeliner", "country": "EU", "value": 3417},
            {"type": "Eyeliner", "country": "China", "value": 15067},
            {"type": "Eyeliner", "country": "USA", "value": 12321},
            {"type": "Foundation", "country": "Africa", "value": 13701},
            {"type": "Foundation", "country": "EU", "value": 5231},
            {"type": "Foundation", "country": "China", "value": 10119},
            {"type": "Foundation", "country": "USA", "value": 10342},
            {"type": "Lip gloss", "country": "Africa", "value": 4008},
            {"type": "Lip gloss", "country": "EU", "value": 4572},
            {"type": "Lip gloss", "country": "China", "value": 12043},
            {"type": "Lip gloss", "country": "USA", "value": 22998},
            {"type": "Mascara", "country": "Africa", "value": 18712},
            {"type": "Mascara", "country": "EU", "value": 6134},
            {"type": "Mascara", "country": "China", "value": 10419},
            {"type": "Mascara", "country": "USA", "value": 11261},
        ]

        c = (
            Area(
                render_opts=opts.RenderOpts(
                    is_disable_dirty_bounds=True,
                    options3d_opts=opts.Render3DOpts(
                        is_enable=True,
                        is_enable_view_3d_transform=True,
                        center={"x": 500, "y": 250},
                    ),
                ),
            )
            .set_3d_mode()
            .set_data(data=[opts.BaseDataOpts(values=TEST_AREA3D_DATA)])
            .set_xy_field(x_field_name="type", y_field_name="value")
            .set_z_field(field_name="country")
            .set_area_spec()
            .set_global_options(
                is_stack=False,
                series_field="country",
                legend_opts=[
                    opts.BaseLegendOpts(
                        is_visible=True, position="middle", orient="bottom"
                    )
                ],
                axes_opts=[
                    opts.BaseAxesOpts(mode="3d", orient="bottom"),
                    opts.BaseAxesOpts(mode="3d", orient="left"),
                    opts.AxesBandOpts(
                        base_axes_opts=opts.BaseAxesOpts(
                            mode="3d",
                            orient="z",
                            label=opts.AxesLabelOpts(is_visible=True),
                            grid=opts.AxesGridOpts(is_visible=True),
                            width=600,
                            height=200,
                            depth=200,
                        ),
                    ),
                ],
                crosshair_opts=opts.CrossHairOpts(
                    x_field=opts.CrossHairFieldOpts(is_visible=False)
                ),
                title_opts=opts.TitleOpts(
                    is_visible=True,
                    text="Unstacked area chart of cosmetic products sales",
                ),
            )
        )

        return c

    @patch("pyvchart.render.engine.write_utf8_html_file")
    def test_area_base_with_custom_background_image(self, fake_writer):
        c = (
            Area(
                init_opts=opts.InitOpts(
                    bg_color={
                        "type": "pattern",
                        "image": JsCode("img"),
                        "repeat": "no-repeat",
                    }
                )
            )
            .set_area_spec()
            .set_data(data=[opts.BaseDataOpts(values=TEST_AREA_DATA)])
            .set_xy_field(
                x_field_name="time",
                y_field_name="value",
            )
        )
        c.add_js_funcs(
            """
            var img = new Image(); img.src = 'https://s2.ax1x.com/2019/07/08/ZsS0fK.jpg';
            """
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("image", content)

    @patch("pyvchart.render.engine.write_utf8_html_file")
    def test_area_base_dict_config(self, fake_writer):
        c = (
            Area({"width": "100", "height": "100"})
            .set_area_spec()
            .set_data(data=[opts.BaseDataOpts(values=TEST_AREA_DATA)])
            .set_xy_field(
                x_field_name="time",
                y_field_name="value",
            )
            .set_global_options(
                title_opts={
                    "text": "Area-dict-setting",
                    "subtext": "subtext also set by dict",
                }
            )
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.width, "100")
        self.assertEqual(c.height, "100")
        self.assertIn("Area-dict-setting", content)
        self.assertIn("subtext also set by dict", content)

    @patch("pyvchart.render.engine.write_utf8_html_file")
    def test_area_title_options(self, fake_writer):
        c = (
            Area()
            .set_area_spec()
            .set_data(data=[opts.BaseDataOpts(values=TEST_AREA_DATA)])
            .set_xy_field(
                x_field_name="time",
                y_field_name="value",
            )
            .set_global_options(
                title_opts=opts.TitleOpts(
                    text="This is title.",
                    sub_text="This is subtitle.",
                    text_style_opts=opts.BaseTitleTextStyleOpts(
                        base_style_opts=opts.BaseStyleOpts(fill="white"),
                    ),
                )
            )
        )
        c.render()
        file_name, content = fake_writer.call_args[0]
        self.assertEqual("render.html", file_name)
        self.assertIn("This is title.", content)
        self.assertIn("This is subtitle.", content)
        self.assertNotIn("null", content)

    @patch("pyvchart.render.engine.write_utf8_html_file")
    def test_area_default_set_function(self, fake_writer):
        c = (
            Area()
            .set_area_spec()
            .set_data(data=[opts.BaseDataOpts(values=TEST_AREA_DATA)])
            .set_xy_field(
                x_field_name="time",
                y_field_name="value",
            )
            .set_global_options()
        )

        c.render("my_chart.html")
        file_name, content = fake_writer.call_args[0]
        self.assertEqual("my_chart.html", file_name)
        self.assertNotIn("null", content)

    @patch("pyvchart.render.engine.write_utf8_html_file")
    def test_area_custom_remote_host(self, fake_writer):
        c = (
            Area(init_opts=opts.InitOpts(js_host="http://localhost:8000/assets/"))
            .set_area_spec()
            .set_data(data=[opts.BaseDataOpts(values=TEST_AREA_DATA)])
            .set_xy_field(
                x_field_name="time",
                y_field_name="value",
            )
        )
        c.render()
        self.assertEqual(c.js_host, "http://localhost:8000/assets/")
        _, content = fake_writer.call_args[0]
        self.assertIn("http://localhost:8000/assets/index.min.js", content)

    def test_area_render_jupyter_notebook(self):
        CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_NOTEBOOK
        c = (
            Area()
            .set_area_spec()
            .set_data(data=[opts.BaseDataOpts(values=TEST_AREA_DATA)])
            .set_xy_field(
                x_field_name="time",
                y_field_name="value",
            )
        )
        nteract_code = c.render_notebook()
        self.assertEqual(isinstance(nteract_code, HTML), True)

    def test_area_render_jupyter_lab(self):
        CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB
        c = (
            Area()
            .set_area_spec()
            .set_data(data=[opts.BaseDataOpts(values=TEST_AREA_DATA)])
            .set_xy_field(
                x_field_name="time",
                y_field_name="value",
            )
        )
        nteract_code = c.render_notebook()
        self.assertEqual(isinstance(nteract_code, HTML), True)

    def test_area_render_nteract(self):
        CurrentConfig.NOTEBOOK_TYPE = NotebookType.NTERACT
        c = (
            Area()
            .set_area_spec()
            .set_data(data=[opts.BaseDataOpts(values=TEST_AREA_DATA)])
            .set_xy_field(
                x_field_name="time",
                y_field_name="value",
            )
        )
        nteract_code = c.render_notebook()
        self.assertEqual(isinstance(nteract_code, HTML), True)

    def test_area_render_zeppelin(self):
        CurrentConfig.NOTEBOOK_TYPE = NotebookType.ZEPPELIN
        c = (
            Area()
            .set_area_spec()
            .set_data(data=[opts.BaseDataOpts(values=TEST_AREA_DATA)])
            .set_xy_field(
                x_field_name="time",
                y_field_name="value",
            )
        )
        # Block Console stdout
        stdout_redirect.fp = StringIO()
        temp_stdout, sys.stdout = sys.stdout, stdout_redirect

        # render
        c.render_notebook()
        sys.stdout = temp_stdout

        # Block Result
        self.assertIn("%html", stdout_redirect.fp.getvalue())

    @patch("pyvchart.render.engine.write_utf8_html_file")
    def test_area_with_brush(self, fake_writer):
        c = (
            Area()
            .set_area_spec()
            .set_data(data=[opts.BaseDataOpts(values=TEST_AREA_DATA)])
            .set_xy_field(
                x_field_name="time",
                y_field_name="value",
            )
            .set_global_options(
                title_opts=opts.TitleOpts(text="Bar-Brush示例", sub_text="我是副标题"),
                brush_opts=opts.BrushOpts(),
            )
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("brush", content)
