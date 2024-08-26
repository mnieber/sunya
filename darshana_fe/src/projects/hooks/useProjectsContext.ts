// File: src/projects/hooks/useProjectsContext.ts

import * as R from 'ramda';
import React from 'react';
import { Highlight } from 'skandha-facets';
import { ProjectT } from '/src/api/types/ProjectT';
import { ProjectsState } from '/src/projects/ProjectsState/ProjectsState';

export const ProjectsContext = React.createContext<any>(null);

export const useProjectsContext = () => {
  const context = React.useContext(ProjectsContext);
  if (!context) {
    throw new Error(
      'useProjectsContext must be used within a ProjectsContext.Provider'
    );
  }
  return context;
};

export const projectsCtx = R.mergeAll([
  {
    projectsState: [
      useProjectsContext,
      'projectsState',
    ] as any as ProjectsState,
    projects: [useProjectsContext, 'projects'] as any as ProjectT[],
    projectId: [useProjectsContext, 'projectId'] as any as string,
    projectsHighlight: [
      useProjectsContext,
      'projectsHighlight',
    ] as any as Highlight,
  },
]);
