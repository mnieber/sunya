import { data, operation } from 'skandha';
import { NodeT } from '/src/treeview/types';
import { NodesState } from '/src/treeview/NodesState';

export class Zoom {
  static className = () => 'Zoom';

  @data isEnabled: boolean = false;

  constructor(private state: NodesState) {}

  @operation toggle(args: { mode?: boolean }) {
    if (args.mode !== undefined) {
      this.isEnabled = args.mode;
    } else {
      this.isEnabled = !this.isEnabled;
    }

    this.onToggle();
  }

  protected onToggle(): void {
    // Initialize the expansionInZoomMode by expanding all nodes that are in zoom mode
    const ctr = this.state.nodesInZoomModeCtr;
    const idsToExpand = ctr.data.nodes
      .filter((x: NodeT) => x.resourceType !== 'result')
      .map((x: NodeT) => x.id);
    for (const node of ctr.data.nodes) {
      ctr.expansion.toggle({
        itemId: node.id,
        value: idsToExpand.includes(node.id),
      });
    }
  }
}
