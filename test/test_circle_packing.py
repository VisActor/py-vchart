import unittest

from pyvchart import options as opts
from pyvchart.charts import CirclePacking
from pyvchart.commons.utils import JsCode
from pyvchart.globals import ChartType

from test import chart_base_test


TEST_CIRCLE_PACKING_DATA = [
    {
        "name": "root",
        "children": [
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
        ],
    }
]


class TestCirclePackingChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.CIRCLE_PACKING)
    def test_circle_packing_base(self):
        c = (
            CirclePacking()
            .set_data(
                data=[opts.BaseDataOpts(id_="data", values=TEST_CIRCLE_PACKING_DATA)]
            )
            .set_circle_packing_spec(
                category_field="name",
                value_field="value",
                is_drill=True,
                circle_packing_opts=opts.CirclePackingOpts(
                    style=opts.BaseStyleOpts(
                        fill_opacity=JsCode("d => (d.isLeaf ? 0.75 : 0.25)")
                    )
                ),
                layout_padding=5,
                label_opts=opts.LabelOpts(
                    style_opts=opts.BaseStyleOpts(
                        is_visible=JsCode("d => { return d.depth === 1 }"),
                    )
                ),
            )
            .set_global_options(
                animation_enter=opts.AnimationOpts(easing="cubicInOut"),
                animation_exit=opts.AnimationOpts(easing="cubicInOut"),
                animation_update=opts.AnimationOpts(easing="cubicInOut"),
                tooltip_opts=opts.TooltipOpts(
                    mark_opts=opts.TooltipCustomOpts(
                        title_value=JsCode(
                            "val => { "
                            "return val?.datum?.map(data => data.name).join(' / '); "
                            "}",
                        )
                    )
                ),
            )
        )
        return c
