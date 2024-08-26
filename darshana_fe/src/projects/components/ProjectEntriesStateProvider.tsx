import { makeAutoObservable } from 'mobx';
import { observer } from 'mobx-react-lite';
import { updateSources } from 'mobx-resource-states';
import React from 'react';
import { isQueryLoading } from '/src/api/lib/ObservableQuery';
import { ProjectEntriesContext } from '/src/projects/hooks/useProjectEntriesContext';
import { useProjectEntriesState } from '/src/projects/hooks/useProjectEntriesState';
import { createGetProps } from '/src/utils/createGetProps';
import { useBuilder } from '/src/utils/hooks/useBuilder';

export type PropsT = React.PropsWithChildren<{}>;

export const ProjectEntriesStateProvider = observer((props: PropsT) => {
  const { projectEntriesState, getProjectEntries } = useProjectEntriesState({});

  const cache = useBuilder(() =>
    makeAutoObservable({
      get projectEntry() {
        return updateSources(
          {
            resource: projectEntriesState.projectEntriesCtr.highlight.item,
            resourceName: 'projectEntry',
          },
          ['loading', () => isQueryLoading(getProjectEntries), 'projectEntry']
        );
      },
      get projectEntries() {
        return updateSources(
          {
            resource: projectEntriesState.projectEntriesCtr.data.projectEntries,
          },
          [
            'loading',
            () => isQueryLoading(getProjectEntries),
            'getProjectEntries',
          ]
        );
      },
    })
  );

  const getProjectEntriesContext = () => {
    return createGetProps({
      projectEntriesState: () => projectEntriesState,
      projectEntries: () => cache.projectEntries,
      projectEntry: () => cache.projectEntry,
      projectEntriesHighlight: () =>
        projectEntriesState.projectEntriesCtr.highlight,
    });
  };

  return (
    <ProjectEntriesContext.Provider value={getProjectEntriesContext()}>
      {props.children}
    </ProjectEntriesContext.Provider>
  );
});
