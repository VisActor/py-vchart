import sys
from unittest.mock import patch

from pyvchart.charts.chart import Base


class ConsoleOutputRedirect:
    """Wrapper to redirect stdout or stderr"""

    def __init__(self, fp):
        self.fp = fp

    def write(self, s):
        self.fp.write(s)

    def writelines(self, lines):
        self.fp.writelines(lines)

    def flush(self):
        self.fp.flush()


stdout_redirect = ConsoleOutputRedirect(sys.stdout)


def chart_base_test(chart_type: str):
    """decorator for chart base tests"""

    def decorator(test_func):

        @patch("pyvchart.render.engine.write_utf8_html_file")
        def wrapper(self, fake_writer):
            chart: Base = test_func(self)
            chart.render()
            _, content = fake_writer.call_args[0]

            self.assertGreater(len(content), 1000)
            self.assertEqual(chart.options.get("type"), chart_type)

            return None

        return wrapper

    return decorator
