import { AtlasT, MilestoneT, RoadmapT } from '/src/api/types';

export const findMilestoneAndRoadmapByResultId = (
  atlas: AtlasT,
  resultId: string
): { milestone?: MilestoneT; roadmap?: RoadmapT } => {
  if (!atlas || !resultId) {
    return {};
  }

  for (const roadmap of atlas.roadmaps) {
    if (!roadmap.milestones) continue;

    for (const milestone of roadmap.milestones) {
      if (!milestone.results) continue;

      const result = milestone.results.find((r) => r.id === resultId);
      if (result) {
        return { milestone, roadmap };
      }
    }
  }

  return {};
};
