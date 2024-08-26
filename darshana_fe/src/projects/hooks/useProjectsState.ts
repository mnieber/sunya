// File: src/projects/hooks/useProjectsState.ts

import React from 'react';
import { useObservableQuery } from '/src/api/hooks';
import { useGetProjects } from '/src/api/queries/useGetProjects';
import { ProjectsState } from '/src/projects/ProjectsState/ProjectsState';
import { useBuilder } from '/src/utils/hooks/useBuilder';
import { useGraftResourceStatesFromMemo } from '/src/utils/hooks/useGraftResourceStatesFromMemo';

export type PropsT = {};

export const useProjectsState = (props: PropsT) => {
  const graftResourceStatesFromMemo = useGraftResourceStatesFromMemo({});

  const getProjects = useObservableQuery(useGetProjects({}), {
    fetchAsLoad: true,
    debugLabel: 'getProjects',
  });

  const projectsState = useBuilder(() => {
    const state = new ProjectsState({
      getProjects: () => {
        return graftResourceStatesFromMemo({
          resources: getProjects.data?.projects ?? [],
        });
      },
    });

    return state;
  }) as ProjectsState;

  React.useEffect(() => () => projectsState.destroy(), [projectsState]);

  return {
    projectsState,
    getProjects,
  };
};
