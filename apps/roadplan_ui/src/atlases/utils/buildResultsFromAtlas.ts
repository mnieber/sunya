import { AtlasT, ResultT } from '/src/api/types';

export const buildResultsFromAtlas = (atlas: AtlasT): ResultT[] => {
  if (!atlas) return [];

  const results: ResultT[] = [];

  atlas.roadmaps.forEach((roadmap) => {
    roadmap.milestones?.forEach((milestone) => {
      milestone.results?.forEach((result) => {
        results.push(result);
      });
    });
  });

  return results;
};
