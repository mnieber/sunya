import { initRS } from 'mobx-resource-states';
import { EntityT } from '/src/api/types/EntityT';
import { AtlasT } from '/src/api/types/AtlasT';
import { ObjT } from '/src/utils/types';
import { createUUID } from '/src/utils/ids';

export type AtlasBriefT = EntityT & {
  atlas?: AtlasT;
  isSyncedWithJira: boolean;
  createdAt: Date;
};

export type AtlasBriefByIdT = { [id: string]: AtlasBriefT };

export const createAtlasBrief = (values: ObjT): AtlasBriefT => {
  return initRS({
    createdAt: values.createdAt ?? new Date(),
    id: values.id ?? createUUID(),
    isSyncedWithJira: values.isSyncedWithJira ?? false,
  } as AtlasBriefT);
};
