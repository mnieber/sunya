import React from 'react';
import { useObservableQuery } from '/src/api/hooks';
import { useGetRoadmaps } from '/src/api/queries/useGetRoadmaps';
import { RoadmapsState } from '/src/roadmaps/RoadmapsState';
import { useBuilder } from '/src/utils/hooks/useBuilder';
import { useGraftResourceStatesFromMemo } from '/src/utils/hooks/useGraftResourceStatesFromMemo';

export type PropsT = {};

export const useRoadmapsState = (props: PropsT) => {
  const graftResourceStatesFromMemo = useGraftResourceStatesFromMemo({});

  // Queries
  const getRoadmaps = useObservableQuery(useGetRoadmaps(), {
    fetchAsLoad: true,
    debugLabel: 'getRoadmaps',
  });

  const roadmapsState = useBuilder(() => {
    const state = new RoadmapsState({
      //
      getRoadmaps: () => {
        return graftResourceStatesFromMemo({
          resources: getRoadmaps.data?.roadmaps ?? [],
        });
      },
    });

    return state;
  }) as RoadmapsState;

  React.useEffect(() => () => roadmapsState.destroy(), [roadmapsState]);

  return {
    roadmapsState,
    getRoadmaps,
  };
};
