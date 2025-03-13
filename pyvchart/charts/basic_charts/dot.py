from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class Dot(RectChart):
    def set_dot_spec(
        self,
        name: types.Optional[str] = None,
        is_support3d: types.Optional[bool] = None,
        id_: types.Union[str, int] = None,
        data_index: types.Optional[types.Numeric] = None,
        data_id: types.Optional[str] = None,
        region_index: types.Union[int, types.Sequence[int]] = None,
        region_id: types.Union[
            int, str, types.Sequence[int], types.Sequence[str]
        ] = None,
        is_morph_enable: types.Optional[bool] = None,
        morph_key: types.Optional[str] = None,
        morph_element_key: types.Optional[str] = None,
        direction: str = "vertical",
        is_sort_data_by_axis: types.Optional[bool] = None,
        series_group_field: types.Optional[str] = None,
        dot_type_field: types.Optional[str] = None,
        title_field: types.Optional[str] = None,
        sub_title_field: types.Optional[str] = None,
        high_light_series_group: types.Optional[str] = None,
        dot_opts: types.Optional[opts.DotOpts] = None,
        title_opts: types.Optional[opts.DotTitleOpts] = None,
        sub_title_opts: types.Optional[opts.DotSubTitleOpts] = None,
        symbol_opts: types.Optional[opts.DotSymbolOpts] = None,
        grid_opts: types.Optional[opts.DotGridOpts] = None,
        left_append_padding: types.Optional[types.Numeric] = None,
        clip_height: types.Optional[types.Numeric] = None,
    ):
        self.options.update(
            {
                "type": ChartType.DOT,
                "name": name,
                "support3d": is_support3d,
                "id_": id_,
                "dataIndex": data_index,
                "dataId": data_id,
                "regionIndex": region_index,
                "regionId": region_id,
                "morph": {
                    "enable": is_morph_enable,
                    "key": morph_key,
                    "elementKey": morph_element_key,
                },
                "direction": direction,
                "sortDataByAxis": is_sort_data_by_axis,
                "seriesGroupField": series_group_field,
                "dotTypeField": dot_type_field,
                "titleField": title_field,
                "subTitleField": sub_title_field,
                "highLightSeriesGroup": high_light_series_group,
                "dot": dot_opts,
                "title": title_opts,
                "subTitle": sub_title_opts,
                "symbol": symbol_opts,
                "grid": grid_opts,
                "leftAppendPadding": left_append_padding,
                "clipHeight": clip_height,
            }
        )

        return self
