import { z } from 'zod';
import { EntitySchema } from '/src/api/types/EntitySchema';
import { RoadmapSchema } from '/src/api/types/RoadmapSchema';

export const AtlasSchema = z.object({
  ...EntitySchema.shape,
  roadmaps: z.array(RoadmapSchema),
  isSyncedToJira: z.boolean(),
  createdAt: z.coerce.date(),
});
