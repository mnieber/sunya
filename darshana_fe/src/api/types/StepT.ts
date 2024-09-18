import { initRS } from 'mobx-resource-states';
import { EntityT } from '/src/api/types/EntityT';
import { createUUID } from '/src/utils/ids';
import { ObjT } from '/src/utils/types';

export type FactBitT = {
  typeName: 'string' | 'role' | 'actor';
  value: any;
};

export type StepT = EntityT & {
  fact: FactBitT[];
  parentStepId: string | null;
  childSteps: StepT[];
  fieldDeltaSetByActorKey: {
    [actorKey: string]: { [field: string]: any };
  };
};

export type StepByIdT = { [id: string]: StepT };

export const createStep = (values: ObjT): StepT => {
  return initRS({
    id: createUUID(),
    fact: values.fact ?? [],
    parentStepId: values.parentStepId ?? null,
    childSteps: values.childSteps ?? [],
    fieldDeltaSetByActorKey: values.fieldDeltaSetByActorKey ?? {},
  } as StepT);
};

export const getStepSequence = (
  leafStep: StepT,
  stepById: StepByIdT
): StepT[] => {
  const sequence: StepT[] = [];
  let currentStep: StepT | null = leafStep;

  while (currentStep) {
    sequence.unshift(currentStep);
    if (!currentStep.parentStepId) {
      break;
    }
    currentStep = stepById[currentStep.parentStepId];
  }

  return sequence;
};
