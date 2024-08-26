import { initRS } from 'mobx-resource-states';
import { EntityT } from '/src/api/types/EntityT';
import { createUUID } from '/src/utils/ids';
import { ObjT } from '/src/utils/types';

export type StepT = EntityT & {
  fact: string[];
  parentStep: StepT | null;
  childSteps: StepT[];
  fieldDeltaSetByActorKey: {
    [actor_key: string]: { [field: string]: any };
  };
};

export type StepByIdT = { [id: string]: StepT };

export const createStep = (values: ObjT): StepT => {
  return initRS({
    id: createUUID(),
    fact: values.fact ?? [],
    parentStep: values.parentStep ?? null,
    childSteps: values.childSteps ?? [],
    fieldDeltaSetByActorKey: values.fieldDeltaSetByActorKey ?? {},
  } as StepT);
};

export const getStepSequence = (leafStep: StepT): StepT[] => {
  const sequence: StepT[] = [];
  let currentStep: StepT | null = leafStep;

  while (currentStep) {
    sequence.unshift(currentStep);
    currentStep = currentStep.parentStep;
  }

  return sequence;
};
