import unittest
from unittest.mock import patch

from pyvchart import options as opts
from pyvchart.charts import Common, HeatMap
from pyvchart.commons.utils import JsCode
from pyvchart.globals import ChartType


TEST_HEATMAP_DATA = [
    {"var1": "Asset Liability Ratio", "var2": "Asset Liability Ratio", "value": 1},
    {
        "var1": "Asset Liability Ratio",
        "var2": "Asset Liability Ratio (Deducting Advance Payments)",
        "value": 0.594527,
    },
    {
        "var1": "Asset Liability Ratio",
        "var2": "Debt-to-long Capital Ratio",
        "value": 0.492963,
    },
    {
        "var1": "Asset Liability Ratio",
        "var2": "Long Term Asset Suitability Ratio",
        "value": -0.160995,
    },
    {"var1": "Asset Liability Ratio", "var2": "Equity Multiplier", "value": 0.723664},
    {
        "var1": "Asset Liability Ratio",
        "var2": "Equity Ratio of Current Liability",
        "value": 0.658646,
    },
    {
        "var1": "Asset Liability Ratio",
        "var2": "Interest Bearing Debt / Fully Invested Capital",
        "value": -0.857474,
    },
    {
        "var1": "Asset Liability Ratio",
        "var2": "Current Liability / Total Liabilities",
        "value": 0.320706,
    },
    {
        "var1": "Asset Liability Ratio",
        "var2": "Capital Fixation Ratio",
        "value": -0.284634,
    },
    {
        "var1": "Asset Liability Ratio",
        "var2": "Expected Default Frequency",
        "value": -0.091423,
    },
    {
        "var1": "Asset Liability Ratio (Deducting Advance Payments)",
        "var2": "Asset Liability Ratio",
        "value": 0.594527,
    },
    {
        "var1": "Asset Liability Ratio (Deducting Advance Payments)",
        "var2": "Asset Liability Ratio (Deducting Advance Payments)",
        "value": 1,
    },
    {
        "var1": "Asset Liability Ratio (Deducting Advance Payments)",
        "var2": "Debt-to-long Capital Ratio",
        "value": 0.724546,
    },
    {
        "var1": "Asset Liability Ratio (Deducting Advance Payments)",
        "var2": "Long Term Asset Suitability Ratio",
        "value": -0.099318,
    },
    {
        "var1": "Asset Liability Ratio (Deducting Advance Payments)",
        "var2": "Equity Multiplier",
        "value": 0.540639,
    },
    {
        "var1": "Asset Liability Ratio (Deducting Advance Payments)",
        "var2": "Equity Ratio of Current Liability",
        "value": 0.49214,
    },
    {
        "var1": "Asset Liability Ratio (Deducting Advance Payments)",
        "var2": "Interest Bearing Debt / Fully Invested Capital",
        "value": -0.554039,
    },
    {
        "var1": "Asset Liability Ratio (Deducting Advance Payments)",
        "var2": "Current Liability / Total Liabilities",
        "value": 0.17127,
    },
    {
        "var1": "Asset Liability Ratio (Deducting Advance Payments)",
        "var2": "Capital Fixation Ratio",
        "value": -0.265259,
    },
    {
        "var1": "Asset Liability Ratio (Deducting Advance Payments)",
        "var2": "Expected Default Frequency",
        "value": 0.068577,
    },
    {
        "var1": "Debt-to-long Capital Ratio",
        "var2": "Asset Liability Ratio",
        "value": 0.492963,
    },
    {
        "var1": "Debt-to-long Capital Ratio",
        "var2": "Asset Liability Ratio (Deducting Advance Payments)",
        "value": 0.724546,
    },
    {
        "var1": "Debt-to-long Capital Ratio",
        "var2": "Debt-to-long Capital Ratio",
        "value": 1,
    },
    {
        "var1": "Debt-to-long Capital Ratio",
        "var2": "Long Term Asset Suitability Ratio",
        "value": -0.091338,
    },
    {
        "var1": "Debt-to-long Capital Ratio",
        "var2": "Equity Multiplier",
        "value": 0.450542,
    },
    {
        "var1": "Debt-to-long Capital Ratio",
        "var2": "Equity Ratio of Current Liability",
        "value": 0.375839,
    },
    {
        "var1": "Debt-to-long Capital Ratio",
        "var2": "Interest Bearing Debt / Fully Invested Capital",
        "value": -0.524955,
    },
    {
        "var1": "Debt-to-long Capital Ratio",
        "var2": "Current Liability / Total Liabilities",
        "value": 0.300627,
    },
    {
        "var1": "Debt-to-long Capital Ratio",
        "var2": "Capital Fixation Ratio",
        "value": -0.198362,
    },
    {
        "var1": "Debt-to-long Capital Ratio",
        "var2": "Expected Default Frequency",
        "value": 0.033209,
    },
    {
        "var1": "Long Term Asset Suitability Ratio",
        "var2": "Asset Liability Ratio",
        "value": -0.160995,
    },
    {
        "var1": "Long Term Asset Suitability Ratio",
        "var2": "Asset Liability Ratio (Deducting Advance Payments)",
        "value": -0.099318,
    },
    {
        "var1": "Long Term Asset Suitability Ratio",
        "var2": "Debt-to-long Capital Ratio",
        "value": -0.091338,
    },
    {
        "var1": "Long Term Asset Suitability Ratio",
        "var2": "Long Term Asset Suitability Ratio",
        "value": 1,
    },
    {
        "var1": "Long Term Asset Suitability Ratio",
        "var2": "Equity Multiplier",
        "value": -0.049872,
    },
    {
        "var1": "Long Term Asset Suitability Ratio",
        "var2": "Equity Ratio of Current Liability",
        "value": -0.028452,
    },
    {
        "var1": "Long Term Asset Suitability Ratio",
        "var2": "Interest Bearing Debt / Fully Invested Capital",
        "value": 0.157157,
    },
    {
        "var1": "Long Term Asset Suitability Ratio",
        "var2": "Current Liability / Total Liabilities",
        "value": 0.009742,
    },
    {
        "var1": "Long Term Asset Suitability Ratio",
        "var2": "Capital Fixation Ratio",
        "value": -0.162374,
    },
    {
        "var1": "Long Term Asset Suitability Ratio",
        "var2": "Expected Default Frequency",
        "value": 0.155095,
    },
    {"var1": "Equity Multiplier", "var2": "Asset Liability Ratio", "value": 0.723664},
    {
        "var1": "Equity Multiplier",
        "var2": "Asset Liability Ratio (Deducting Advance Payments)",
        "value": 0.540639,
    },
    {
        "var1": "Equity Multiplier",
        "var2": "Debt-to-long Capital Ratio",
        "value": 0.450542,
    },
    {
        "var1": "Equity Multiplier",
        "var2": "Long Term Asset Suitability Ratio",
        "value": -0.049872,
    },
    {"var1": "Equity Multiplier", "var2": "Equity Multiplier", "value": 1},
    {
        "var1": "Equity Multiplier",
        "var2": "Equity Ratio of Current Liability",
        "value": 0.951933,
    },
    {
        "var1": "Equity Multiplier",
        "var2": "Interest Bearing Debt / Fully Invested Capital",
        "value": -0.651767,
    },
    {
        "var1": "Equity Multiplier",
        "var2": "Current Liability / Total Liabilities",
        "value": 0.079052,
    },
    {"var1": "Equity Multiplier", "var2": "Capital Fixation Ratio", "value": -0.535984},
    {
        "var1": "Equity Multiplier",
        "var2": "Expected Default Frequency",
        "value": 0.00798,
    },
    {
        "var1": "Equity Ratio of Current Liability",
        "var2": "Asset Liability Ratio",
        "value": 0.658646,
    },
    {
        "var1": "Equity Ratio of Current Liability",
        "var2": "Asset Liability Ratio (Deducting Advance Payments)",
        "value": 0.49214,
    },
    {
        "var1": "Equity Ratio of Current Liability",
        "var2": "Debt-to-long Capital Ratio",
        "value": 0.375839,
    },
    {
        "var1": "Equity Ratio of Current Liability",
        "var2": "Long Term Asset Suitability Ratio",
        "value": -0.028452,
    },
    {
        "var1": "Equity Ratio of Current Liability",
        "var2": "Equity Multiplier",
        "value": 0.951933,
    },
    {
        "var1": "Equity Ratio of Current Liability",
        "var2": "Equity Ratio of Current Liability",
        "value": 1,
    },
    {
        "var1": "Equity Ratio of Current Liability",
        "var2": "Interest Bearing Debt / Fully Invested Capital",
        "value": -0.543147,
    },
    {
        "var1": "Equity Ratio of Current Liability",
        "var2": "Current Liability / Total Liabilities",
        "value": -0.106139,
    },
    {
        "var1": "Equity Ratio of Current Liability",
        "var2": "Capital Fixation Ratio",
        "value": -0.52232,
    },
    {
        "var1": "Equity Ratio of Current Liability",
        "var2": "Expected Default Frequency",
        "value": 0.011466,
    },
    {
        "var1": "Interest Bearing Debt / Fully Invested Capital",
        "var2": "Asset Liability Ratio",
        "value": -0.857474,
    },
    {
        "var1": "Interest Bearing Debt / Fully Invested Capital",
        "var2": "Asset Liability Ratio (Deducting Advance Payments)",
        "value": -0.554039,
    },
    {
        "var1": "Interest Bearing Debt / Fully Invested Capital",
        "var2": "Debt-to-long Capital Ratio",
        "value": -0.524955,
    },
    {
        "var1": "Interest Bearing Debt / Fully Invested Capital",
        "var2": "Long Term Asset Suitability Ratio",
        "value": 0.157157,
    },
    {
        "var1": "Interest Bearing Debt / Fully Invested Capital",
        "var2": "Equity Multiplier",
        "value": -0.651767,
    },
    {
        "var1": "Interest Bearing Debt / Fully Invested Capital",
        "var2": "Equity Ratio of Current Liability",
        "value": -0.543147,
    },
    {
        "var1": "Interest Bearing Debt / Fully Invested Capital",
        "var2": "Interest Bearing Debt / Fully Invested Capital",
        "value": 1,
    },
    {
        "var1": "Interest Bearing Debt / Fully Invested Capital",
        "var2": "Current Liability / Total Liabilities",
        "value": -0.595016,
    },
    {
        "var1": "Interest Bearing Debt / Fully Invested Capital",
        "var2": "Capital Fixation Ratio",
        "value": 0.310521,
    },
    {
        "var1": "Interest Bearing Debt / Fully Invested Capital",
        "var2": "Expected Default Frequency",
        "value": 0.066397,
    },
    {
        "var1": "Current Liability / Total Liabilities",
        "var2": "Asset Liability Ratio",
        "value": 0.320706,
    },
    {
        "var1": "Current Liability / Total Liabilities",
        "var2": "Asset Liability Ratio (Deducting Advance Payments)",
        "value": 0.17127,
    },
    {
        "var1": "Current Liability / Total Liabilities",
        "var2": "Debt-to-long Capital Ratio",
        "value": 0.300627,
    },
    {
        "var1": "Current Liability / Total Liabilities",
        "var2": "Long Term Asset Suitability Ratio",
        "value": 0.009742,
    },
    {
        "var1": "Current Liability / Total Liabilities",
        "var2": "Equity Multiplier",
        "value": 0.079052,
    },
    {
        "var1": "Current Liability / Total Liabilities",
        "var2": "Equity Ratio of Current Liability",
        "value": -0.106139,
    },
    {
        "var1": "Current Liability / Total Liabilities",
        "var2": "Interest Bearing Debt / Fully Invested Capital",
        "value": -0.595016,
    },
    {
        "var1": "Current Liability / Total Liabilities",
        "var2": "Current Liability / Total Liabilities",
        "value": 1,
    },
    {
        "var1": "Current Liability / Total Liabilities",
        "var2": "Capital Fixation Ratio",
        "value": -0.105199,
    },
    {
        "var1": "Current Liability / Total Liabilities",
        "var2": "Expected Default Frequency",
        "value": -0.064886,
    },
    {
        "var1": "Capital Fixation Ratio",
        "var2": "Asset Liability Ratio",
        "value": -0.284634,
    },
    {
        "var1": "Capital Fixation Ratio",
        "var2": "Asset Liability Ratio (Deducting Advance Payments)",
        "value": -0.265259,
    },
    {
        "var1": "Capital Fixation Ratio",
        "var2": "Debt-to-long Capital Ratio",
        "value": -0.198362,
    },
    {
        "var1": "Capital Fixation Ratio",
        "var2": "Long Term Asset Suitability Ratio",
        "value": -0.162374,
    },
    {"var1": "Capital Fixation Ratio", "var2": "Equity Multiplier", "value": -0.535984},
    {
        "var1": "Capital Fixation Ratio",
        "var2": "Equity Ratio of Current Liability",
        "value": -0.52232,
    },
    {
        "var1": "Capital Fixation Ratio",
        "var2": "Interest Bearing Debt / Fully Invested Capital",
        "value": 0.310521,
    },
    {
        "var1": "Capital Fixation Ratio",
        "var2": "Current Liability / Total Liabilities",
        "value": -0.105199,
    },
    {"var1": "Capital Fixation Ratio", "var2": "Capital Fixation Ratio", "value": 1},
    {
        "var1": "Capital Fixation Ratio",
        "var2": "Expected Default Frequency",
        "value": -0.080153,
    },
    {
        "var1": "Expected Default Frequency",
        "var2": "Asset Liability Ratio",
        "value": -0.091423,
    },
    {
        "var1": "Expected Default Frequency",
        "var2": "Asset Liability Ratio (Deducting Advance Payments)",
        "value": 0.068577,
    },
    {
        "var1": "Expected Default Frequency",
        "var2": "Debt-to-long Capital Ratio",
        "value": 0.033209,
    },
    {
        "var1": "Expected Default Frequency",
        "var2": "Long Term Asset Suitability Ratio",
        "value": 0.155095,
    },
    {
        "var1": "Expected Default Frequency",
        "var2": "Equity Multiplier",
        "value": 0.00798,
    },
    {
        "var1": "Expected Default Frequency",
        "var2": "Equity Ratio of Current Liability",
        "value": 0.011466,
    },
    {
        "var1": "Expected Default Frequency",
        "var2": "Interest Bearing Debt / Fully Invested Capital",
        "value": 0.066397,
    },
    {
        "var1": "Expected Default Frequency",
        "var2": "Current Liability / Total Liabilities",
        "value": -0.064886,
    },
    {
        "var1": "Expected Default Frequency",
        "var2": "Capital Fixation Ratio",
        "value": -0.080153,
    },
    {
        "var1": "Expected Default Frequency",
        "var2": "Expected Default Frequency",
        "value": 1,
    },
]


