import { makeAutoObservable } from 'mobx';
import { observer } from 'mobx-react-lite';
import { updateSources } from 'mobx-resource-states';
import React from 'react';
import { useScenariosState } from '/src/scenarios/hooks/useScenariosState';
import { useBuilder } from '/src/utils/hooks/useBuilder';

export type PropsT = React.PropsWithChildren<{}>;

const ContextProps = {};

export const ScenariosStateProvider = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const { scenariosState: state } = useScenariosState({
      /* MOONLEAP TODO */
    });

    const cache = useBuilder(() =>
      makeAutoObservable({
        get scenarios() {
          return updateSources(
            {
              resource: state.scenariosCtr.store.items,
              resourceName: 'scenarios',
            },
            ['loading', () => 'MOONLEAP TODO'],
            ['updating', () => 'MOONLEAP TODO']
          );
        },
        get scenario() {
          return updateSources(
            { resource: state.scenariosCtr.highlight.item },
            ['loading', () => 'MOONLEAP TODO'],
            ['updating', () => 'MOONLEAP TODO']
          );
        },
      })
    );

    const getScenariosContext = () => {
      return createGetProps(
        R.mergeAll([
          {
            scenariosState: () => state,
          },
          {
            scenarios: () => cache.scenarios,
            scenario: () => cache.scenario,
            scenariosHighlight: () => state.scenariosCtr.highlight,
            scenariosSelection: () => state.scenariosCtr.selection,
          },
        ])
      );
    };

    return (
      <ScenariosContext.Provider value={getScenariosContext()}>
        {props.children}
      </ScenariosContext.Provider>
    );
  }, ContextProps)
);
