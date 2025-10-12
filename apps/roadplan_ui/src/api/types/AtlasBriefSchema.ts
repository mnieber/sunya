import { z } from 'zod';
import { EntitySchema } from '/src/api/types/EntitySchema';

export const AtlasBriefSchema = z.object({
  ...EntitySchema.shape,
  isSyncedToJira: z.boolean(),
  createdAt: z.coerce.date(),
});
