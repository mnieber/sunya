import { initRS } from 'mobx-resource-states';
import { EntityT } from '/src/api/types/EntityT';
import { FactBitT } from '/src/api/types/FactBitT';
import { createUUID } from '/src/utils/ids';
import { ObjT } from '/src/utils/types';

export type StepT = EntityT & {
  fact: FactBitT[];
  parentStepId: string | null;
  childSteps: StepT[];
  fieldDeltaSetByActorKey: {
    [actorKey: string]: { [field: string]: any };
  };
  preActorKeyByRoleName: { [roleName: string]: string };
  postActorKeyByRoleName: { [roleName: string]: string };
};

export type StepByIdT = { [id: string]: StepT };

export const createStep = (values: ObjT): StepT => {
  return initRS({
    id: createUUID(),
    fact: values.fact ?? [],
    parentStepId: values.parentStepId ?? null,
    childSteps: values.childSteps ?? [],
    fieldDeltaSetByActorKey: values.fieldDeltaSetByActorKey ?? {},
    preActorKeyByRoleName: values.preActorKeyByRoleName ?? {},
    postActorKeyByRoleName: values.postActorKeyByRoleName ?? {},
  } as StepT);
};
