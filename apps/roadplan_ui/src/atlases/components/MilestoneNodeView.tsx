import { observer } from 'mobx-react-lite';
import { MilestoneT } from '/src/api/types';
import { Expansion } from '/src/treeview/NodesState/facets/Expansion';
import { cn } from '/src/utils/classnames';

import './MilestoneNodeView.scss';

export type PropsT = {
  milestone: MilestoneT;
  nodeId: string;
  expansion: Expansion;
  className?: any;
};

export const MilestoneNodeView = observer((props: PropsT) => {
  const isExpanded = props.expansion.isExpanded(props.nodeId);
  const toggleIcon = isExpanded ? 'V' : '>';

  return (
    <div
      className={cn('MilestoneNodeView', props.className)}
      onClick={() => props.expansion.toggle({ itemId: props.nodeId })}
    >
      <span className="MilestoneNodeView__icon">{toggleIcon}</span>
      <span className="MilestoneNodeView__label">
        {false && (
          <span className="MilestoneNodeView__number">
            MS-{props.milestone.nr}
          </span>
        )}
        {false && ': '}
        {props.milestone.title}
      </span>
    </div>
  );
});
