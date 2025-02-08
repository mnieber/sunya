import { z } from 'zod';
import { EntitySchema } from '/src/api/types/EntitySchema';
import { ProjectT } from '/src/api/types/ProjectT';
import { ScenarioSchema } from '/src/api/types/ScenarioSchema';

export const ProjectSchema: z.ZodType<ProjectT> = z.object({
  ...EntitySchema.shape,
  name: z.string(),
  description: z.string(),
  scenarios: z.array(ScenarioSchema),
});
