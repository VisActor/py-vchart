from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class Scatter(RectChart):
    def set_scatter_spec(
        self,
        label_opts: types.Optional[opts.LabelOpts] = None,
        point_opts: types.Optional[opts.PointOpts] = None,
        size_field: types.Optional[str] = None,
        size: types.Union[types.Numeric, types.Sequence, dict, types.JSFunc] = None,
        shape_field: types.Union[
            types.Numeric, types.Sequence, dict, types.JSFunc
        ] = None,
        shape: types.Union[types.Numeric, types.Sequence, dict, types.JSFunc] = None,
    ):
        self.options.update(
            {
                "type": ChartType.SCATTER,
                "label": label_opts,
                "point": point_opts,
                "sizeField": size_field,
                "size": size,
                "shapeField": shape_field,
                "shape": shape,
            }
        )

        return self
