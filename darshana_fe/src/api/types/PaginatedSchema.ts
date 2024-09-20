import { z } from 'zod';
import { AnyZodSchema } from '/src/utils/zod';

export const getPaginatedSchema = <SchemaT extends AnyZodSchema>(
  innerSchema: SchemaT
) => {
  return z.object({
    results: z.array(innerSchema),
  });
};
