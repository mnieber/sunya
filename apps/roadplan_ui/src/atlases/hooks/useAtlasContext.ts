import * as R from 'ramda';
import React from 'react';
import { Highlight, Selection } from 'skandha-facets';
import { ResultT, RoadmapT } from '/src/api/types';
import { AtlasT } from '/src/api/types/AtlasT';
import { AtlasState } from '/src/atlases/AtlasState';
import { AtlasFiltering } from '/src/atlases/AtlasState/facets/AtlasFiltering';
import { RoadmapExpansion } from '/src/atlases/AtlasState/facets/RoadmapExpansion';

export const AtlasContext = React.createContext<any>(null);

export const useAtlasContext = () => {
  const context = React.useContext(AtlasContext);
  if (!context) {
    throw new Error(
      'useAtlasContext must be used within a AtlasContext.Provider'
    );
  }
  return context;
};

export const atlasCtx = R.mergeAll([
  {
    atlasState: [useAtlasContext, 'atlasState'] as any as AtlasState,
    atlas: [useAtlasContext, 'atlas'] as any as AtlasT,
    filteredAtlas: [useAtlasContext, 'filteredAtlas'] as any as AtlasT,
    atlasFiltering: [
      useAtlasContext,
      'atlasFiltering',
    ] as any as AtlasFiltering,
    roadmaps: [useAtlasContext, 'roadmaps'] as any as RoadmapT[],
    roadmap: [useAtlasContext, 'roadmap'] as any as RoadmapT,
    roadmapsHighlight: [
      useAtlasContext,
      'roadmapsHighlight',
    ] as any as Highlight,
    roadmapExpansion: [
      useAtlasContext,
      'roadmapExpansion',
    ] as any as RoadmapExpansion,
    results: [useAtlasContext, 'results'] as any as ResultT[],
    result: [useAtlasContext, 'result'] as any as ResultT,
    resultsHighlight: [useAtlasContext, 'resultsHighlight'] as any as Highlight,
    resultsSelection: [useAtlasContext, 'resultsSelection'] as any as Selection,
  },
]);
