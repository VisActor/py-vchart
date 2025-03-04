import unittest

from pyvchart import options as opts
from pyvchart.charts import Correlation
from pyvchart.globals import ChartType

from test import chart_base_test


TEST_CORRELATION_DATA = [
    {"word": "输入法哪个好用", "pv": 15952, "ratio": 94, "sim": 3932},
    {"word": "谷歌拼音输入法", "pv": 11032, "ratio": 97, "sim": 2799},
    {"word": "讯飞输入法", "pv": 107908, "ratio": 102, "sim": 2645},
    {"word": "QQ输入法", "pv": 74912, "ratio": 99, "sim": 2189},
    {"word": "百度输入法", "pv": 193624, "ratio": 121, "sim": 2100},
    {"word": "搜狗输入法", "pv": 835168, "ratio": 88, "sim": 2050},
    {"word": "谷歌输入法", "pv": 14140, "ratio": 96, "sim": 1953},
    {"word": "手心输入法", "pv": 19236, "ratio": 97, "sim": 1870},
    {"word": "输入法不见了", "pv": 1968, "ratio": 109, "sim": 1705},
    {"word": "输入法哪个最好用", "pv": 812, "ratio": 150, "sim": 1567},
    {"word": "必应输入法", "pv": 4602, "ratio": 91, "sim": 1522},
    {"word": "章鱼输入法", "pv": 18262, "ratio": 97, "sim": 1486},
    {"word": "输入法下载", "pv": 34186, "ratio": 91, "sim": 1278},
    {"word": "拼音输入法", "pv": 7186, "ratio": 86, "sim": 1009},
    {"word": "SHURUFA", "pv": 13418, "ratio": 102, "sim": 924},
    {"word": "微软输入法", "pv": 4680, "ratio": 88, "sim": 804},
    {"word": "GOOGLE输入法", "pv": 2206, "ratio": 97, "sim": 800},
    {"word": "输入法切换不出来", "pv": 15112, "ratio": 85, "sim": 764},
    {"word": "章鱼输入法下载", "pv": 8204, "ratio": 135, "sim": 754},
    {"word": "讯飞输入法下载", "pv": 5590, "ratio": 106, "sim": 609},
    {"word": "输入法搜狗", "pv": 352, "ratio": 132, "sim": 593},
    {"word": "输入法皮肤", "pv": 2476, "ratio": 103, "sim": 540},
    {"word": "紫光输入法", "pv": 1582, "ratio": 86, "sim": 538},
    {"word": "输入法设置", "pv": 1298, "ratio": 75, "sim": 527},
    {"word": "搜狗输入法下载安装", "pv": 126182, "ratio": 102, "sim": 521},
    {"word": "微软拼音输入法", "pv": 3442, "ratio": 88, "sim": 510},
    {"word": "QQ拼音输入法", "pv": 24912, "ratio": 98, "sim": 478},
    {"word": "输入发", "pv": 150, "ratio": 125, "sim": 465},
    {"word": "SOUGOU输入法", "pv": 264, "ratio": 89, "sim": 452},
    {"word": "微软拼音", "pv": 2772, "ratio": 93, "sim": 443},
]


class TestCorrelationChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.CORRELATION)
    def test_correlation_base(self):
        c = (
            Correlation()
            .set_data(data=[opts.BaseDataOpts(values=TEST_CORRELATION_DATA)])
            .set_correlation_spec(
                category_field="word",
                value_field="sim",
                size_field="pv",
                size_range=[12, 30],
                inner_radius="25%",
                outer_radius="95%",
                node_point_opts=opts.CorrelationNodePointOpts(
                    state=opts.BaseStateOpts(
                        hover_opts=opts.BaseStyleOpts(
                            line_width=8,
                            stroke_opacity=0.2,
                        ),
                    ),
                ),
                center_point_opts=opts.CorrelationCenterPointOpts(
                    state=opts.BaseStateOpts(
                        hover_opts=opts.BaseStyleOpts(
                            line_width=8,
                            stroke_opacity=0.2,
                        ),
                    ),
                ),
                center_label_opts=opts.LabelOpts(
                    is_visible=True,
                    position="center",
                    style_opts=opts.BaseStyleOpts(fill="white", text="输入法"),
                ),
                label_opts=opts.LabelOpts(
                    is_visible=True,
                    position="bottom",
                    style_opts=opts.BaseStyleOpts(fill="black"),
                ),
            )
        )
        return c
