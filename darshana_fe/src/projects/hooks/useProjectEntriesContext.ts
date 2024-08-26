// File: src/projects/hooks/useProjectEntriesContext.ts

import * as R from 'ramda';
import React from 'react';
import { Highlight } from 'skandha-facets';
import { ProjectEntryT } from '/src/api/types/ProjectEntryT';
import { ProjectT } from '/src/api/types/ProjectT';
import { ProjectEntriesState } from '/src/projects/ProjectEntriesState/ProjectEntriesState';

export const ProjectEntriesContext = React.createContext<any>(null);

export const useProjectEntriesContext = () => {
  const context = React.useContext(ProjectEntriesContext);
  if (!context) {
    throw new Error(
      'useProjectEntriesContext must be used within a ProjectEntriesContext.Provider'
    );
  }
  return context;
};

export const projectEntriesCtx = R.mergeAll([
  {
    projectEntriesState: [
      useProjectEntriesContext,
      'projectEntriesState',
    ] as any as ProjectEntriesState,
    projectEntries: [
      useProjectEntriesContext,
      'projectEntries',
    ] as any as ProjectT[],
    projectEntry: [
      useProjectEntriesContext,
      'projectEntry',
    ] as any as ProjectEntryT,
    projectsHighlight: [
      useProjectEntriesContext,
      'projectsHighlight',
    ] as any as Highlight,
  },
]);
