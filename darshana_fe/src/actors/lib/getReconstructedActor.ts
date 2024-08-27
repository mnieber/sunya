import { ActorT } from '/src/api/types/ActorT';
import { getStepSequence, StepT } from '/src/api/types/StepT';

export const getReconstructedActor = (
  step: StepT,
  actorKey: string
): ActorT => {
  let fields = {};

  for (const currentStep of getStepSequence(step)) {
    const fieldDeltaSet = currentStep.fieldDeltaSetByActorKey[actorKey];
    if (fieldDeltaSet) {
      Object.assign(fields, fieldDeltaSet);
    }
  }

  return { key: actorKey, fields, changed_fields: [] };
};
