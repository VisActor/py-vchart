from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType, RegisterFunctionType


class Pictogram(Chart):
    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        # register pictogram chart.
        self.add_js_funcs(RegisterFunctionType.Pictogram)

    def register_svg(self, name: str, svg_path: str):
        # hard code here
        self.add_js_funcs(f"VChart.default.registerSVG('{name}', `{svg_path}`)")

        return self

    def set_pictogram_spec(
        self,
        name_field: types.Optional[str] = None,
        value_field: types.Optional[str] = None,
        svg: types.Optional[str] = None,
        default_fill_color: types.Optional[str] = None,
        pictogram_opts: types.Optional[str] = None,
    ):
        self.options.update(
            {
                "type": ChartType.PICTOGRAM,
                "nameField": name_field,
                "valueField": value_field,
                "svg": svg,
                "defaultFillColor": default_fill_color,
                "pictogram": pictogram_opts,
            }
        )

        return self
