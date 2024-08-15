import React from 'react';
import { ScenariosState } from '/src/scenarios/ScenariosState';
import { useBuilder } from '/src/utils/hooks/useBuilder';

export type PropsT = {};

export const useScenariosState = (props: PropsT) => {
  const scenariosState = useBuilder<ScenariosState>(() => {
    return new ScenariosState({
      getScenarios: () => {
        return graftResourceStatesFromMemo({
          resources: [] /* MOONLEAP TODO */,
        });
      },
    });
  }) as ScenariosState;

  React.useEffect(() => () => scenariosState.destroy(), [scenariosState]);

  return {
    scenariosState,
  };
};
