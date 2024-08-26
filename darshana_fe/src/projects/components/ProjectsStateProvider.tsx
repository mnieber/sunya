// File: src/projects/components/ProjectsStateProvider.tsx

import { makeAutoObservable } from 'mobx';
import { observer } from 'mobx-react-lite';
import { updateSources } from 'mobx-resource-states';
import React from 'react';
import { isQueryLoading } from '/src/api/lib/ObservableQuery';
import { ProjectsContext } from '/src/projects/hooks/useProjectsContext';
import { useProjectsState } from '/src/projects/hooks/useProjectsState';
import { createGetProps } from '/src/utils/createGetProps';
import { useBuilder } from '/src/utils/hooks/useBuilder';

export type PropsT = React.PropsWithChildren<{}>;

export const ProjectsStateProvider = observer((props: PropsT) => {
  const { projectsState, getProjects } = useProjectsState({});

  const cache = useBuilder(() =>
    makeAutoObservable({
      get project() {
        return updateSources(
          {
            resource: projectsState.projectsCtr.highlight.item,
            resourceName: 'project',
          },
          ['loading', () => isQueryLoading(getProjects), 'project']
        );
      },
      get projects() {
        return updateSources(
          { resource: projectsState.projectsCtr.data.projects },
          ['loading', () => isQueryLoading(getProjects), 'getProjects']
        );
      },
    })
  );

  const getProjectsContext = () => {
    return createGetProps({
      projectsState: () => projectsState,
      projects: () => cache.projects,
      projectId: () => cache.project?.id,
      projectsHighlight: () => projectsState.projectsCtr.highlight,
    });
  };

  return (
    <ProjectsContext.Provider value={getProjectsContext()}>
      {props.children}
    </ProjectsContext.Provider>
  );
});
