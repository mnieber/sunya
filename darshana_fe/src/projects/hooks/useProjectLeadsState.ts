import React from 'react';
import { useObservableQuery } from '/src/api/hooks';
import { useGetProjectLeads } from '/src/api/queries/useGetProjectLeads';
import { ProjectLeadsState } from '/src/projects/ProjectLeadsState/ProjectLeadsState';
import { useBuilder } from '/src/utils/hooks/useBuilder';
import { useGraftResourceStatesFromMemo } from '/src/utils/hooks/useGraftResourceStatesFromMemo';

export type PropsT = {};

export const useProjectLeadsState = (props: PropsT) => {
  const graftResourceStatesFromMemo = useGraftResourceStatesFromMemo({});

  const getProjectLeads = useObservableQuery(useGetProjectLeads({}), {
    fetchAsLoad: true,
    debugLabel: 'getProjectLeads',
  });

  const projectLeadsState = useBuilder(() => {
    const state = new ProjectLeadsState({
      getProjectLeads: () => {
        return graftResourceStatesFromMemo({
          resources: getProjectLeads.data?.projectLeads ?? [],
        });
      },
    });

    return state;
  }) as ProjectLeadsState;

  React.useEffect(() => () => projectLeadsState.destroy(), [projectLeadsState]);

  return {
    projectLeadsState,
    getProjectLeads,
  };
};
