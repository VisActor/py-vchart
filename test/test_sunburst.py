import unittest

from pyvchart import options as opts
from pyvchart.charts import Sunburst
from pyvchart.commons.utils import JsCode
from pyvchart.globals import ChartType

from test import chart_base_test

TEST_SUNBURST_DATA = [
    {
        "name": "Country A",
        "children": [
            {
                "name": "Region1",
                "children": [
                    {"name": "Office Supplies", "value": 824},
                    {"name": "Furniture", "value": 920},
                    {"name": "Electronic equipment", "value": 936},
                ],
            },
            {
                "name": "Region2",
                "children": [
                    {"name": "Office Supplies", "value": 1270},
                    {"name": "Furniture", "value": 1399},
                    {"name": "Electronic equipment", "value": 1466},
                ],
            },
            {
                "name": "Region3",
                "children": [
                    {"name": "Office Supplies", "value": 1408},
                    {"name": "Furniture", "value": 1676},
                    {"name": "Electronic equipment", "value": 1559},
                ],
            },
            {
                "name": "Region4",
                "children": [
                    {"name": "Office Supplies", "value": 745},
                    {"name": "Furniture", "value": 919},
                    {"name": "Electronic equipment", "value": 781},
                ],
            },
            {
                "name": "Region5",
                "children": [
                    {"name": "Office Supplies", "value": 267},
                    {"name": "Furniture", "value": 316},
                    {"name": "Electronic equipment", "value": 230},
                ],
            },
            {
                "name": "Region6",
                "children": [
                    {"name": "Office Supplies", "value": 347},
                    {"name": "Furniture", "value": 501},
                    {"name": "Electronic equipment", "value": 453},
                ],
            },
        ],
    },
    {
        "name": "Country B",
        "children": [
            {
                "name": "Region1",
                "children": [
                    {"name": "Office Supplies", "value": 824},
                    {"name": "Furniture", "value": 920},
                    {"name": "Electronic equipment", "value": 936},
                ],
            },
            {
                "name": "Region2",
                "children": [
                    {"name": "Office Supplies", "value": 1270},
                    {"name": "Furniture", "value": 1399},
                    {"name": "Electronic equipment", "value": 1466},
                ],
            },
            {
                "name": "Region3",
                "children": [
                    {"name": "Office Supplies", "value": 1408},
                    {"name": "Furniture", "value": 1676},
                    {"name": "Electronic equipment", "value": 1559},
                ],
            },
            {
                "name": "Region4",
                "children": [
                    {"name": "Office Supplies", "value": 745},
                    {"name": "Furniture", "value": 919},
                    {"name": "Electronic equipment", "value": 781},
                ],
            },
            {
                "name": "Region5",
                "children": [
                    {"name": "Office Supplies", "value": 267},
                    {"name": "Furniture", "value": 316},
                    {"name": "Electronic equipment", "value": 230},
                ],
            },
            {
                "name": "Region6",
                "children": [
                    {"name": "Office Supplies", "value": 347},
                    {"name": "Furniture", "value": 501},
                    {"name": "Electronic equipment", "value": 453},
                ],
            },
        ],
    },
    {
        "name": "Country C",
        "children": [
            {
                "name": "Region1",
                "children": [
                    {"name": "Office Supplies", "value": 824},
                    {"name": "Furniture", "value": 920},
                    {"name": "Electronic equipment", "value": 936},
                ],
            },
            {
                "name": "Region2",
                "children": [
                    {"name": "Office Supplies", "value": 1270},
                    {"name": "Furniture", "value": 1399},
                    {"name": "Electronic equipment", "value": 1466},
                ],
            },
            {
                "name": "Region3",
                "children": [
                    {"name": "Office Supplies", "value": 1408},
                    {"name": "Furniture", "value": 1676},
                    {"name": "Electronic equipment", "value": 1559},
                ],
            },
            {
                "name": "Region4",
                "children": [
                    {"name": "Office Supplies", "value": 745},
                    {"name": "Furniture", "value": 919},
                    {"name": "Electronic equipment", "value": 781},
                ],
            },
            {
                "name": "Region5",
                "children": [
                    {"name": "Office Supplies", "value": 267},
                    {"name": "Furniture", "value": 316},
                    {"name": "Electronic equipment", "value": 230},
                ],
            },
            {
                "name": "Region6",
                "children": [
                    {"name": "Office Supplies", "value": 347},
                    {"name": "Furniture", "value": 501},
                    {"name": "Electronic equipment", "value": 453},
                ],
            },
        ],
    },
]


class TestSunburstChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.SUNBURST)
    def test_sunburst_base(self):
        c = (
            Sunburst()
            .set_data(data=[opts.BaseDataOpts(id_="data", values=TEST_SUNBURST_DATA)])
            .set_sunburst_spec(
                offset_x=0,
                offset_y=0,
                category_field="name",
                value_field="value",
                outer_radius=1,
                inner_radius=0,
                gap=5,
                is_drill=True,
                sunburst_opts=opts.SunburstOpts(
                    is_visible=True,
                    style=opts.BaseStyleOpts(
                        fill_opacity=JsCode(
                            "datum => { return datum.isLeaf ? 0.4 : 0.8; }"
                        ),
                    ),
                ),
                label_opts=opts.LabelOpts(
                    is_visible=True,
                    style_opts=opts.BaseStyleOpts(
                        fill_opacity=JsCode(
                            "datum => { return datum.isLeaf ? 0.4 : 0.8; }"
                        ),
                    ),
                ),
            )
            .set_global_options(
                tooltip_opts=opts.TooltipOpts(
                    mark_opts=opts.TooltipCustomOpts(
                        title_value=JsCode(
                            "val => { "
                            "return val?.datum?.map(data => data.name).join(' / '); "
                            "}",
                        ),
                    ),
                ),
                animation_enter=opts.AnimationOpts(easing="cubicInOut", duration=1000),
                animation_exit=opts.AnimationOpts(easing="cubicInOut", duration=1000),
                animation_update=opts.AnimationOpts(easing="cubicInOut", duration=1000),
            )
        )

        return c
