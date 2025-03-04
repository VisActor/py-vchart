import unittest

from pyvchart import options as opts
from pyvchart.charts import WordCloud3D
from pyvchart.commons.utils import JsCode
from pyvchart.globals import ChartType

from test import chart_base_test


TEST_WORDCLOUD3D_DATA = [
    {"challenge_name": "刘浩存", "sum_count": 957},
    {"challenge_name": "刘昊然", "sum_count": 942},
    {"challenge_name": "喜欢", "sum_count": 842},
    {"challenge_name": "真的", "sum_count": 828},
    {"challenge_name": "四海", "sum_count": 665},
    {"challenge_name": "好看", "sum_count": 627},
    {"challenge_name": "评论", "sum_count": 574},
    {"challenge_name": "好像", "sum_count": 564},
    {"challenge_name": "沈腾", "sum_count": 554},
    {"challenge_name": "不像", "sum_count": 540},
    {"challenge_name": "多少钱", "sum_count": 513},
    {"challenge_name": "韩寒", "sum_count": 513},
    {"challenge_name": "不知道", "sum_count": 499},
    {"challenge_name": "感觉", "sum_count": 499},
    {"challenge_name": "尹正", "sum_count": 495},
    {"challenge_name": "不看", "sum_count": 487},
    {"challenge_name": "奥特之父", "sum_count": 484},
    {"challenge_name": "阿姨", "sum_count": 482},
    {"challenge_name": "支持", "sum_count": 482},
    {"challenge_name": "父母", "sum_count": 479},
    {"challenge_name": "一条", "sum_count": 462},
    {"challenge_name": "女主", "sum_count": 456},
    {"challenge_name": "确实", "sum_count": 456},
    {"challenge_name": "票房", "sum_count": 456},
    {"challenge_name": "无语", "sum_count": 443},
    {"challenge_name": "干干净净", "sum_count": 443},
    {"challenge_name": "为啥", "sum_count": 426},
    {"challenge_name": "爱情", "sum_count": 425},
    {"challenge_name": "喜剧", "sum_count": 422},
    {"challenge_name": "春节", "sum_count": 414},
    {"challenge_name": "剧情", "sum_count": 414},
    {"challenge_name": "人生", "sum_count": 409},
    {"challenge_name": "风格", "sum_count": 408},
    {"challenge_name": "演员", "sum_count": 403},
    {"challenge_name": "成长", "sum_count": 403},
    {"challenge_name": "玩意", "sum_count": 402},
    {"challenge_name": "文学", "sum_count": 397},
]

TEST_MASK_SHAPE = "https://lf9-dp-fe-cms-tos.byteorg.com/obj/bit-cloud/log.jpeg"


class TestWordCloud3DChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.WORDCLOUD3D)
    def test_wordcloud3d_base(self):
        c = (
            WordCloud3D(
                render_opts=opts.RenderOpts(
                    is_disable_dirty_bounds=True,
                    options3d_opts=opts.Render3DOpts(is_enable=True),
                )
            )
            .set_data(
                data=[opts.BaseDataOpts(id_="data", values=TEST_WORDCLOUD3D_DATA)]
            )
            .set_wordcloud3d_spec(
                name_field="challenge_name",
                value_field="sum_count",
                mask_shape=TEST_MASK_SHAPE,
                wordcloud_opts=opts.WordCloudOpts(
                    style=opts.BaseStyleOpts(is_keep_dir_in_3d=False),
                ),
                filling_word_opts=opts.WordCloud3DFillingWordOpts(
                    style=opts.BaseStyleOpts(is_keep_dir_in_3d=False),
                ),
                depth_3d=1000,
            )
            .set_global_options(
                series_field="challenge_name",
            )
        )
        return c
