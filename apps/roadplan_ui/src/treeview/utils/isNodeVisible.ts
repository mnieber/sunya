import { NodeT } from '/src/treeview/types';
import { Expansion } from '/src/treeview/NodesState/facets/Expansion';

export const isNodeVisible = (node: NodeT, expansion: Expansion): boolean => {
  if (!node.parentNode) return true;

  // Check if parent is expanded
  if (!expansion.isExpanded(node.parentNode.id)) return false;

  // Recursively check if all ancestors are expanded
  return isNodeVisible(node.parentNode, expansion);
};
