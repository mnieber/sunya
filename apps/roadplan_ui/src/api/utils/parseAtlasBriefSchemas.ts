import { AtlasBriefT } from '/src/api/types';
import { AtlasBriefSchema } from '/src/api/types/AtlasBriefSchema';
import { z } from 'zod';
import { createAtlasBrief } from '/src/api/types/AtlasBriefT';

export function parseAtlasBriefSchemas(
  atlasBriefSchemas: z.infer<typeof AtlasBriefSchema>[]
): AtlasBriefT[] {
  const atlasBriefs: AtlasBriefT[] = [];
  for (const atlasBriefSchema of atlasBriefSchemas) {
    const atlasBrief = createAtlasBrief({
      id: atlasBriefSchema.id,
      isSyncedWithJira: atlasBriefSchema.isSyncedWithJira,
      createdAt: atlasBriefSchema.createdAt,
    });
    atlasBriefs.push(atlasBrief);
  }
  return atlasBriefs;
}
