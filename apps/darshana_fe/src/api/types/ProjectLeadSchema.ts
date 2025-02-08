import { z } from 'zod';
import { EntitySchema } from '/src/api/types/EntitySchema';
import { ProjectLeadT } from '/src/api/types/ProjectLeadT';

export const ProjectLeadSchema: z.ZodType<ProjectLeadT> = z.object({
  ...EntitySchema.shape,
  name: z.string(),
  description: z.string(),
});
