from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class Boxplot(RectChart):
    def set_boxplot_spec(
        self,
        direction: str = "vertical",
        is_sort_data_by_axis: types.Optional[bool] = None,
        min_field: types.Optional[str] = None,
        q1_field: types.Optional[str] = None,
        median_field: types.Optional[str] = None,
        q3_field: types.Optional[str] = None,
        max_field: types.Optional[str] = None,
        outliers_field: types.Optional[str] = None,
        boxplot_opts: types.Optional[opts.BoxplotOpts] = None,
        outliers_style_fill: types.Optional[str] = None,
        outliers_style_size: types.Optional[int] = None,
    ):
        self.options.update(
            {
                "type": ChartType.BOXPLOT,
                "direction": direction,
                "sortDataByAxis": is_sort_data_by_axis,
                "minField": min_field,
                "q1Field": q1_field,
                "medianField": median_field,
                "q3Field": q3_field,
                "maxField": max_field,
                "outliersField": outliers_field,
                "boxPlot": boxplot_opts,
                "outliersStyle": {
                    "fill": outliers_style_fill,
                    "size": outliers_style_size,
                },
            }
        )

        return self
