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
        get reconstructedActor() {
          return updateSources({
            resource: stepTreeState.stepTreeCtr.data.reconstructedActor,
          });
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
        reconstructedActor: () => cache.reconstructedActor,
      });
    };

    return (
      <StepTreeContext.Provider value={getStepTreeContext()}>
        {props.children}
      </StepTreeContext.Provider>
    );
  }, ContextProps)
);
