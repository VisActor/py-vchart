from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class Area(RectChart):

    def set_3d_mode(self):
        self.add_js_funcs("VChart.register3DPlugin();")

        return self

    def set_area_spec(
        self,
        direction: str = "vertical",
        is_sort_data_by_axis: types.Optional[bool] = None,
        series_mark: str = "area",
        area_opts: types.Optional[opts.AreaOpts] = None,
        line_opts: opts.LineOpts = None,
        point_opts: opts.PointOpts = None,
        label_opts: opts.LabelOpts = None,
        area_label_opts: types.Optional[opts.LabelOpts] = None,
        total_label_opts: types.Optional[opts.LabelOpts] = None,
        sampling: types.Optional[str] = None,
        sampling_factor: types.Optional[types.Numeric] = 1,
        is_mark_overlap: types.Optional[bool] = False,
        point_dis: types.Optional[types.Numeric] = None,
        point_dis_mul: types.Optional[types.Numeric] = None,
    ):
        self.options.update(
            {
                "type": ChartType.AREA,
                "direction": direction,
                "sortDataByAxis": is_sort_data_by_axis,
                "seriesMark": series_mark,
                "area": area_opts,
                "line": line_opts,
                "point": point_opts,
                "label": label_opts,
                "areaLabel": area_label_opts,
                "totalLabel": total_label_opts,
                "sampling": sampling,
                "samplingFactor": sampling_factor,
                "markOverlap": is_mark_overlap,
                "pointDis": point_dis,
                "pointDisMul": point_dis_mul,
            }
        )

        return self
