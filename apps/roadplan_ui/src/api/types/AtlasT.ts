import { initRS } from 'mobx-resource-states';
import { EntityT } from '/src/api/types/EntityT';
import { type RoadmapT } from '/src/api/types/RoadmapT';
import { createUUID } from '/src/utils/ids';
import { ObjT } from '/src/utils/types';

export type AtlasT = EntityT & {
  createdAt: Date;
  isSyncedToJira: boolean;
  roadmaps: RoadmapT[];
};

export type AtlasByIdT = { [id: string]: AtlasT };

export const createAtlas = (values: ObjT): AtlasT => {
  return initRS({
    createdAt: values.createdAt ?? new Date(),
    id: values.id ?? createUUID(),
    isSyncedToJira: values.isSyncedToJira ?? false,
    roadmaps: values.roadmaps ?? [],
  } as AtlasT);
};
