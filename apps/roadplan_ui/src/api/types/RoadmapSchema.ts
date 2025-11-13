import { z } from 'zod';
import { EntitySchema } from '/src/api/types/EntitySchema';
import { MilestoneSchema } from '/src/api/types/MilestoneSchema';

export const RoadmapSchema = z.object({
  ...EntitySchema.shape,
  name: z.string(),
  notionUrl: z.string(),
  owner: z.string(),
  milestones: z.array(MilestoneSchema),
});
