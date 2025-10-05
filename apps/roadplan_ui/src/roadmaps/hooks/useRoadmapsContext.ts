import * as R from 'ramda';
import React from 'react';
import { Highlight, Selection } from 'skandha-facets';
import { RoadmapT } from '/src/api/types';
import { RoadmapsState } from '/src/roadmaps/RoadmapsState';

export const RoadmapsContext = React.createContext<any>(null);

export const useRoadmapsContext = () => {
  const context = React.useContext(RoadmapsContext);
  if (!context) {
    throw new Error(
      'useRoadmapsContext must be used within a RoadmapsContext.Provider'
    );
  }
  return context;
};

export const roadmapsCtx = R.mergeAll([
  {
    roadmapsState: [
      useRoadmapsContext,
      'roadmapsState',
    ] as any as RoadmapsState,
    roadmaps: [useRoadmapsContext, 'roadmaps'] as any as RoadmapT[],
    roadmap: [useRoadmapsContext, 'roadmap'] as any as RoadmapT,
    roadmapsHighlight: [
      useRoadmapsContext,
      'roadmapsHighlight',
    ] as any as Highlight,
    roadmapsSelection: [
      useRoadmapsContext,
      'roadmapsSelection',
    ] as any as Selection,
  },
]);
