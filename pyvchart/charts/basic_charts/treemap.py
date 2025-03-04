from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Treemap(Chart):
    def set_treemap_spec(
        self,
        category_field: types.Optional[str] = None,
        value_field: types.Optional[str] = None,
        aspect_ratio: types.Optional[types.Numeric] = 1.618,
        split_type: types.Optional[str] = "binary",
        gap_width: types.Optional[
            types.Union[types.Numeric, types.Sequence[types.Numeric]]
        ] = None,
        node_padding: types.Optional[
            types.Union[types.Numeric, types.Sequence[types.Numeric]]
        ] = None,
        max_depth: types.Optional[types.Numeric] = None,
        min_visible_area: types.Optional[types.Numeric] = None,
        min_children_visible_area: types.Optional[types.Numeric] = None,
        is_roam: types.Optional[bool] = None,
        is_drill: types.Optional[bool] = None,
        drill_field: types.Optional[str] = None,
        leaf_opts: types.Optional[opts.TreeMapLeafOpts] = None,
        non_leaf_opts: types.Optional[opts.TreeMapNonLeafOpts] = None,
        label_opts: types.Optional[opts.LabelOpts] = None,
        non_leaf_label_opts: types.Optional[opts.LabelOpts] = None,
    ):
        self.options.update(
            {
                "type": ChartType.TREEMAP,
                "categoryField": category_field,
                "valueField": value_field,
                "aspectRatio": aspect_ratio,
                "splitType": split_type,
                "gapWidth": gap_width,
                "nodePadding": node_padding,
                "maxDepth": max_depth,
                "minVisibleArea": min_visible_area,
                "minChildrenVisibleArea": min_children_visible_area,
                "roam": is_roam,
                "drill": is_drill,
                "drillField": drill_field,
                "leaf": leaf_opts,
                "nonLeaf": non_leaf_opts,
                "label": label_opts,
                "nonLeafLabel": non_leaf_label_opts,
            }
        )

        return self
