import { makeAutoObservable } from 'mobx';
import { observer } from 'mobx-react-lite';
import { updateSources } from 'mobx-resource-states';
import React from 'react';
import { isQueryLoading } from '/src/api/lib/ObservableQuery';
import { RoadmapsContext } from '/src/roadmaps/hooks/useRoadmapsContext';
import { useRoadmapsState } from '/src/roadmaps/hooks/useRoadmapsState';
import { createGetProps } from '/src/utils/createGetProps';
import { useBuilder } from '/src/utils/hooks/useBuilder';

export type PropsT = React.PropsWithChildren<{}>;

export const RoadmapsStateProvider = observer((props: PropsT) => {
  const { roadmapsState, getRoadmaps } = useRoadmapsState({});

  const cache = useBuilder(() =>
    makeAutoObservable({
      get roadmap() {
        return updateSources(
          {
            resource: roadmapsState.roadmapsCtr.highlight.item,
            resourceName: 'roadmap',
          },
          ['loading', () => isQueryLoading(getRoadmaps), 'roadmap']
        );
      },
      get roadmaps() {
        return updateSources({ resource: roadmapsState.roadmapsCtr.data.roadmaps }, [
          'loading',
          () => isQueryLoading(getRoadmaps),
          'getRoadmaps',
        ]);
      },
    })
  );

  const getRoadmapsContext = () => {
    return createGetProps({
      roadmapsState: () => roadmapsState,
      roadmaps: () => cache.roadmaps,
      roadmap: () => cache.roadmap,
      roadmapsHighlight: () => roadmapsState.roadmapsCtr.highlight,
      roadmapsSelection: () => roadmapsState.roadmapsCtr.selection,
    });
  };

  return (
    <RoadmapsContext.Provider value={getRoadmapsContext()}>
      {props.children}
    </RoadmapsContext.Provider>
  );
});
