import { NodeT } from '/src/treeview/types';
import * as R from 'ramda';
import React from 'react';
import { NodesState } from '/src/treeview/NodesState/NodesState';
import { Expansion } from '/src/treeview/NodesState/facets/Expansion';
import { Zoom } from '/src/treeview/NodesState/facets/Zoom';

export const NodesContext = React.createContext<any>(null);

export const useNodesContext = () => {
  const context = React.useContext(NodesContext);
  if (!context) {
    throw new Error(
      'useNodesContext must be used within a NodesContext.Provider'
    );
  }
  return context;
};

export const nodesCtx = R.mergeAll([
  {
    nodesState: [useNodesContext, 'nodesState'] as any as NodesState,
    nodes: [useNodesContext, 'nodes'] as any as NodeT[],
    nodesExpansion: [useNodesContext, 'nodesExpansion'] as any as Expansion,
    nodesExpansionInZoomMode: [
      useNodesContext,
      'nodesExpansionInZoomMode',
    ] as any as Expansion,
    nodesInZoomMode: [useNodesContext, 'nodesInZoomMode'] as any as NodeT[],
    nodesZoom: [useNodesContext, 'nodesZoom'] as any as Zoom,
    node: [useNodesContext, 'node'] as any as NodeT,
  },
]);
