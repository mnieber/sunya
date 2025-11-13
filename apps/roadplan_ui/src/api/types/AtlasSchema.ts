import { z } from 'zod';
import { EntitySchema } from '/src/api/types/EntitySchema';
import { RoadmapSchema } from '/src/api/types/RoadmapSchema';

export const AtlasSchema = z.object({
  ...EntitySchema.shape,
  snapshot: z.object({
    roadmaps: z.array(RoadmapSchema),
  }),
  isSyncedWithJira: z.boolean(),
  createdAt: z.coerce.date(),
});
