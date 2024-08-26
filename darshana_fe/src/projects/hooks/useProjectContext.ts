import * as R from 'ramda';
import React from 'react';
import { Highlight } from 'skandha-facets';
import { ScenarioT } from '/src/api/types/ScenarioT';
import { ProjectState } from '/src/projects/ProjectState';

export const ProjectContext = React.createContext<any>(null);

export const useProjectContext = () => {
  const context = React.useContext(ProjectContext);
  if (!context) {
    throw new Error(
      'useProjectContext must be used within a ProjectContext.Provider'
    );
  }
  return context;
};

export const projectCtx = R.mergeAll([
  {
    projectState: [useProjectContext, 'projectState'] as any as ProjectState,
    scenarios: [useProjectContext, 'scenarios'] as any as ScenarioT[],
    scenario: [useProjectContext, 'scenario'] as any as ScenarioT,
    scenariosHighlight: [
      useProjectContext,
      'scenariosHighlight',
    ] as any as Highlight,
  },
]);
