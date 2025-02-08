import { z } from 'zod';
import { EntitySchema } from '/src/api/types/EntitySchema';
import { ScenarioT } from '/src/api/types/ScenarioT';
import { StepSchema } from '/src/api/types/StepSchema';

export const ScenarioSchema: z.ZodType<ScenarioT> = z.object({
  ...EntitySchema.shape,
  name: z.string(),
  rootStep: StepSchema,
});
