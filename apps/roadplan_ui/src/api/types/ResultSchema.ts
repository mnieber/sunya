import { z } from 'zod';
import { EntitySchema } from '/src/api/types/EntitySchema';

export const ResultSchema = z.object({
  ...EntitySchema.shape,
  name: z.string(),
  owner: z.string().optional(),
  parentResultIds: z.array(z.string()).optional(),
});
