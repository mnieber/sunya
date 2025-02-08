import React from 'react';
import { ScenarioT } from '/src/api/types/ScenarioT';
import { StepTreeState } from '/src/steps/StepTreeState/StepTreeState';
import { useBuilder } from '/src/utils/hooks/useBuilder';

export type PropsT = {
  getScenario: () => ScenarioT | undefined;
};

export const useStepTreeState = (props: PropsT) => {
  const stepTreeState = useBuilder(() => {
    const state = new StepTreeState({
      getRootStep: () => {
        const scenario = props.getScenario();
        return scenario?.rootStep ?? null;
      },
    });

    return state;
  }) as StepTreeState;

  React.useEffect(() => () => stepTreeState.destroy(), [stepTreeState]);

  return {
    stepTreeState,
  };
};
