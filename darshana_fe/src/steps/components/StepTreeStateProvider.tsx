import { makeAutoObservable } from 'mobx';
import { isLoading, updateSources } from 'mobx-resource-states';
import { createGetProps } from '/src/utils/createGetProps';
import { useBuilder } from '/src/utils/hooks/useBuilder';

import { observer } from 'mobx-react-lite';
import React from 'react';
import { withContextProps } from 'react-props-from-context';
import { projectCtx } from '/src/projects/hooks/useProjectContext';
import { StepTreeContext } from '/src/steps/hooks/useStepTreeContext';
import { useStepTreeState } from '/src/steps/hooks/useStepTreeState';

export type PropsT = React.PropsWithChildren<{}>;

const ContextProps = {
  scenario: projectCtx.scenario,
};

export const StepTreeStateProvider = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const { stepTreeState } = useStepTreeState({
      getScenario: () => props.scenario,
    });

    const cache = useBuilder(() =>
      makeAutoObservable({
        get reconstructedActorByKey() {
          return updateSources({
            resource:
              stepTreeState.stepTreeCtr.data.reconstructedActorByKey ?? {},
          });
        },
        get actorContext() {
          return stepTreeState.stepTreeCtr.data.actorContext;
        },
        get rootStep() {
          return updateSources(
            {
              resource: stepTreeState.stepTreeCtr.data.rootStep,
            },
            ['loading', () => isLoading(props.scenario), 'scenario']
          );
        },
      })
    );

    const getStepTreeContext = () => {
      return createGetProps({
        stepTreeState: () => stepTreeState,
        rootStep: () => cache.rootStep,
        reconstructedActorByKey: () => cache.reconstructedActorByKey,
        actorContext: () => cache.actorContext,
      });
    };

    return (
      <StepTreeContext.Provider value={getStepTreeContext()}>
        {props.children}
      </StepTreeContext.Provider>
    );
  }, ContextProps)
);
