import * as R from 'ramda';
import React from 'react';
import { ActorByKeyT } from '/src/api/types/ActorT';
import { StepT } from '/src/api/types/StepT';
import { StepTreeState } from '/src/steps/StepTreeState/StepTreeState';

export const StepTreeContext = React.createContext<any>(null);

export const useStepTreeContext = () => {
  const context = React.useContext(StepTreeContext);
  if (!context) {
    throw new Error(
      'useStepTreeContext must be used within a StepTreeContext.Provider'
    );
  }
  return context;
};

export const stepTreeCtx = R.mergeAll([
  {
    stepTreeState: [
      useStepTreeContext,
      'stepTreeState',
    ] as any as StepTreeState,
    rootStep: [useStepTreeContext, 'rootStep'] as any as StepT,
    reconstructedActorByKey: [
      useStepTreeContext,
      'reconstructedActorByKey',
    ] as any as ActorByKeyT,
    actorKey: [useStepTreeContext, 'actorKey'] as any as string,
  },
]);
