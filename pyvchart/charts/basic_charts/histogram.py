from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class Histogram(RectChart):
    def set_histogram_spec(
        self,
        direction: str = "vertical",
        is_sort_data_by_axis: types.Optional[bool] = None,
        bar_opts: types.Optional[opts.BarOpts] = None,
        bar_background_opts: types.Optional[opts.BarBackgroundOpts] = None,
        label_opts: types.Optional[opts.LabelOpts] = None,
        bar_width: types.Optional[types.Union[str, types.Numeric]] = None,
        bar_min_width: types.Optional[types.Union[str, types.Numeric]] = None,
        bar_max_width: types.Optional[types.Union[str, types.Numeric]] = None,
        bar_gap_in_group: types.Optional[types.Union[str, types.Numeric]] = None,
        bar_min_height: types.Optional[types.Union[str, types.Numeric]] = None,
        stack_corner_radius: types.Optional[
            types.Union[types.Numeric, types.Sequence[types.Numeric], types.JSFunc]
        ] = None,
        total_label_opts: types.Optional[opts.LabelOpts] = None,
        sampling: types.Optional[str] = None,
        sampling_factor: types.Optional[types.Numeric] = 1,
        x2_field: types.Optional[types.Union[str, types.Sequence[str]]] = None,
        y2_field: types.Optional[types.Union[str, types.Sequence[str]]] = None,
    ):
        self.options.update(
            {
                "type": ChartType.HISTOGRAM,
                "sortDataByAxis": is_sort_data_by_axis,
                "bar": bar_opts,
                "barBackground": bar_background_opts,
                "label": label_opts,
                "barWidth": bar_width,
                "barMinWidth": bar_min_width,
                "barMaxWidth": bar_max_width,
                "barGapInGroup": bar_gap_in_group,
                "barMinHeight": bar_min_height,
                "stackCornerRadius": stack_corner_radius,
                "totalLabel": total_label_opts,
                "sampling": sampling,
                "samplingFactor": sampling_factor,
                "x2Field": x2_field,
                "y2Field": y2_field,
            }
        )

        return self
