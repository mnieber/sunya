import { AtlasT } from '/src/api/types';
import { AtlasLutT } from '/src/atlases/types';

export const createAtlasLut = (atlas: AtlasT | undefined | null): AtlasLutT => {
  const resultById: Record<string, any> = {};
  const milestoneById: Record<string, any> = {};
  const roadmapById: Record<string, any> = {};

  if (!atlas) {
    return { resultById, milestoneById, roadmapById };
  }

  for (const roadmap of atlas.roadmaps) {
    roadmapById[roadmap.id] = roadmap;
    for (const milestone of roadmap.milestones) {
      milestoneById[milestone.id] = milestone;
      for (const result of milestone.results) {
        resultById[result.id] = result;
      }
    }
  }

  return { resultById, milestoneById, roadmapById };
};
