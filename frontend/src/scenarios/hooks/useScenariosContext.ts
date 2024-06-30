import React from 'react';
import { Highlight, Selection } from 'skandha-facets';
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

export const scenariosCtx = {
  scenariosState: [
    useScenariosContext,
    'scenariosState',
  ] as any as ScenariosState,
  scenario: [useScenariosContext, 'scenario'] as any as ScenarioT,
  scenarios: [useScenariosContext, 'scenarios'] as any as ScenarioT[],
  scenariosHighlight: [
    useScenariosContext,
    'scenariosHighlight',
  ] as any as Highlight,
  scenariosSelection: [
    useScenariosContext,
    'scenariosSelection',
  ] as any as Selection,
};
