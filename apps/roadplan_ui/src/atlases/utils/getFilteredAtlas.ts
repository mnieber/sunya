import { AtlasT, RoadmapT } from '/src/api/types';

export type FilterOptionsT = {
  showCompletedMilestones: boolean;
  showFutureMilestones: boolean;
};

/**
 * Filter the atlas based on milestone visibility settings.
 * Returns a new atlas with only the milestones that should be visible.
 * Roadmaps with no visible milestones are omitted from the result.
 */
export function getFilteredAtlas(
  atlas: AtlasT | null,
  options: FilterOptionsT
): AtlasT | null {
  if (!atlas) {
    return null;
  }

  const filteredRoadmaps: RoadmapT[] = [];

  for (const roadmap of atlas.roadmaps) {
    const visibleMilestones = roadmap.milestones.filter((milestone) => {
      if (!options.showCompletedMilestones && milestone.isCompleted) {
        return false;
      }
      if (!options.showFutureMilestones && milestone.isFuture) {
        return false;
      }
      return true;
    });

    // Only include roadmap if it has at least one visible milestone
    if (visibleMilestones.length > 0) {
      filteredRoadmaps.push({
        ...roadmap,
        milestones: visibleMilestones,
      });
    }
  }

  return {
    ...atlas,
    roadmaps: filteredRoadmaps,
  };
}
