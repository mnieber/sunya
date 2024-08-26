import { ActorT } from '/src/api/types/ActorT';
import { getStepSequence, StepT } from '/src/api/types/StepT';

export const getReconstructedActor = (step: StepT, actor: ActorT): ActorT => {
  let reconstructedActor = {} as ActorT;

  for (const currentStep of getStepSequence(step)) {
    const fieldDeltaSet = currentStep.fieldDeltaSetByActorKey[actor.key];
    if (fieldDeltaSet) {
      Object.assign(reconstructedActor, fieldDeltaSet);
    }
  }

  return reconstructedActor as ActorT;
};
