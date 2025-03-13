from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Common(Chart):
    def set_common_spec(
        self,
        series: types.Optional[types.Sequence[dict]] = None,
        is_auto_band_size: types.Optional[bool] = None,
        label_layout: types.Optional[str] = "series",
    ):
        self.options.update(
            {
                "type": ChartType.COMMON,
                "series": series,
                "autoBandSize": is_auto_band_size,
                "labelLayout": label_layout,
            }
        )

        return self
