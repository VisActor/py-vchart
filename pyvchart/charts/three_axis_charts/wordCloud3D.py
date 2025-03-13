from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class WordCloud3D(RectChart):
    def set_wordcloud3d_spec(
        self,
        direction: str = "vertical",
        is_sort_data_by_axis: types.Optional[bool] = None,
        name_field: types.Optional[str] = None,
        value_field: types.Optional[str] = None,
        font_family_field: types.Optional[str] = None,
        font_weight_field: types.Optional[str] = None,
        font_styles_field: types.Optional[str] = None,
        color_hex_field: types.Optional[str] = None,
        color_mode: types.Optional[str] = None,
        color_list: types.Optional[types.Sequence] = None,
        rotate_angles: types.Optional[types.Sequence] = None,
        font_weight_range: types.Optional[types.Sequence] = None,
        font_size_range: types.Optional[types.Union[str, types.Sequence]] = None,
        mask_shape: types.Optional[types.Union[str, types.JSFunc]] = None,
        is_random: types.Optional[bool] = None,
        wordcloud_config_opts: types.Optional[opts.WordCloudConfigOpts] = None,
        wordcloud_shape_config_opts: types.Optional[
            opts.WordCloudShapeConfigOpts
        ] = None,
        wordcloud_opts: types.Optional[opts.WordCloudOpts] = None,
        filling_word_opts: types.Optional[opts.WordCloud3DFillingWordOpts] = None,
        depth_3d: types.Optional[types.Numeric] = None,
    ):
        self.options.update(
            {
                "type": ChartType.WORDCLOUD3D,
                "direction": direction,
                "sortDataByAxis": is_sort_data_by_axis,
                "nameField": name_field,
                "valueField": value_field,
                "fontFamilyField": font_family_field,
                "fontWeightField": font_weight_field,
                "fontStylesField": font_styles_field,
                "colorHexField": color_hex_field,
                "colorMode": color_mode,
                "colorList": color_list,
                "rotateAngles": rotate_angles,
                "fontWeightRange": font_weight_range,
                "fontSizeRange": font_size_range,
                "maskShape": mask_shape,
                "random": is_random,
                "wordCloudConfig": wordcloud_config_opts,
                "wordCloudShapeConfig": wordcloud_shape_config_opts,
                "word": wordcloud_opts,
                "fillingWord": filling_word_opts,
                "depth3d": depth_3d,
            }
        )

        return self
