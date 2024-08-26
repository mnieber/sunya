import { initRS } from 'mobx-resource-states';
import { EntityT } from '/src/api/types/EntityT';
import { createUUID } from '/src/utils/ids';
import { ObjT } from '/src/utils/types';

export type ProjectEntryT = EntityT & {
  name: string;
};

export type ProjectEntryByIdT = { [id: string]: ProjectEntryT };

export const createProjectEntry = (values: ObjT): ProjectEntryT => {
  return initRS({
    id: createUUID(),
    name: values.name ?? 'New project entry',
  } as ProjectEntryT);
};
