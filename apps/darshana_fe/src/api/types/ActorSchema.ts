import { z } from 'zod';
import { ActorT } from '/src/api/types/ActorT';

export const ActorSchema: z.ZodType<ActorT> = z.object({
  key: z.string(),
  fields: z.record(z.string(), z.any()),
  changedFields: z.array(z.string()),
});
