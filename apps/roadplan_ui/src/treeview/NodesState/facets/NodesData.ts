import * as R from 'ramda';
import { data } from 'skandha';
import { NodeT } from '/src/treeview/types';

export class NodesData {
  static className = () => 'NodesData';

  @data nodes: NodeT[] = [];

  @data get nodeById() {
    return R.indexBy(R.prop('id'), this.nodes);
  }
}
