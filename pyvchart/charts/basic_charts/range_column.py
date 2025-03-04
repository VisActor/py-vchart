from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class RangeColumn(RectChart):
    def set_range_column_spec(
        self,
        direction: str = "vertical",
        is_sort_data_by_axis: types.Optional[bool] = None,
        bar_opts: types.Optional[opts.BarOpts] = None,
        bar_background_opts: types.Optional[opts.BarBackgroundOpts] = None,
        label_opts: types.Optional[opts.LabelOpts] = None,
        min_field: types.Optional[str] = None,
        max_field: types.Optional[str] = None,
        bar_width: types.Optional[types.Union[str, types.Numeric]] = None,
        bar_min_width: types.Optional[types.Union[str, types.Numeric]] = None,
        bar_max_width: types.Optional[types.Union[str, types.Numeric]] = None,
        bar_gap_in_group: types.Optional[types.Union[str, types.Numeric]] = None,
        bar_min_height: types.Optional[types.Union[str, types.Numeric]] = None,
        stack_corner_radius: types.Optional[
            types.Union[types.Numeric, types.Sequence[types.Numeric], types.JSFunc]
        ] = None,
    ):
        self.options.update(
            {
                "type": ChartType.RANGE_COLUMN,
                "direction": direction,
                "sortDataByAxis": is_sort_data_by_axis,
                "bar": bar_opts,
                "barBackground": bar_background_opts,
                "label": label_opts,
                "minField": min_field,
                "maxField": max_field,
                "barWidth": bar_width,
                "barMinWidth": bar_min_width,
                "barMaxWidth": bar_max_width,
                "barGapInGroup": bar_gap_in_group,
                "barMinHeight": bar_min_height,
                "stackCornerRadius": stack_corner_radius,
            }
        )

        return self
