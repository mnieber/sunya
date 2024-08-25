import { makeAutoObservable } from 'mobx';
import { observer } from 'mobx-react-lite';
import { updateSources } from 'mobx-resource-states';
import React from 'react';
import { isQueryLoading } from '/src/api/lib/ObservableQuery';
import { ScenariosContext } from '/src/scenarios/hooks/useScenariosContext';
import { useScenariosState } from '/src/scenarios/hooks/useScenariosState';
import { createGetProps } from '/src/utils/createGetProps';
import { useBuilder } from '/src/utils/hooks/useBuilder';

export type PropsT = React.PropsWithChildren<{}>;

export const ScenariosStateProvider = observer((props: PropsT) => {
  const { scenariosState, getScenarios } = useScenariosState({});

  const cache = useBuilder(() =>
    makeAutoObservable({
      get scenario() {
        return updateSources(
          {
            resource: scenariosState.scenariosCtr.highlight.item,
            resourceName: 'scenario',
          },
          ['loading', () => isQueryLoading(getScenarios), 'scenario']
        );
      },
      get scenarios() {
        return updateSources(
          { resource: scenariosState.scenariosCtr.data.scenarios },
          ['loading', () => isQueryLoading(getScenarios), 'getScenarios']
        );
      },
    })
  );

  const getScenariosContext = () => {
    return createGetProps({
      scenariosState: () => scenariosState,
      scenarios: () => cache.scenarios,
      scenario: () => cache.scenario,
      scenariosHighlight: () => scenariosState.scenariosCtr.highlight,
    });
  };

  return (
    <ScenariosContext.Provider value={getScenariosContext()}>
      {props.children}
    </ScenariosContext.Provider>
  );
});