def _gen_heatmap() -> dict:
    h = (
        HeatMap()
        .set_xy_field(x_field_name="var1", y_field_name="var2")
        .set_heatmap_spec(
            region_id="region0",
            value_field="value",
            cell_opts=opts.HeatMapCellOpts(
                style=opts.BaseStyleOpts(
                    fill={"field": "value", "scale": "color"},
                )
            ),
        )
    )
    return h.options


class TestHeatmapChart(unittest.TestCase):

    @patch("pyvchart.render.engine.write_utf8_html_file")
    def test_heatmap_base(self, fake_writer):
        c = (
            Common()
            .set_data(data=[opts.BaseDataOpts(id_="data0", values=TEST_HEATMAP_DATA)])
            .set_common_spec(series=[_gen_heatmap()])
            .set_global_options(
                padding_opts=12,
                region_opts=[
                    opts.RegionOpts(
                        id_="region0",
                        width=200,
                        height=200,
                        padding_opts=opts.PaddingOpts(pos_top=40),
                    )
                ],
                color_opts=opts.ColorOpts(
                    type_="linear",
                    domain=[{"dataId": "data0", "fields": ["value"]}],
                    range_=["#feedde", "#fdbe85", "#fd8d3c", "#e6550d", "#a63603"],
                ),
                axes_opts=[
                    opts.AxesBandOpts(
                        base_axes_opts=opts.BaseAxesOpts(
                            orient="bottom",
                            grid=opts.AxesGridOpts(is_visible=False),
                            domain_line=opts.AxesDomainLineOpts(is_visible=False),
                            label=opts.AxesLabelOpts(
                                space=10, style_opts=opts.BaseStyleOpts(angle=90)
                            ),
                            height=JsCode(
                                "layoutRect => { return layoutRect.height - 314; }"
                            ),
                        ),
                        band_padding=0,
                    ),
                    opts.AxesBandOpts(
                        base_axes_opts=opts.BaseAxesOpts(
                            orient="left",
                            grid=opts.AxesGridOpts(is_visible=False),
                            domain_line=opts.AxesDomainLineOpts(is_visible=False),
                            label=opts.AxesLabelOpts(space=10),
                        ),
                        band_padding=0,
                    ),
                ],
                legend_opts=opts.ColorLegendOpts(
                    base_legend_opts=opts.BaseLegendOpts(
                        is_visible=True,
                        orient="right",
                        position="start",
                        field="value",
                    )
                ),
                title_opts=opts.TitleOpts(
                    is_visible=True,
                    text="Correlation Coefficient",
                ),
            )
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertGreater(len(content), 1000)
        self.assertEqual(c.options.get("type"), ChartType.COMMON)
        self.assertEqual(c.options.get("series")[0].get("type"), ChartType.HEATMAP)
