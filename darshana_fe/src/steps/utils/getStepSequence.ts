import { StepByIdT, StepT } from '/src/api/types/StepT';

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
