import * as R from 'ramda';
import React from 'react';
import { Highlight } from 'skandha-facets';
import { ProjectLeadT } from '/src/api/types/ProjectLeadT';
import { ProjectT } from '/src/api/types/ProjectT';
import { ProjectLeadsState } from '/src/projects/ProjectLeadsState/ProjectLeadsState';

export const ProjectLeadsContext = React.createContext<any>(null);

export const useProjectLeadsContext = () => {
  const context = React.useContext(ProjectLeadsContext);
  if (!context) {
    throw new Error(
      'useProjectLeadsContext must be used within a ProjectLeadsContext.Provider'
    );
  }
  return context;
};

export const projectLeadsCtx = R.mergeAll([
  {
    projectLeadsState: [
      useProjectLeadsContext,
      'projectLeadsState',
    ] as any as ProjectLeadsState,
    projectLeads: [useProjectLeadsContext, 'projectLeads'] as any as ProjectT[],
    projectLead: [useProjectLeadsContext, 'projectLead'] as any as ProjectLeadT,
    projectLeadsHighlight: [
      useProjectLeadsContext,
      'projectLeadsHighlight',
    ] as any as Highlight,
  },
]);
