import { withContextProps } from 'react-props-from-context';
import { makeAutoObservable } from 'mobx';
import { observer } from 'mobx-react-lite';
import { updateSources } from 'mobx-resource-states';
import React from 'react';
import { NodesContext } from '/src/treeview/hooks/useNodesContext';
import { useNodesState } from '/src/treeview/hooks/useNodesState';
import { createGetProps } from '/src/utils/createGetProps';
import { useBuilder } from '/src/utils/hooks/useBuilder';
import { atlasCtx } from '/src/atlases/hooks/useAtlasContext';

export type PropsT = React.PropsWithChildren<{}>;

const ContextProps = {
  filteredAtlas: atlasCtx.filteredAtlas,
  unfilteredAtlas: atlasCtx.atlas,
  resultsSelection: atlasCtx.resultsSelection,
};

export const NodesStateProvider = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const { nodesState } = useNodesState({
      getFilteredAtlas: () => props.filteredAtlas,
      getUnfilteredAtlas: () => props.unfilteredAtlas,
      getSelectedResultIds: () => props.resultsSelection.itemIds,
    });

    const cache = useBuilder(() =>
      makeAutoObservable({
        get nodes() {
          return updateSources({ resource: nodesState.nodesCtr.data.nodes });
        },
      })
    );

    const getNodesContext = () => {
      return createGetProps({
        nodesState: () => nodesState,
        nodes: () => cache.nodes,
        nodesExpansion: () => nodesState.nodesCtr.expansion,
        nodesExpansionInZoomMode: () => nodesState.nodesInZoomModeCtr.expansion,
        nodesInZoomMode: () => nodesState.nodesInZoomModeCtr.data.nodes,
        nodesZoom: () => nodesState.nodesInZoomModeCtr.zoom,
      });
    };

    return (
      <NodesContext.Provider value={getNodesContext()}>
        {props.children}
      </NodesContext.Provider>
    );
  }, ContextProps)
);
