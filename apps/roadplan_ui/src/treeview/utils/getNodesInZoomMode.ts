import { createAtlasLut } from '/src/atlases/utils/createAtlasLut';
import { NodeT } from '/src/treeview/types';
import { AtlasT, ResultT } from '/src/api/types';
import { topologicalSort } from '/src/treeview/utils/topologicalSort';
import { isRelated } from '/src/treeview/utils/isUpstream';
import { createNode } from '/src/treeview/types';

/**
 * Get the nodes that should be visible in zoom mode.
 * This includes:
 * - The zoomed results themselves
 * - All upstream results (dependencies via parentResultIds)
 * - All downstream results (dependents - results that have zoomed results as parents)
 * - The parent milestones and roadmaps for all these results
 */
export function getNodesInZoomMode(
  atlas: AtlasT,
  zoomedResultIds: string[]
): NodeT[] {
  if (zoomedResultIds.length === 0) {
    return [];
  }

  const atlasLut = createAtlasLut(atlas);

  // Create a set of results that are in zoomedResultIds and all their upstream
  // and downstream results
  const zoomedResults: ResultT[] = [];
  let changed = true;
  while (changed) {
    changed = false;

    for (const result of Object.values(atlasLut.resultById)) {
      if (zoomedResults.includes(result)) {
        continue;
      }

      let isRelevant = zoomedResultIds.includes(result.id);
      for (const zoomedResult of zoomedResults) {
        if (
          !isRelevant &&
          isRelated(zoomedResult, result, atlasLut.resultById)
        ) {
          isRelevant = true;
        }
      }

      if (isRelevant) {
        zoomedResults.push(result);
        changed = true;
      }
    }
  }

  // Tie breaker function to sort by roadmap and milestone
  const tieBreaker = (a: ResultT, b: ResultT): number => {
    const milestoneA = atlasLut.milestoneById[a.milestoneId];
    const milestoneB = atlasLut.milestoneById[b.milestoneId];

    const roadmapAId = milestoneA.roadmapId || '';
    const roadmapBId = milestoneB.roadmapId || '';
    if (roadmapAId !== roadmapBId) {
      return roadmapAId.localeCompare(roadmapBId);
    }

    return (milestoneA.nr || 0) - (milestoneB.nr || 0);
  };

  // Sort zoomedResults topologically
  const sortedZoomedResults = topologicalSort(zoomedResults, tieBreaker);

  // Build nodes from sortedZoomedResults
  const nodes: NodeT[] = [];
  let roadmapNode: NodeT | null = null;
  let milestoneNode: NodeT | null = null;

  const countByRoadmapId: Record<string, number> = {};
  const countByMilestoneId: Record<string, number> = {};

  const bumpCount = (id: string, countById: Record<string, number>) => {
    const count = countById[id];
    if (count === undefined) {
      countById[id] = 1;
    } else {
      countById[id] = count + 1;
    }
    return countById[id];
  };

  for (const result of sortedZoomedResults) {
    const milestone = atlasLut.milestoneById[result.milestoneId];
    if (roadmapNode?.resource?.id !== milestone.roadmapId) {
      const roadmap = atlasLut.roadmapById[milestone.roadmapId];
      const count = bumpCount(roadmap.id, countByRoadmapId);

      roadmapNode = createNode({
        resource: roadmap,
        resourceType: 'roadmap',
        id: count === 1 ? roadmap.id : `${roadmap.id}_${count}`,
      });
      nodes.push(roadmapNode);
      milestoneNode = null;
    }
    if (milestoneNode?.resource?.id !== result.milestoneId) {
      const count = bumpCount(milestone.id, countByMilestoneId);

      milestoneNode = createNode({
        resource: milestone,
        resourceType: 'milestone',
        parentNode: roadmapNode,
        id: count === 1 ? milestone.id : `${milestone.id}_${count}`,
      });
      nodes.push(milestoneNode);
    }
    const resultNode = createNode({
      resource: result,
      resourceType: 'result',
      parentNode: milestoneNode,
    });
    nodes.push(resultNode);
  }

  return nodes;
}
