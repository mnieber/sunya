import { initRS } from 'mobx-resource-states';
import { EntityT } from '/src/api/types/EntityT';
import { createUUID } from '/src/utils/ids';
import { ObjT } from '/src/utils/types';

export type ProjectLeadT = EntityT & {
  name: string;
  description: string;
};

export type ProjectLeadByIdT = { [id: string]: ProjectLeadT };

export const createProjectLead = (values: ObjT): ProjectLeadT => {
  return initRS({
    id: createUUID(),
    name: values.name ?? 'New project entry',
  } as ProjectLeadT);
};
