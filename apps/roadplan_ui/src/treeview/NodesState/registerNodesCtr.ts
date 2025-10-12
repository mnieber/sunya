import * as R from 'ramda';
import { mapDataToProps } from 'skandha';
import { registerCtr } from 'skandha-mobx';
import { NodesState } from '/src/treeview/NodesState';
import { buildNodesFromAtlas } from '/src/treeview/utils/buildNodesFromAtlas';

const mapData = (state: NodesState) => {
  const ctr = state.nodesCtr;

  mapDataToProps(ctr, {
    data: {
      nodes: () => buildNodesFromAtlas(state.props.getAtlas()),
    },
    expansion: {
      expandableIds: () => R.map(R.prop('id'), ctr.data.nodes),
    },
  });
};

const setCallbacks = (state: NodesState) => {};

export const registerNodesCtr = (state: NodesState) => {
  registerCtr({
    ctr: state.nodesCtr,
    options: { name: 'NodesState.Nodes' },
    initCtr: () => {
      mapData(state);
      setCallbacks(state);
    },
  });
};
