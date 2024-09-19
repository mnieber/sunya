import { z } from 'zod';
import { EntitySchema } from '/src/api/types/EntitySchema';
import { FactBitSchema } from '/src/api/types/FactBitSchema';
import { StepT } from '/src/api/types/StepT';

export const StepSchema: z.ZodType<StepT> = z.object({
  ...EntitySchema.shape,
  fact: z.array(FactBitSchema),
  parentStepId: z.string().nullable(),
  childSteps: z.lazy(() => z.array(StepSchema)),
  fieldDeltaSetByActorKey: z.record(z.string(), z.record(z.string(), z.any())),
  preActorKeyByRoleName: z.record(z.string(), z.string()),
  postActorKeyByRoleName: z.record(z.string(), z.string()),
});
