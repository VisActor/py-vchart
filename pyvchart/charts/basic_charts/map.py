from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Map(Chart):
    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self._is_geo_chart = True

    def register_map(self, map_name: str, map_geojson: str):
        self.add_js_funcs(f"VChart.default.registerMap('{map_name}', {map_geojson})")

        return self

    def set_map_spec(
        self,
        map_: types.Optional[str] = None,
        name_field: types.Optional[str] = None,
        value_field: types.Optional[str] = None,
        name_property: types.Optional[str] = None,
        name_map: types.Optional[dict] = None,
        default_fill_color: types.Optional[str] = "#f3f3f3",
        centroid_property: types.Optional[str] = None,
        is_show_default_name: types.Optional[bool] = None,
        area_opts: types.Optional[opts.AreaOpts] = None,
        label_opts: types.Optional[opts.LabelOpts] = None,
        map_label_opts: types.Optional[opts.MapLabelOpts] = None,
    ):
        self.options.update(
            {
                "type": ChartType.MAP,
                "map": map_,
                "nameField": name_field,
                "valueField": value_field,
                "nameProperty": name_property,
                "nameMap": name_map,
                "defaultFillColor": default_fill_color,
                "centroidProperty": centroid_property,
                "showDefaultName": is_show_default_name,
                "area": area_opts,
                "label": label_opts,
                "mapLabel": map_label_opts,
            }
        )

        return self
