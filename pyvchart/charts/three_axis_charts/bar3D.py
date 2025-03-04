from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class Bar3D(RectChart):
    def set_bar3d_spec(
        self,
        direction: str = "vertical",
        is_sort_data_by_axis: types.Optional[bool] = None,
        bar3d_opts: types.Optional[opts.Bar3DOpts] = None,
        label_opts: opts.LabelOpts = None,
        bar_width: types.Optional[types.Union[str, types.Numeric]] = None,
        bar_min_width: types.Optional[types.Union[str, types.Numeric]] = None,
        bar_max_width: types.Optional[types.Union[str, types.Numeric]] = None,
    ):
        self.options.update(
            {
                "type": ChartType.BAR3D,
                "direction": direction,
                "sortDataByAxis": is_sort_data_by_axis,
                "bar3d": bar3d_opts,
                "label": label_opts,
                "barWidth": bar_width,
                "barMinWidth": bar_min_width,
                "barMaxWidth": bar_max_width,
            }
        )

        return self
