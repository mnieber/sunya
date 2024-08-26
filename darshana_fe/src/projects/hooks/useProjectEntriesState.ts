import React from 'react';
import { useObservableQuery } from '/src/api/hooks';
import { useGetProjectEntries } from '/src/api/queries/useGetProjectEntries';
import { ProjectEntriesState } from '/src/projects/ProjectEntriesState/ProjectEntriesState';
import { useBuilder } from '/src/utils/hooks/useBuilder';
import { useGraftResourceStatesFromMemo } from '/src/utils/hooks/useGraftResourceStatesFromMemo';

export type PropsT = {};

export const useProjectEntriesState = (props: PropsT) => {
  const graftResourceStatesFromMemo = useGraftResourceStatesFromMemo({});

  const getProjectEntries = useObservableQuery(useGetProjectEntries({}), {
    fetchAsLoad: true,
    debugLabel: 'getProjectEntries',
  });

  const projectEntriesState = useBuilder(() => {
    const state = new ProjectEntriesState({
      getProjectEntries: () => {
        return graftResourceStatesFromMemo({
          resources: getProjectEntries.data?.projectEntries ?? [],
        });
      },
    });

    return state;
  }) as ProjectEntriesState;

  React.useEffect(
    () => () => projectEntriesState.destroy(),
    [projectEntriesState]
  );

  return {
    projectEntriesState,
    getProjectEntries,
  };
};
