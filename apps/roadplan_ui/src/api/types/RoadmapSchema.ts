import { z } from 'zod';
import { RoadmapT } from '/src/api/types/RoadmapT';
import { EntitySchema } from '/src/api/types/EntitySchema';

export const RoadmapSchema: z.ZodType<RoadmapT> = z.object({
  ...EntitySchema.shape,
  name: z.string(),
});
