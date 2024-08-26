import { makeAutoObservable } from 'mobx';
import { observer } from 'mobx-react-lite';
import { updateSources } from 'mobx-resource-states';
import React from 'react';
import { withContextProps } from 'react-props-from-context';
import { isQueryLoading } from '/src/api/lib/ObservableQuery';
import { ProjectContext } from '/src/projects/hooks/useProjectContext';
import { projectEntriesCtx } from '/src/projects/hooks/useProjectEntriesContext';
import { useProjectState } from '/src/projects/hooks/useProjectState';
import { createGetProps } from '/src/utils/createGetProps';
import { useBuilder } from '/src/utils/hooks/useBuilder';

export type PropsT = React.PropsWithChildren<{}>;

const ContextProps = {
  projectEntry: projectEntriesCtx.projectEntry,
};

export const ProjectStateProvider = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const { projectState, getProject } = useProjectState({
      projectId: props.projectEntry.id,
    });

    const cache = useBuilder(() =>
      makeAutoObservable({
        get scenario() {
          return updateSources(
            {
              resource: projectState.scenariosCtr.highlight.item,
              resourceName: 'scenario',
            },
            ['loading', () => isQueryLoading(getProject), 'scenario']
          );
        },
        get project() {
          return updateSources(
            { resource: projectState.projectCtr.data.project },
            ['loading', () => isQueryLoading(getProject), 'getProject']
          );
        },
      })
    );

    const getProjectContext = () => {
      return createGetProps({
        projectState: () => projectState,
        scenario: () => cache.scenario,
        project: () => cache.project,
      });
    };

    return (
      <ProjectContext.Provider value={getProjectContext()}>
        {props.children}
      </ProjectContext.Provider>
    );
  }, ContextProps)
);
