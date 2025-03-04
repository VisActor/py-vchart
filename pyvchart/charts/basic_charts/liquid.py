from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType, RegisterFunctionType


class Liquid(RectChart):

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        # register liquid chart.
        self.add_js_funcs(RegisterFunctionType.Liquid)

    def set_liquid_spec(
        self,
        direction: str = "vertical",
        is_sort_data_by_axis: types.Optional[bool] = None,
        value_field: types.Optional[str] = None,
        mask_shape: types.Optional[str] = "circle",
        outline_margin: types.Optional[
            types.Union[types.JSFunc, types.Numeric, types.Sequence[types.Numeric]]
        ] = None,
        outline_padding: types.Optional[
            types.Union[types.JSFunc, types.Numeric, types.Sequence[types.Numeric]]
        ] = None,
        is_indicator_smart_invert: bool = False,
        is_reverse: bool = False,
        liquid_opts: types.Optional[opts.LiquidOpts] = None,
        liquid_background_opts: types.Optional[opts.LiquidBackgroundOpts] = None,
    ):
        self.options.update(
            {
                "type": ChartType.LIQUID,
                "direction": direction,
                "sortDataByAxis": is_sort_data_by_axis,
                "valueField": value_field,
                "maskShape": mask_shape,
                "outlineMargin": outline_margin,
                "outlinePadding": outline_padding,
                "indicatorSmartInvert": is_indicator_smart_invert,
                "reverse": is_reverse,
                "liquid": liquid_opts,
                "liquidBackground": liquid_background_opts,
            }
        )

        return self
