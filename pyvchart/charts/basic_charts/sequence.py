from ... import types
from ...charts.chart import Chart
from ...globals import ChartType
from .. import Bar, Dot, Link


class Sequence(Chart):
    def set_sequence_spec(
        self,
        append_padding: types.Optional[types.Numeric] = None,
        series: types.Optional[
            types.Sequence[types.Union[Bar, Dot, Link, dict]]
        ] = None,
    ):
        self.options.update(
            {
                "type": ChartType.SEQUENCE,
                "appendPadding": append_padding,
                "series": series,
            }
        )

        return self
