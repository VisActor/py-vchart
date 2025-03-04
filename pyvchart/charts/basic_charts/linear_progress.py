from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class LinearProgress(RectChart):
    def set_linear_progress_spec(
        self,
        direction: str = "vertical",
        is_sort_data_by_axis: types.Optional[bool] = None,
        progress_opts: types.Optional[opts.ProgressOpts] = None,
        track_opts: types.Optional[opts.TrackOpts] = None,
        corner_radius: types.Optional[types.Numeric] = None,
        band_width: types.Optional[types.Numeric] = None,
    ):
        self.options.update(
            {
                "type": ChartType.LINEAR_PROGRESS,
                "direction": direction,
                "sortDataByAxis": is_sort_data_by_axis,
                "progress": progress_opts,
                "track": track_opts,
                "cornerRadius": corner_radius,
                "bandWidth": band_width,
            }
        )

        return self
