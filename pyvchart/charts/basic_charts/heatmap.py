from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class HeatMap(RectChart):
    def set_heatmap_spec(
        self,
        direction: str = "vertical",
        is_sort_data_by_axis: types.Optional[bool] = None,
        region_id: types.Optional[str] = None,
        value_field: types.Optional[str] = None,
        cell_opts: types.Optional[opts.HeatMapCellOpts] = None,
        cell_background_opts: types.Optional[opts.HeatMapCellBackgroundOpts] = None,
        label_opts: types.Optional[opts.LabelOpts] = None,
    ):
        self.options.update(
            {
                "type": ChartType.HEATMAP,
                "direction": direction,
                "sortDataByAxis": is_sort_data_by_axis,
                "regionId": region_id,
                "valueField": value_field,
                "cell": cell_opts,
                "cellBackground": cell_background_opts,
                "label": label_opts,
            }
        )

        return self
