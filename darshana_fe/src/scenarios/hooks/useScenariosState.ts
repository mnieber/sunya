import React from 'react';
import { useObservableQuery } from '/src/api/hooks';
import { useGetScenarios } from '/src/api/queries/useGetScenarios';
import { ScenariosState } from '/src/scenarios/ScenariosState';
import { useBuilder } from '/src/utils/hooks/useBuilder';
import { useGraftResourceStatesFromMemo } from '/src/utils/hooks/useGraftResourceStatesFromMemo';

export type PropsT = {};

export const useScenariosState = (props: PropsT) => {
  const graftResourceStatesFromMemo = useGraftResourceStatesFromMemo({});

  const getScenarios = useObservableQuery(useGetScenarios({}), {
    fetchAsLoad: true,
    debugLabel: 'getScenarios',
  });

  const scenariosState = useBuilder(() => {
    const state = new ScenariosState({
      getScenarios: () => {
        return graftResourceStatesFromMemo({
          resources: getScenarios.data?.scenarios ?? [],
        });
      },
    });

    return state;
  }) as ScenariosState;

  React.useEffect(() => () => scenariosState.destroy(), [scenariosState]);

  return {
    scenariosState,
    getScenarios,
  };
};
