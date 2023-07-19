import os
from IPython.core.display import HTML
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import json
import uuid

env = Environment(
    loader=FileSystemLoader(
        os.path.join(
            os.path.dirname(__file__), "templates"
        )
    ),
    autoescape=select_autoescape(['html', 'xml'])
)

colors = [
    '#009DB5',
    '#F2B823',
    '#3DA241',
    '#1F5273',
    '#EB6F02',
    '#76BEC8',
    '#D44977',
    '#EF85A7',
    '#675DAE',
    '#B6BC65',
    '#829E0B',
    '#A6A6E1',
    '#4A525F',
    '#87B7DD',
    '#A13630',
    '#CB7B48',
    '#AA7F01',
    '#E1CA56',
    '#0F7000',
    '#7C878D',
]

def _render_template(chart):
    template = env.get_template('jupyter_lab.html')
    html = template.render(chart=chart)
    return html

def vaild_json(data):
    try:
        json.dumps(data)
        return True
    except:
        return False


def render_chart(data, width="100%", height="500px", colors=colors):
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
    if(vaild_json(data)):
        chart = {}
        chart_id = uuid.uuid4().hex
        chart['chart_id'] = chart_id
        chart['data_source'] = json.dumps(data)
        chart['width'] = width
        chart['height'] = height
        chart['colors'] = colors
        return HTML(_render_template(chart))
    else:
        return 'is not a vaild json to render chart'
