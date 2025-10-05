import { z } from 'zod';
import { MilestoneT } from '/src/api/types/MilestoneT';
import { EntitySchema } from '/src/api/types/EntitySchema';

export const MilestoneSchema: z.ZodType<MilestoneT> = z.object({
  ...EntitySchema.shape,
  title: z.string(),
});
