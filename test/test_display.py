import unittest

from pyvchart.render.display import HTML, Javascript


class TestDisplay(unittest.TestCase):

    def test_display_html(self):
        html_content = "<p>hello world<p/>"
        obj = HTML(html_content)
        self.assertEqual(obj.data, html_content)
        self.assertEqual(obj.__html__(), html_content)

    def test_display_javascript(self):
        js_content = "console.log('hello world')"
        obj = Javascript(js_content)
        self.assertEqual(obj.data, js_content)
        self.assertEqual(obj._repr_javascript_(), js_content)

    def test_display_javascript_v1(self):
        js_content = "console.log('hello world')"
        obj = Javascript(js_content, lib="test lib", css="test css")
        self.assertEqual(obj.data, js_content)

        obj_1 = Javascript(
            data=js_content,
            lib=["lib1", "lib2"],
            css=["css1", "css2"],
        )
        self.assertEqual(obj_1.data, js_content)
        self.assertIn(js_content, obj_1._repr_javascript_())

    def test_display_javascript_v2(self):
        import ssl

        # ssl._create_default_https_context = ssl._create_unverified_context

        obj = Javascript(
            lib=["https://unpkg.com/@visactor/vchart@1.13.5/build/index.min.js"]
        )
        obj.load_javascript_contents()
        self.assertIn(
            "vchart",
            obj.javascript_contents[
                "https://unpkg.com/@visactor/vchart@1.13.5/build/index.min.js"
            ],
        )

        obj_1 = Javascript(lib=["https://unpkg.com/@visactor/build/index.min.js"])
        try:
            obj_1.load_javascript_contents()
        except RuntimeError:
            pass
