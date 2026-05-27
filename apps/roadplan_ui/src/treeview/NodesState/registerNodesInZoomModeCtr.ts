import * as R from 'ramda';
import { mapDataToProps } from 'skandha';
import { registerCtr } from 'skandha-mobx';
import { NodesState } from '/src/treeview/NodesState';
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

export const registerNodesInZoomModeCtr = (state: NodesState) => {
  registerCtr({
    ctr: state.nodesInZoomModeCtr,
    options: { name: 'NodesState.NodesInZoomMode' },
    initCtr: () => {
      mapData(state);
    },
  });
};
