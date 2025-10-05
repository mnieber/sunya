import React from 'react';
import { RoadmapT } from '/src/api/types/RoadmapT';
import { ResultsState } from '/src/results/ResultsState';
import { useBuilder } from '/src/utils/hooks/useBuilder';

export type PropsT = {
  getRoadmaps: () => RoadmapT[] | undefined;
};

export const useResultsState = (props: PropsT) => {
  const resultsState = useBuilder(() => {
    const state = new ResultsState({
      //
      getResults: () => {
        // TODO: return all results from all milestones in all roadmaps
        return [];
      },
    });

    return state;
  }) as ResultsState;

  React.useEffect(() => () => resultsState.destroy(), [resultsState]);

  return {
    resultsState,
  };
};
