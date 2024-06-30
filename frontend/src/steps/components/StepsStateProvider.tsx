import { makeAutoObservable } from 'mobx';
import { observer } from 'mobx-react-lite';
import { updateSources } from 'mobx-resource-states';
import React from 'react';
import { useStepsState } from '/src/steps/hooks/useStepsState';
import { useBuilder } from '/src/utils/hooks/useBuilder';

export type PropsT = React.PropsWithChildren<{}>;

const ContextProps = {};

export const StepsStateProvider = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const { stepsState: state } = useStepsState({
      /* MOONLEAP TODO */
    });

    const cache = useBuilder(() =>
      makeAutoObservable({
        get steps() {
          return updateSources(
            {
              resource: state.stepsCtr.store.items,
              resourceName: 'steps',
            },
            ['loading', () => 'MOONLEAP TODO'],
            ['updating', () => 'MOONLEAP TODO']
          );
        },
        get step() {
          return updateSources(
            { resource: state.stepsCtr.highlight.item },
            ['loading', () => 'MOONLEAP TODO'],
            ['updating', () => 'MOONLEAP TODO']
          );
        },
      })
    );

    const getStepsContext = () => {
      return createGetProps(
        R.mergeAll([
          {
            stepsState: () => state,
          },
          {
            steps: () => cache.steps,
            step: () => cache.step,
            stepsHighlight: () => state.stepsCtr.highlight,
          },
        ])
      );
    };

    return (
      <StepsContext.Provider value={getStepsContext()}>
        {props.children}
      </StepsContext.Provider>
    );
  }, ContextProps)
);
