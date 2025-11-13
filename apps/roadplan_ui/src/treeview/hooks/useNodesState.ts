import React from 'react';
import { AtlasT } from '/src/api/types';
import { NodesState } from '/src/treeview/NodesState/NodesState';
import { useBuilder } from '/src/utils/hooks/useBuilder';

export type PropsT = {
  getFilteredAtlas: () => AtlasT;
  getUnfilteredAtlas: () => AtlasT;
  getSelectedResultIds: () => string[];
};

export const useNodesState = (props: PropsT) => {
  const nodesState = useBuilder(() => {
    const state = new NodesState({
      getFilteredAtlas: () => props.getFilteredAtlas(),
      getUnfilteredAtlas: () => props.getUnfilteredAtlas(),
      //
      getZoomedResultIds: () => {
        const selectedIds = props.getSelectedResultIds();
        const allNodes = nodesState.nodesCtr.data.nodes;
        const selectedResultNames = allNodes
          .filter(
            (node) =>
              node.resourceType === 'result' && selectedIds.includes(node.id)
          )
          .map((node) => (node.resource as any).id);
        return selectedResultNames;
      },
    });

    return state;
  }) as NodesState;

  React.useEffect(() => () => nodesState.destroy(), [nodesState]);

  return {
    nodesState,
  };
};
