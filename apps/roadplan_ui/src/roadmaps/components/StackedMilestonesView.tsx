import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { MilestoneT } from '/src/api/types';
import { atlasCtx } from '/src/atlases/hooks/useAtlasContext';
import { MilestoneView } from '/src/roadmaps/components/MilestoneView';
import { ToggleMilestonesBar } from '/src/roadmaps/components/ToggleMilestonesBar';
import { cn } from '/src/utils/classnames';

import './StackedMilestonesView.scss';

export type PropsT = {
  milestones: MilestoneT[];
  className?: any;
};

const ContextProps = {
  roadmapExpansion: atlasCtx.roadmapExpansion,
};

export const StackedMilestonesView = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    // Separate milestones into categories
    const completedMilestones = props.milestones.filter((m) => m.isCompleted);
    const currentMilestones = props.milestones.filter(
      (m) => !m.isCompleted && !m.isFuture
    );
    const futureMilestones = props.milestones.filter((m) => m.isFuture);

    // Determine which milestones to show based on expansion state
    const visibleCompletedMilestones = props.roadmapExpansion
      .expandCompletedMilestones
      ? completedMilestones
      : [];

    const visibleFutureMilestones = props.roadmapExpansion.expandFutureMilestones
      ? futureMilestones
      : [];

    return (
      <div className={cn('StackedMilestonesView', props.className)}>
        {/* Completed milestones section */}
        {completedMilestones.length > 0 && (
          <>
            <ToggleMilestonesBar
              isTogglingCompletedMilestones={true}
              count={completedMilestones.length}
            />
            {visibleCompletedMilestones.map((milestone) => (
              <MilestoneView key={milestone.id} milestone={milestone} />
            ))}
          </>
        )}

        {/* Current milestones (always visible) */}
        {currentMilestones.map((milestone) => (
          <MilestoneView key={milestone.id} milestone={milestone} />
        ))}

        {/* Future milestones section */}
        {futureMilestones.length > 0 && (
          <>
            <ToggleMilestonesBar
              isTogglingCompletedMilestones={false}
              count={futureMilestones.length}
            />
            {visibleFutureMilestones.map((milestone) => (
              <MilestoneView key={milestone.id} milestone={milestone} />
            ))}
          </>
        )}
      </div>
    );
  }, ContextProps)
);
