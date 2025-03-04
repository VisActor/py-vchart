from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class Line(RectChart):
    def set_line_spec(
        self,
        direction: str = "vertical",
        is_sort_data_by_axis: types.Optional[bool] = None,
        series_mark: str = "line",
        line_opts: types.Optional[opts.LineOpts] = None,
        point_opts: types.Optional[opts.PointOpts] = None,
        label_opts: types.Optional[opts.LabelOpts] = None,
        line_label_opts: types.Optional[opts.LineCurveLabelOpts] = None,
        sampling: types.Optional[str] = None,
        sampling_factor: types.Optional[types.Numeric] = 1,
        is_mark_overlap: types.Optional[bool] = False,
        point_dis: types.Optional[types.Numeric] = None,
        point_dis_mul: types.Optional[types.Numeric] = None,
    ):
        self.options.update(
            {
                "type": ChartType.LINE,
                "direction": direction,
                "sortDataByAxis": is_sort_data_by_axis,
                "seriesMark": series_mark,
                "line": line_opts,
                "point": point_opts,
                "label": label_opts,
                "lineLabel": line_label_opts,
                "sampling": sampling,
                "samplingFactor": sampling_factor,
                "markOverlap": is_mark_overlap,
                "pointDis": point_dis,
                "pointDisMul": point_dis_mul,
            }
        )

        return self
