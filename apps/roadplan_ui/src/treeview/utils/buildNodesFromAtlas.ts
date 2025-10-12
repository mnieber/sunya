import { AtlasT } from '/src/api/types';
import { NodeT, createNode } from '/src/treeview/types';

export const buildNodesFromAtlas = (atlas: AtlasT): NodeT[] => {
  if (!atlas) return [];

  const nodes: NodeT[] = [];

  atlas.roadmaps.forEach((roadmap) => {
    const roadmapNode: NodeT = createNode({
      resource: roadmap,
      resourceType: 'roadmap',
      parentNode: undefined,
    });
    nodes.push(roadmapNode);

    roadmap.milestones?.forEach((milestone) => {
      const milestoneNode: NodeT = createNode({
        resource: milestone,
        resourceType: 'milestone',
        parentNode: roadmapNode,
      });
      nodes.push(milestoneNode);

      milestone.results?.forEach((result) => {
        const resultNode: NodeT = createNode({
          resource: result,
          resourceType: 'result',
          parentNode: milestoneNode,
        });
        nodes.push(resultNode);
      });
    });
  });

  return nodes;
};
