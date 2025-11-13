import { z } from 'zod';
import { EntitySchema } from '/src/api/types/EntitySchema';

export const ResultSchema = z.object({
  ...EntitySchema.shape,
  name: z.string(),
  isDone: z.boolean(),
  resultType: z.enum(['ms', 'bug', 'generic', 'meeting', 'release']),
  owner: z.string().optional(),
  parentResultNames: z.array(z.string()).optional(),
  jiraTicketUrls: z.array(z.string()).optional(),
});
