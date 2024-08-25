import * as R from 'ramda';
import React from 'react';
import { Highlight } from 'skandha-facets';
import { ScenarioT } from '/src/api/types/ScenarioT';
import { ScenariosState } from '/src/scenarios/ScenariosState';

export const ScenariosContext = React.createContext<any>(null);

export const useScenariosContext = () => {
  const context = React.useContext(ScenariosContext);
  if (!context) {
    throw new Error(
      'useScenariosContext must be used within a ScenariosContext.Provider'
    );
  }
  return context;
};

export const scenariosCtx = R.mergeAll([
  {
    scenariosState: [
      useScenariosContext,
      'scenariosState',
    ] as any as ScenariosState,
    scenarios: [useScenariosContext, 'scenarios'] as any as ScenarioT[],
    scenario: [useScenariosContext, 'scenario'] as any as ScenarioT,
    scenariosHighlight: [
      useScenariosContext,
      'scenariosHighlight',
    ] as any as Highlight,
  },
]);
