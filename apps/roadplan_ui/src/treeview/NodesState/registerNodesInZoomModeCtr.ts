import { NodeT } from '/src/treeview/types';
import * as R from 'ramda';
import { Cbs } from 'aspiration';
import { mapDataToProps } from 'skandha';
import { registerCtr } from 'skandha-mobx';
import { NodesState } from '/src/treeview/NodesState';
import { Zoom } from '/src/treeview/NodesState/facets/Zoom';
import { getNodesInZoomMode } from '/src/treeview/utils/getNodesInZoomMode';

const mapData = (state: NodesState) => {
  const ctr = state.nodesInZoomModeCtr;

  mapDataToProps(ctr, {
    data: {
      nodes: () =>
        ctr.zoom.isEnabled
          ? getNodesInZoomMode(
              state.props.getUnfilteredAtlas(),
              state.props.getZoomedResultIds()
            )
          : [],
    },
    expansion: {
      expandableIds: () => R.map(R.prop('id'), ctr.data.nodes),
    },
  });
};

const setCallbacks = (state: NodesState) => {
  const ctr = state.nodesInZoomModeCtr;

  ctr.zoom.callbackMap = {
    toggle: {
      exit(this: Cbs<Zoom['toggle']>) {
        // Initialize the expansionInZoomMode by expanding all nodes that are in zoom mode
        const idsToExpand = ctr.data.nodes
          .filter((x: NodeT) => x.resourceType !== 'result')
          .map((x: NodeT) => x.id);
        for (const node of ctr.data.nodes) {
          ctr.expansion.toggle({
            itemId: node.id,
            value: idsToExpand.includes(node.id),
          });
        }
      },
    },
  };
};

export const registerNodesInZoomModeCtr = (state: NodesState) => {
  registerCtr({
    ctr: state.nodesInZoomModeCtr,
    options: { name: 'NodesState.NodesInZoomMode' },
    initCtr: () => {
      mapData(state);
      setCallbacks(state);
    },
  });
};
