import json
import os
import uuid
from collections.abc import Iterable

from jinja2 import Environment

from ..commons import utils
from ..datasets import EXTRA, FILENAMES
from ..globals import CurrentConfig, NotebookType, RenderSepType
from ..types import Any, Sequence, Optional
from .display import HTML, Javascript


def write_utf8_html_file(file_name: str, html_content: str):
    with open(
        file=file_name, mode="w+", encoding="utf-8", newline=RenderSepType.SepType
    ) as html_file:
        html_file.write(html_content)


class RenderEngine:
    def __init__(self, env: Optional[Environment] = None):
        self.env = env or CurrentConfig.GLOBAL_ENV

    @staticmethod
    def generate_js_link(chart: Any) -> Any:
        if not chart.js_host:
            chart.js_host = CurrentConfig.ONLINE_HOST
        links = []
        css_links = []
        for dep in chart.js_dependencies.items:
            if dep in FILENAMES:
                f, ext = FILENAMES[dep]
                _link = "{}{}.{}".format(chart.js_host, f, ext)
                links.append(_link)
                # if ext == "css":
                #     css_links.append(_link)
                # else:
                #     links.append(_link)
            else:
                for url, files in EXTRA.items():
                    if dep in files:
                        f, ext = files[dep]
                        _link = "{}{}.{}".format(url, f, ext)
                        if ext == "css":
                            css_links.append(_link)
                        else:
                            links.append(_link)
                        break
        chart.dependencies = links
        chart.css_libs = css_links
        return chart

    def render_chart_to_file(self, template_name: str, chart: Any, path: str, **kwargs):
        """
        Render a chart or page to local html files.

        :param chart: A Chart or Page object
        :param path: The destination file which the html code write to
        :param template_name: The name of template file.
        """
        tpl = self.env.get_template(template_name)
        html = utils.replace_placeholder(
            tpl.render(chart=self.generate_js_link(chart), **kwargs)
        )
        write_utf8_html_file(path, html)

    def render_chart_to_template(self, template_name: str, chart: Any, **kwargs) -> str:
        tpl = self.env.get_template(template_name)
        return utils.replace_placeholder(
            tpl.render(chart=self.generate_js_link(chart), **kwargs)
        )

    def render_chart_to_notebook(self, template_name: str, **kwargs) -> str:
        tpl = self.env.get_template(template_name)
        return utils.replace_placeholder(tpl.render(**kwargs))


def render(
    chart, path: str, template_name: str, env: Optional[Environment], **kwargs
) -> str:
    RenderEngine(env).render_chart_to_file(
        template_name=template_name, chart=chart, path=path, **kwargs
    )
    return os.path.abspath(path)


def render_embed(
    chart, template_name: str, env: Optional[Environment], **kwargs
) -> str:
    return RenderEngine(env).render_chart_to_template(
        template_name=template_name, chart=chart, **kwargs
    )


def render_notebook(self, notebook_template, lab_template):
    instance = self if isinstance(self, Iterable) else (self,)
    if CurrentConfig.NOTEBOOK_TYPE == NotebookType.JUPYTER_NOTEBOOK:
        require_config = utils.produce_require_dict(self.js_dependencies, self.js_host)
        return HTML(
            RenderEngine().render_chart_to_notebook(
                template_name=notebook_template,
                charts=instance,
                config_items=require_config["config_items"],
                libraries=require_config["libraries"],
            )
        )

    if CurrentConfig.NOTEBOOK_TYPE == NotebookType.JUPYTER_LAB:
        return HTML(
            RenderEngine().render_chart_to_notebook(
                template_name=lab_template, charts=instance
            )
        )

    if CurrentConfig.NOTEBOOK_TYPE == NotebookType.NTERACT:
        return HTML(self.render_embed())

    if CurrentConfig.NOTEBOOK_TYPE == NotebookType.ZEPPELIN:
        print("%html " + self.render_embed())


def load_javascript(chart):
    scripts = []
    for dep in chart.js_dependencies.items:
        f, ext = FILENAMES[dep]
        scripts.append("{}{}.{}".format(CurrentConfig.ONLINE_HOST, f, ext))
    return Javascript(lib=scripts)


_old_default_colors = [
    "#009DB5",
    "#F2B823",
    "#3DA241",
    "#1F5273",
    "#EB6F02",
    "#76BEC8",
    "#D44977",
    "#EF85A7",
    "#675DAE",
    "#B6BC65",
    "#829E0B",
    "#A6A6E1",
    "#4A525F",
    "#87B7DD",
    "#A13630",
    "#CB7B48",
    "#AA7F01",
    "#E1CA56",
    "#0F7000",
    "#7C878D",
]


def render_chart(
    data: dict,
    width: str = "100%",
    height: str = "500px",
    colors: Optional[Sequence[str]] = None,
):
    """ render_chart
    chart: https://github.com/VisActor/VChart
    ----------
        data: json
            is a json, which can render chart like new VChart(data, {dom: `${domId}`})
        width: string
            chart width: 100%, 500px
        height: string
            chart height: 100% 500px
        colors: list
            chart theme color
    ----------
    """
    if not colors:
        colors = _old_default_colors

    chart: dict = {
        "chart_id": uuid.uuid4().hex,
        "data_source": json.dumps(data),
        "width": width,
        "height": height,
        "colors": colors,
    }

    return HTML(
        RenderEngine().render_chart_to_notebook(
            template_name="jupyter_lab_old.html",
            chart=chart,
        )
    )
