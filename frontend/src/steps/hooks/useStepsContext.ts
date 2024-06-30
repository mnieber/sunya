import React from 'react';
import { Highlight } from 'skandha-facets';
import { StepsState } from '/src/steps/StepsState';

export const StepsContext = React.createContext<any>(null);

export const useStepsContext = () => {
  const context = React.useContext(StepsContext);
  if (!context) {
    throw new Error(
      'useStepsContext must be used within a StepsContext.Provider'
    );
  }
  return context;
};

export const stepsCtx = {
  stepsState: [useStepsContext, 'stepsState'] as any as StepsState,
  step: [useStepsContext, 'step'] as any as StepT,
  steps: [useStepsContext, 'steps'] as any as StepT[],
  stepsHighlight: [useStepsContext, 'stepsHighlight'] as any as Highlight,
};
