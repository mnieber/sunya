import { z } from 'zod';
import { EntitySchema } from '/src/api/types/EntitySchema';
import { ResultSchema } from '/src/api/types/ResultSchema';

export const MilestoneSchema = z.object({
  ...EntitySchema.shape,
  title: z.string(),
  markdownContent: z.string(),
  results: z.array(ResultSchema),
  isFuture: z.boolean(),
  isCompleted: z.boolean(),
});
