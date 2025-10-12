import { initRS } from 'mobx-resource-states';
import { EntityT } from '/src/api/types/EntityT';
import { ObjT } from '/src/utils/types';

export type ResultT = EntityT & {
  name: string;
  owner?: string;
  milestoneId: string;
  parentResultIds: string[];
};

export type ResultByIdT = { [id: string]: ResultT };

export const createResult = (
  values: ObjT & { id: string; name: string }
): ResultT => {
  return initRS({
    id: values.id,
    name: values.name,
    owner: values.owner,
    milestoneId: values.milestoneId,
    parentResultIds: values.parentResultIds ?? [],
  } as ResultT);
};
