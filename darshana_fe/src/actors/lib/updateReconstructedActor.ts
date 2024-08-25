import { ActorT } from '/src/api/types/ActorT';
import { StepT } from '/src/api/types/StepT';
import { ObjT } from '/src/utils/types';

export const updateReconstructedActor = (step: StepT) => {
  let currentStep: StepT | null = step;
  let reconstructedActor: ObjT = {};

  while (currentStep) {
    Object.entries(currentStep.field_delta_set_by_actor_key).forEach(
      ([actorKey, fieldDeltas]) => {
        if (!reconstructedActor[actorKey]) {
          reconstructedActor[actorKey] = {};
        }
        Object.assign(reconstructedActor[actorKey], fieldDeltas);
      }
    );
    currentStep = currentStep.parent_step;
  }

  return _createActorFromReconstructedData(reconstructedActor);
};

export const _createActorFromReconstructedData = (data: ObjT): ActorT => {
  return {
    id: 'reconstructed-actor-id',
    key: 'reconstructed-actor-key',
    fields: data,
    changed_fields: Object.keys(data),
  };
};
