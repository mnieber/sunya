import { trackPromise } from 'mobx-resource-states';
import React from 'react';
import { useObservableQuery } from '/src/api/hooks';
import { useCreateProject } from '/src/api/mutations/useCreateProject';
import {
  DeleteProjectsArgsT,
  useDeleteProjects,
} from '/src/api/mutations/useDeleteProjects';
import { useSaveProject } from '/src/api/mutations/useSaveProject';
import { useGetProjectLeads } from '/src/api/queries/useGetProjectLeads';
import { ProjectLeadsState } from '/src/projects/ProjectLeadsState/ProjectLeadsState';
import { useBuilder } from '/src/utils/hooks/useBuilder';
import { useGraftResourceStatesFromMemo } from '/src/utils/hooks/useGraftResourceStatesFromMemo';
import { lookUp } from '/src/utils/ids';
import { ObjT } from '/src/utils/types';

export type PropsT = {};

export const useProjectLeadsState = (props: PropsT) => {
  const graftResourceStatesFromMemo = useGraftResourceStatesFromMemo({});

  // Mutations
  const deleteProjects = useDeleteProjects();
  const createProject = useCreateProject();
  const saveProject = useSaveProject();

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
      //
      deleteProjects: (projectIds: string[]) => {
        const projectLeads = lookUp(
          projectIds,
          projectLeadsState.projectLeadsCtr.data.projectLeadById
        );
        return trackPromise({
          name: 'deleteProjects',
          states: { updating: projectLeads },
          promise: deleteProjects.mutateAsync({
            projectIds: projectIds,
          } as DeleteProjectsArgsT),
        }).result;
      },
      //
      saveProject: (values: ObjT) => {
        const mutation = values.projectForm.isTransient
          ? createProject
          : saveProject;
        return trackPromise({
          name: 'saveProject',
          promise: mutation.mutateAsync(values),
        }).result;
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
