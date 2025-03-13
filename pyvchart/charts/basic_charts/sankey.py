from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Sankey(Chart):
    def set_sankey_spec(
        self,
        node_opts: types.Optional[opts.SankeyNodeOpts] = None,
        link_opts: types.Optional[opts.SankeyLinkOpts] = None,
        category_field: types.Optional[str] = None,
        value_field: types.Optional[str] = None,
        source_field: types.Optional[str] = None,
        target_field: types.Optional[str] = None,
        direction: str = "horizontal",
        node_align: types.Optional[str] = None,
        cross_node_align: types.Optional[str] = None,
        is_inverse: types.Optional[bool] = None,
        node_gap: types.Optional[types.Numeric] = None,
        node_width: types.Optional[
            types.Union[str, types.Numeric, types.JSFunc]
        ] = None,
        link_width: types.Optional[types.Union[types.Numeric, types.JSFunc]] = None,
        min_step_width: types.Optional[types.Numeric] = None,
        min_node_height: types.Optional[types.Numeric] = None,
        max_node_height: types.Optional[types.Numeric] = None,
        min_link_height: types.Optional[types.Numeric] = None,
        max_link_height: types.Optional[types.Numeric] = None,
        iterations: types.Optional[types.Numeric] = None,
        node_key: types.Optional[types.Union[str, types.Numeric, types.JSFunc]] = None,
        link_sort_by: types.Optional[types.JSFunc] = None,
        node_sort_by: types.Optional[types.JSFunc] = None,
        set_node_layer: types.Optional[types.JSFunc] = None,
        is_drop_isolated_node: types.Optional[bool] = None,
        node_height: types.Optional[types.Union[types.Numeric, types.JSFunc]] = None,
        link_height: types.Optional[types.Union[types.Numeric, types.JSFunc]] = None,
        is_equal_node_height: types.Optional[bool] = None,
        link_overlap: types.Optional[str] = None,
        emphasis_opts: types.Optional[opts.SankeyEmphasisOpts] = None,
        overflow: types.Optional[str] = None,
        label_opts: types.Optional[opts.LabelOpts] = None,
    ):
        self.options.update(
            {
                "type": ChartType.SANKEY,
                "node": node_opts,
                "link": link_opts,
                "categoryField": category_field,
                "valueField": value_field,
                "sourceField": source_field,
                "targetField": target_field,
                "direction": direction,
                "nodeAlign": node_align,
                "crossNodeAlign": cross_node_align,
                "inverse": is_inverse,
                "nodeGap": node_gap,
                "nodeWidth": node_width,
                "linkWidth": link_width,
                "minStepWidth": min_step_width,
                "minNodeHeight": min_node_height,
                "maxNodeHeight": max_node_height,
                "minLinkHeight": min_link_height,
                "maxLinkHeight": max_link_height,
                "iterations": iterations,
                "nodeKey": node_key,
                "linkSortBy": link_sort_by,
                "nodeSortBy": node_sort_by,
                "setNodeLayer": set_node_layer,
                "dropIsolatedNode": is_drop_isolated_node,
                "nodeHeight": node_height,
                "linkHeight": link_height,
                "equalNodeHeight": is_equal_node_height,
                "linkOverlap": link_overlap,
                "emphasis": emphasis_opts,
                "overflow": overflow,
                "label": label_opts,
            }
        )

        return self
