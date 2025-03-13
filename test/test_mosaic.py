import unittest

from pyvchart import options as opts
from pyvchart.charts import Mosaic
from pyvchart.commons.utils import JsCode
from pyvchart.globals import ChartType

from test import chart_base_test


TEST_MOSAIC_DATA = [
    {"State": "WY", "Age": "Under 5 Years", "Population": 25635},
    {"State": "WY", "Age": "5 to 13 Years", "Population": 1890},
    {"State": "WY", "Age": "14 to 17 Years", "Population": 9314},
    {"State": "DC", "Age": "Under 5 Years", "Population": 30352},
    {"State": "DC", "Age": "5 to 13 Years", "Population": 20439},
    {"State": "DC", "Age": "14 to 17 Years", "Population": 10225},
    {"State": "VT", "Age": "Under 5 Years", "Population": 38253},
    {"State": "VT", "Age": "5 to 13 Years", "Population": 42538},
    {"State": "VT", "Age": "14 to 17 Years", "Population": 15757},
    {"State": "ND", "Age": "Under 5 Years", "Population": 51896},
    {"State": "ND", "Age": "5 to 13 Years", "Population": 67358},
    {"State": "ND", "Age": "14 to 17 Years", "Population": 18794},
    {"State": "AK", "Age": "Under 5 Years", "Population": 72083},
    {"State": "AK", "Age": "5 to 13 Years", "Population": 85640},
    {"State": "AK", "Age": "14 to 17 Years", "Population": 22153},
]


class TestMosaicChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.MOSAIC)
    def test_mosaic_base(self):
        c = (
            Mosaic()
            .set_data(data=[opts.BaseDataOpts(id_="barData", values=TEST_MOSAIC_DATA)])
            .set_xy_field(x_field_name="State", y_field_name="Population")
            .set_mosaic_spec(
                label_opts=[
                    opts.LabelOpts(
                        is_visible=True,
                        position="bottom",
                        style_opts=opts.BaseStyleOpts(fill="#333"),
                        filter_by_group_opts=opts.LabelFilterByGroupOpts(
                            field="State",
                            type_="min",
                        ),
                        format_method=JsCode(
                            "(value, datum, ctx) => { return datum['State']; }"
                        ),
                        overlap_opts=False,
                    ),
                    opts.LabelOpts(
                        is_visible=True,
                        position="top",
                        style_opts=opts.BaseStyleOpts(fill="#333"),
                        filter_by_group_opts=opts.LabelFilterByGroupOpts(
                            field="State",
                            type_="max",
                        ),
                        format_method=JsCode(
                            "(value, datum, ctx) => {"
                            "return `${datum['__VCHART_STACK_END']} "
                            "(${((datum['__VCHART_MOSAIC_CAT_END_PERCENT'] - "
                            "datum['__VCHART_MOSAIC_CAT_START_PERCENT']) * 100"
                            ").toFixed(0)}% )`;}"
                        ),
                        overlap_opts=False,
                    ),
                    opts.LabelOpts(
                        is_visible=True,
                        position="center",
                        smart_invert=True,
                    ),
                ]
            )
            .set_global_options(
                series_field="Age",
                is_percent=True,
                legend_opts=[opts.BaseLegendOpts(is_visible=True)],
                axes_opts=[
                    opts.BaseAxesOpts(
                        orient="left",
                        label=opts.AxesLabelOpts(
                            format_method=JsCode(
                                "val => { return `${(val * 100).toFixed(2)}%`; }",
                            ),
                        ),
                    ),
                    opts.BaseAxesOpts(
                        orient="right",
                        label=opts.AxesLabelOpts(is_visible=False),
                    ),
                ],
            )
        )
        return c
