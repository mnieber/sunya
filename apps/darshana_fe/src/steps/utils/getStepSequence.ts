import { StepByIdT, StepT } from '/src/api/types/StepT';

export function getStepSequence(
  rootStep: StepT,
  stopStepId: string,
  stepById: StepByIdT
): StepT[] {
  const result: StepT[] = [];
  const stack: { stepId: string; visited: boolean }[] = [
    { stepId: rootStep.id, visited: false },
  ];

  while (stack.length > 0) {
    const { stepId, visited } = stack[stack.length - 1];
    const currentStep = stepById[stepId];

    if (!visited) {
      stack[stack.length - 1].visited = true;

      // Push children onto the stack in reverse order
      for (let i = currentStep.childSteps.length - 1; i >= 0; i--) {
        stack.push({ stepId: currentStep.childSteps[i].id, visited: false });
      }
    } else {
      stack.pop();
      result.push(currentStep);

      if (stepId === stopStepId) {
        break;
      }
    }
  }

  return result;
}
