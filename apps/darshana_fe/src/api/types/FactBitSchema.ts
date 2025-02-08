import { z } from 'zod';
import { FactBitT } from '/src/api/types/FactBitT';

export const FactBitSchema: z.ZodType<FactBitT> = z.object({
  typeName: z.enum(['string', 'role', 'actor']),
  value: z.string(),
});
