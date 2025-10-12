import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { atlasCtx } from '/src/atlases/hooks/useAtlasContext';
import { cn } from '/src/utils/classnames';

import './ToggleMilestonesBar.scss';

export type PropsT = {
  isTogglingCompletedMilestones: boolean;
  count: number;
  className?: any;
};

const ContextProps = {
  roadmapExpansion: atlasCtx.roadmapExpansion,
};

export const ToggleMilestonesBar = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const isExpanded = props.isTogglingCompletedMilestones
      ? props.roadmapExpansion.expandCompletedMilestones
      : props.roadmapExpansion.expandFutureMilestones;

    const label = props.isTogglingCompletedMilestones
      ? `Completed milestones (${props.count})`
      : `Future milestones (${props.count})`;

    const handleToggle = () => {
      if (props.isTogglingCompletedMilestones) {
        props.roadmapExpansion.toggleExpandCompletedMilestones({});
      } else {
        props.roadmapExpansion.toggleExpandFutureMilestones({});
      }
    };

    return (
      <div
        className={cn('ToggleMilestonesBar', props.className)}
        onClick={handleToggle}
      >
        <span className="ToggleMilestonesBar__icon">
          {isExpanded ? '▼' : '▶'}
        </span>
        <span className="ToggleMilestonesBar__label">{label}</span>
      </div>
    );
  }, ContextProps)
);
