from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class RangeArea(RectChart):
    def set_range_area_spec(
        self,
        direction: str = "vertical",
        is_sort_data_by_axis: types.Optional[bool] = None,
        series_mark: types.Optional[str] = None,
        area_opts: types.Optional[opts.AreaOpts] = None,
        line_opts: types.Optional[opts.LineOpts] = None,
        point_opts: types.Optional[opts.PointOpts] = None,
        label_opts: types.Optional[opts.LabelOpts] = None,
        area_label_opts: types.Optional[opts.LabelOpts] = None,
        total_label_opts: types.Optional[opts.LabelOpts] = None,
        sampling: types.Optional[str] = None,
        sampling_factor: types.Optional[types.Numeric] = None,
        is_mark_overlap: types.Optional[bool] = False,
        point_dis: types.Optional[types.Numeric] = None,
        point_dis_mul: types.Optional[types.Numeric] = None,
        min_field: types.Optional[str] = None,
        max_field: types.Optional[str] = None,
    ):
        self.options.update(
            {
                "type": ChartType.RANGE_AREA,
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
                "minField": min_field,
                "maxField": max_field,
            }
        )

        return self
