import { observer } from 'mobx-react-lite';
import { RoadmapT } from '/src/api/types';
import { Expansion } from '/src/treeview/NodesState/facets/Expansion';
import { cn } from '/src/utils/classnames';

import './RoadmapNodeView.scss';

export type PropsT = {
  roadmap: RoadmapT;
  nodeId: string;
  expansion: Expansion;
  className?: any;
};

export const RoadmapNodeView = observer((props: PropsT) => {
  const isExpanded = props.expansion.isExpanded(props.nodeId);
  const toggleIcon = isExpanded ? '▼' : '▶';

  return (
    <div
      className={cn('RoadmapNodeView', props.className)}
      onClick={() => props.expansion.toggle({ itemId: props.nodeId })}
    >
      <span className="RoadmapNodeView__icon">{toggleIcon}</span>
      <span className="RoadmapNodeView__label">{props.roadmap.name}</span>
    </div>
  );
});
