import unittest
import urllib.request

from pyvchart import options as opts
from pyvchart.charts import Map
from pyvchart.commons.utils import JsCode
from pyvchart.globals import ChartType

from test import chart_base_test


req = urllib.request.Request(
    url="https://lf9-dp-fe-cms-tos.byteorg.com/obj/bit-cloud/geojson/usa.json"
)
resp = urllib.request.urlopen(req)
map_geo_json = resp.read().decode("utf-8")


TEST_MAP_DATA = [
    {"name": "Alabama", "value": 4822023},
    {"name": "Alaska", "value": 731449},
    {"name": "Arizona", "value": 6553255},
    {"name": "Arkansas", "value": 2949131},
    {"name": "California", "value": 38041430},
    {"name": "Colorado", "value": 5187582},
    {"name": "Connecticut", "value": 3590347},
    {"name": "Delaware", "value": 917092},
    {"name": "District of Columbia", "value": 632323},
    {"name": "Florida", "value": 19317568},
    {"name": "Georgia", "value": 9919945},
    {"name": "Hawaii", "value": 1392313},
    {"name": "Idaho", "value": 1595728},
    {"name": "Illinois", "value": 12875255},
    {"name": "Indiana", "value": 6537334},
    {"name": "Iowa", "value": 3074186},
    {"name": "Kansas", "value": 2885905},
    {"name": "Kentucky", "value": 4380415},
    {"name": "Louisiana", "value": 4601893},
    {"name": "Maine", "value": 1329192},
    {"name": "Maryland", "value": 5884563},
    {"name": "Massachusetts", "value": 6646144},
    {"name": "Michigan", "value": 9883360},
    {"name": "Minnesota", "value": 5379139},
    {"name": "Mississippi", "value": 2984926},
    {"name": "Missouri", "value": 6021988},
    {"name": "Montana", "value": 1005141},
    {"name": "Nebraska", "value": 1855525},
    {"name": "Nevada", "value": 2758931},
    {"name": "New Hampshire", "value": 1320718},
    {"name": "New Jersey", "value": 8864590},
    {"name": "New Mexico", "value": 2085538},
    {"name": "New York", "value": 19570261},
    {"name": "North Carolina", "value": 9752073},
    {"name": "North Dakota", "value": 699628},
    {"name": "Ohio", "value": 11544225},
    {"name": "Oklahoma", "value": 3814820},
    {"name": "Oregon", "value": 3899353},
    {"name": "Pennsylvania", "value": 12763536},
    {"name": "Rhode Island", "value": 1050292},
    {"name": "South Carolina", "value": 4723723},
    {"name": "South Dakota", "value": 833354},
    {"name": "Tennessee", "value": 6456243},
    {"name": "Texas", "value": 26059203},
    {"name": "Utah", "value": 2855287},
    {"name": "Vermont", "value": 626011},
    {"name": "Virginia", "value": 8185867},
    {"name": "Washington", "value": 6897012},
    {"name": "West Virginia", "value": 1855413},
    {"name": "Wisconsin", "value": 5726398},
    {"name": "Wyoming", "value": 576412},
]


class TestMapChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.MAP)
    def test_map_base(self):
        c = (
            Map()
            .register_map(map_name="usa", map_geojson=map_geo_json)
            .set_data(data=[opts.BaseDataOpts(values=TEST_MAP_DATA)])
            .set_map_spec(
                map_="usa",
                name_field="name",
                value_field="value",
                name_property="name",
                area_opts=opts.AreaOpts(
                    style=opts.BaseStyleOpts(
                        fill={
                            "field": "value",
                            "scale": "color",
                            "changeDomain": "replace",
                        },
                    )
                ),
            )
            .set_global_options(
                region_opts=[
                    opts.RegionOpts(
                        roam=True,
                        projection={"type": "albersUsa"},
                    )
                ],
                legend_opts=[
                    opts.ColorLegendOpts(
                        base_legend_opts=opts.BaseLegendOpts(
                            is_visible=True,
                            field="value",
                            orient="bottom",
                            position="start",
                            title_opts=opts.LegendTitleOpts(
                                is_visible=True,
                                text="Population",
                            ),
                        ),
                    )
                ],
                title_opts=opts.TitleOpts(
                    text="USA Population Estimates (2012)",
                    sub_text="Data from www.census.gov",
                ),
                color_opts=opts.ColorOpts(
                    type_="linear",
                    range_=["rgb(252,250,97)", "rgb(252,150,134)", "rgb(87,33,15)"],
                ),
            )
        )
        return c
