from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Funnel3D(Chart):
    def set_funnel3d_spec(
        self,
        category_field: types.Optional[str] = None,
        value_field: types.Optional[str] = None,
        funnel_orient: types.Optional[str] = "top",
        funnel_align: types.Optional[str] = "center",
        height_ratio: types.Optional[types.Numeric] = 0.5,
        shape: types.Optional[str] = "trapezoid",
        is_transform: types.Optional[bool] = None,
        is_cone: types.Optional[bool] = None,
        gap: types.Optional[types.Numeric] = None,
        max_size: types.Optional[types.Union[types.Numeric, str]] = "80%",
        min_size: types.Optional[types.Union[types.Numeric, str]] = None,
        funnel3d_opts: types.Optional[opts.Funnel3DOpts] = None,
        funnel3d_transform_opts: types.Optional[opts.FunnelTransformOpts] = None,
        label_opts: types.Optional[opts.LabelOpts] = None,
        transform_label_opts: types.Optional[opts.LabelOpts] = None,
        outer_label_opts: types.Optional[opts.LabelOpts] = None,
    ):
        self.options.update(
            {
                "type": ChartType.FUNNEL3D,
                "categoryField": category_field,
                "valueField": value_field,
                "funnelOrient": funnel_orient,
                "funnelAlign": funnel_align,
                "heightRatio": height_ratio,
                "shape": shape,
                "isTransform": is_transform,
                "isCone": is_cone,
                "gap": gap,
                "maxSize": max_size,
                "minSize": min_size,
                "funnel3d": funnel3d_opts,
                "transform": funnel3d_transform_opts,
                "label": label_opts,
                "transformLabel": transform_label_opts,
                "outerLabel": outer_label_opts,
            }
        )

        return self
