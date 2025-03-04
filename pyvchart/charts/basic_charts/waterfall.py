from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class Waterfall(RectChart):
    def set_waterfall_spec(
        self,
        direction: str = "vertical",
        is_sort_data_by_axis: types.Optional[bool] = None,
        bar_opts: types.Optional[opts.BarOpts] = None,
        bar_background_opts: types.Optional[opts.BarBackgroundOpts] = None,
        bar_width: types.Optional[types.Union[str, types.Numeric]] = None,
        bar_min_width: types.Optional[types.Union[str, types.Numeric]] = None,
        bar_max_width: types.Optional[types.Union[str, types.Numeric]] = None,
        total_opts: types.Optional[types.Sequence[types.WaterfallTotal]] = None,
        leader_line_opts: types.Optional[opts.WaterfallLeaderLineOpts] = None,
        stack_label_opts: types.Optional[opts.LabelOpts] = None,
        label_opts: types.Optional[opts.LabelOpts] = None,
    ):
        self.options.update(
            {
                "type": ChartType.WATERFALL,
                "direction": direction,
                "sortDataByAxis": is_sort_data_by_axis,
                "bar": bar_opts,
                "barBackground": bar_background_opts,
                "barWidth": bar_width,
                "barMinWidth": bar_min_width,
                "barMaxWidth": bar_max_width,
                "total": total_opts,
                "leaderLine": leader_line_opts,
                "stackLabel": stack_label_opts,
                "label": label_opts,
            }
        )

        return self
