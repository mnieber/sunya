import React from 'react';
import { StepsState } from '/src/steps/StepsState';
import { useBuilder } from '/src/utils/hooks/useBuilder';

export type PropsT = {};

export const useStepsState = (props: PropsT) => {
  const stepsState = useBuilder<StepsState>(() => {
    return new StepsState({
      getSteps: () => {
        return graftResourceStatesFromMemo({
          resources: [] /* MOONLEAP TODO */,
        });
      },
    });
  }) as StepsState;

  React.useEffect(() => () => stepsState.destroy(), [stepsState]);

  return {
    stepsState,
  };
};
