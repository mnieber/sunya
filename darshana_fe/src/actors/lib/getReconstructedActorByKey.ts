import * as R from 'ramda';
import { ActorByKeyT } from '/src/api/types/ActorT';
import { StepByIdT, StepT, getStepSequence } from '/src/api/types/StepT';

export const getReconstructedActorByKey = (
  step: StepT,
  stepById: StepByIdT
): ActorByKeyT => {
  let actorByKey: ActorByKeyT = {};

  for (const factBit of step.fact) {
    if (factBit.typeName === 'actor') {
      const actorKey = factBit.value as string;
      actorByKey[actorKey] = { key: actorKey, fields: {}, changedFields: [] };
    }
  }

  for (const currentStep of getStepSequence(step, stepById)) {
    for (const actorKey of R.keys(actorByKey)) {
      const actor = actorByKey[actorKey];

      const fieldDeltaSet = currentStep.fieldDeltaSetByActorKey[actorKey];
      if (fieldDeltaSet) {
        Object.assign(actor.fields, fieldDeltaSet);
      }
    }
  }

  return actorByKey;
};
