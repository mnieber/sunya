import { initRS } from 'mobx-resource-states';
import { EntityT } from '/src/api/types/EntityT';
import { createUUID } from '/src/utils/ids';
import { ObjT } from '/src/utils/types';

export type StepT = EntityT & {
  fact: string[];
  parent_step: StepT | null;
  child_steps: StepT[];
  field_delta_set_by_actor_key: {
    [actor_key: string]: { [field: string]: any };
  };
};

export type StepByIdT = { [id: string]: StepT };

export const createStep = (values: ObjT): StepT => {
  return initRS({
    id: createUUID(),
    fact: values.fact ?? [],
    parent_step: values.parent_step ?? null,
    child_steps: values.child_steps ?? [],
    field_delta_set_by_actor_key: values.field_delta_set_by_actor_key ?? {},
  } as StepT);
};
