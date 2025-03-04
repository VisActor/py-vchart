import unittest
from datetime import datetime
from unittest.mock import patch

from pyvchart import options as opts
from pyvchart.charts import Bar
from pyvchart.options import InitOpts, RenderOpts
from pyvchart.globals import CurrentConfig
from pyvchart.commons.utils import JsCode
from pyvchart.charts.base import Base, default
from pyvchart.options.series_options import AnimationOpts


class TestBaseClass(unittest.TestCase):

    def test_base_add_functions(self):
        c = Base()
        c.add_js_funcs("console.log('hello')", "console.log('hello')")
        self.assertEqual(1, len(c.js_functions.items))
        self.assertEqual(["console.log('hello')"], c.js_functions.items)

    def test_base_add_events(self):
        c = Base()
        c.add_js_events("console.log('hello')", "console.log('hello')")
        self.assertEqual(1, len(c.js_events.items))
        self.assertEqual(["console.log('hello')"], c.js_events.items)

    def test_base_init_funcs(self):
        c0 = Base({"width": "100px", "height": "200px"})
        self.assertEqual(c0.width, "100px")
        self.assertEqual(c0.height, "200px")

        c1 = Base(dict(width="110px", height="210px"))
        self.assertEqual(c1.width, "110px")
        self.assertEqual(c1.height, "210px")
        self.assertNotIn(c1.js_host, ["", None])

    @patch("pyvchart.render.engine.write_utf8_html_file")
    def test_render(self, fake_writer):
        my_render_content = "my_render_content"
        bar = Bar()
        bar.set_data(data=[opts.BaseDataOpts(values=[{"x": 1, "y": 2}])])
        bar.set_xy_field(x_field_name="x", y_field_name="y")
        bar.render(my_render_content=my_render_content)
        assert "test ok" == "test ok"

    @patch("pyvchart.render.engine.write_utf8_html_file")
    def test_render_js_host_none(self, fake_writer):
        my_render_content = "my_render_content"
        bar = Bar()
        bar.set_data(data=[opts.BaseDataOpts(values=[{"x": 1, "y": 2}])])
        bar.set_xy_field(x_field_name="x", y_field_name="y")
        # Hack to test
        bar.js_host = None
        # Render
        bar.render(my_render_content=my_render_content)
        self.assertEqual(bar.js_host, CurrentConfig.ONLINE_HOST)

    @patch("pyvchart.render.engine.write_utf8_html_file")
    def test_render_embed_js(self, _):
        c = Base(init_opts=InitOpts(is_embed_js=True))
        # Embedded JavaScript
        content = c.render_embed()
        self.assertNotIn(
            CurrentConfig.ONLINE_HOST, content, "Embedding JavaScript fails"
        )
        # No embedded JavaScript
        c._embed_js = False
        content = c.render_embed()
        self.assertIn(
            CurrentConfig.ONLINE_HOST, content, "Embedded JavaScript cannot be closed"
        )

    def test_base_render_options(self):
        c0 = Base(init_opts=InitOpts(is_embed_js=True))
        self.assertEqual(c0._embed_js, True)

    def test_base_iso_format(self):
        mock_time_str = "2022-04-14 14:42:00"
        mock_time = datetime.strptime(mock_time_str, "%Y-%m-%d %H:%M:%S")
        assert default(mock_time) == "2022-04-14T14:42:00"

    def test_base_animation_option(self):
        c0 = AnimationOpts(easing="cubicInOut")
        self.assertEqual(c0.get("easing"), "cubicInOut")

        c0.update(easing=None)
        self.assertEqual(c0.get("easing"), None)

    def test_base_chart_id(self):
        c0 = Base(render_opts=RenderOpts(dom="1234567"))
        self.assertEqual(c0.chart_id, "1234567")

        c1 = Base(render_opts=RenderOpts(dom="1234567"))
        self.assertEqual(c1.get_chart_id(), "1234567")

    def test_dump_options_with_quotes(self):
        bar = Bar()
        bar.set_data(data=[opts.BaseDataOpts(values=[{"x": 1, "y": 2}])])
        bar.set_xy_field(x_field_name="x", y_field_name="y")
        bar.set_bar_spec(
            label_opts=opts.LabelOpts(
                format_method=JsCode(
                    "(value, datum, ctx) => { return datum['State']; }"
                ),
            )
        )
        formatter = """formatMethod": "(value, datum, ctx) => { return datum['State']; }"""  # noqa
        self.assertIn(formatter, bar.dump_options_with_quotes())
