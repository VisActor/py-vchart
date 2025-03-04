from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class Link(RectChart):
    def set_link_spec(
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
        from_field: types.Optional[str] = None,
        to_field: types.Optional[str] = None,
        dot_series_index: types.Optional[types.Numeric] = None,
        dot_type_field: types.Optional[str] = None,
        link_opts: types.Optional[opts.LinkOpts] = None,
        arrow_opts: types.Optional[opts.ArrowOpts] = None,
    ):
        self.options.update(
            {
                "type": ChartType.LINK,
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
                "fromField": from_field,
                "toField": to_field,
                "dotSeriesIndex": dot_series_index,
                "dotTypeField": dot_type_field,
                "link": link_opts,
                "arrow": arrow_opts,
            }
        )
        return self
