import { observer } from 'mobx-react-lite';
import { isLoading } from 'mobx-resource-states';
import { withContextProps } from 'react-props-from-context';
import { atlasCtx } from '/src/atlases/hooks/useAtlasContext';
import { StackedMilestonesView } from '/src/roadmaps/components/StackedMilestonesView';
import { cn } from '/src/utils/classnames';

import './RoadmapView.scss';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  roadmap: atlasCtx.roadmap,
};

export const RoadmapView = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    if (isLoading(props.roadmap)) {
      return (
        <div className={cn('RoadmapView', props.className)}>
          <div className="RoadmapView__empty">Loading...</div>
        </div>
      );
    }

    if (!props.roadmap) {
      return (
        <div className={cn('RoadmapView', props.className)}>
          <div className="RoadmapView__empty">
            Select a roadmap to view its details
          </div>
        </div>
      );
    }

    return (
      <div className={cn('RoadmapView', props.className)}>
        <div className="RoadmapView__header">
          <h1 className="RoadmapView__title">{props.roadmap.name}</h1>
        </div>
        <div className="RoadmapView__content">
          <StackedMilestonesView milestones={props.roadmap.milestones || []} />
        </div>
      </div>
    );
  }, ContextProps)
);
