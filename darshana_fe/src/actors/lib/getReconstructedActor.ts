import { ActorT } from '/src/api/types/ActorT';
import { getStepSequence, StepByIdT, StepT } from '/src/api/types/StepT';

export const getReconstructedActor = (
  step: StepT,
  actorKey: string,
  stepById: StepByIdT
): ActorT => {
  let fields = {};

  for (const currentStep of getStepSequence(step, stepById)) {
    const fieldDeltaSet = currentStep.fieldDeltaSetByActorKey[actorKey];
    if (fieldDeltaSet) {
      Object.assign(fields, fieldDeltaSet);
    }
  }

  return { key: actorKey, fields, changedFields: [] };
};
