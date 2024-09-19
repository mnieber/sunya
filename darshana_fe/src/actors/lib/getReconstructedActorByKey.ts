import * as R from 'ramda';
import { ActorByKeyT } from '/src/api/types/ActorT';
import { StepByIdT, StepT, getStepSequence } from '/src/api/types/StepT';

export const getReconstructedActorByKey = (
  step: StepT,
  stepById: StepByIdT
): ActorByKeyT => {
  let actorByKey: ActorByKeyT = {};
  const createActor = (actorKey: string) => {
    actorByKey[actorKey] = { key: actorKey, fields: {}, changedFields: [] };
  };

  for (const factBit of step.fact) {
    if (factBit.typeName === 'actor') {
      const actorKey = factBit.value as string;
      createActor(actorKey);
    }
  }

  for (const actorKeyByRoleName of [
    step.preActorKeyByRoleName,
    step.postActorKeyByRoleName,
  ]) {
    for (const roleName of R.keys(actorKeyByRoleName)) {
      const actorKey = step.preActorKeyByRoleName[roleName];
      createActor(actorKey);
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
