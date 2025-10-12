import { AtlasT } from '/src/api/types/AtlasT';
import { AtlasSchema } from '/src/api/types/AtlasSchema';
import { createMilestone } from '/src/api/types/MilestoneT';
import { createResult } from '/src/api/types/ResultT';
import { createRoadmap } from '/src/api/types/RoadmapT';
import { z } from 'zod';
import { createAtlas } from '/src/api/types/AtlasT';

export function parseAtlasSchema(
  atlasSchema: z.infer<typeof AtlasSchema>
): AtlasT {
  const atlas = createAtlas({
    id: atlasSchema.id,
    isSyncedToJira: atlasSchema.isSyncedToJira,
    createdAt: atlasSchema.createdAt,
    roadmaps: [],
  });

  for (const roadmapSchema of atlasSchema.roadmaps) {
    const roadmap = createRoadmap({
      id: roadmapSchema.id,
      name: roadmapSchema.name,
      owner: roadmapSchema.owner,
      milestones: [],
    });
    atlas.roadmaps.push(roadmap);

    for (let i = 0; i < roadmapSchema.milestones.length; i++) {
      const milestoneSchema = roadmapSchema.milestones[i];
      const milestone = createMilestone({
        id: milestoneSchema.id,
        title: milestoneSchema.title,
        roadmapId: roadmap.id,
        markdownContent: milestoneSchema.markdownContent,
        results: [],
        nr: i + 1,
        isFuture: milestoneSchema.isFuture,
        isCompleted: milestoneSchema.isCompleted,
      });
      roadmap.milestones.push(milestone);

      for (const resultSchema of milestoneSchema.results) {
        const result = createResult({
          id: resultSchema.id,
          name: resultSchema.name,
          owner: resultSchema.owner,
          parentResultIds: resultSchema.parentResultIds ?? [],
          milestoneId: milestone.id,
        });
        milestone.results.push(result);
      }
    }
  }

  return atlas;
}
