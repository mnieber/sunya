import * as Skandha from 'skandha';
import { AtlasT } from '/src/api/types';
import { NodesData } from '/src/treeview/NodesState/facets/NodesData';
import { Expansion } from '/src/treeview/NodesState/facets/Expansion';
import { Zoom } from '/src/treeview/NodesState/facets/Zoom';
import { registerNodesCtr } from '/src/treeview/NodesState/registerNodesCtr';
import { registerNodesInZoomModeCtr } from '/src/treeview/NodesState/registerNodesInZoomModeCtr';

export type PropsT = {
  getAtlas: () => AtlasT;
  getZoomedResultIds: () => string[];
};

export class NodesState {
  props: PropsT;

  nodesCtr = {
    data: new NodesData(),
    expansion: new Expansion(),
  };

  nodesInZoomModeCtr = {
    data: new NodesData(),
    expansion: new Expansion(),
    zoom: new Zoom(),
  };

  destroy() {
    Skandha.cleanUpCtr(this);
  }

  constructor(props: PropsT) {
    this.props = props;
    registerNodesCtr(this);
    registerNodesInZoomModeCtr(this);
  }
}
