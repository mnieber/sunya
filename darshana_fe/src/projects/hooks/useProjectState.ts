import { trackPromise } from 'mobx-resource-states';
import * as R from 'ramda';
import React from 'react';
import { useObservableQuery } from '/src/api/hooks';
import { useUpdateProject } from '/src/api/mutations/useUpdateProject';
import { useUploadSpecFiles } from '/src/api/mutations/useUploadSpecFiles';
import { useGetProject } from '/src/api/queries/useGetProject';
import { ProjectState } from '/src/projects/ProjectState';
import { useBuilder } from '/src/utils/hooks/useBuilder';
import { useGraftResourceStatesFromMemo } from '/src/utils/hooks/useGraftResourceStatesFromMemo';
import { ObjT } from '/src/utils/types';

export type PropsT = {
  projectId?: string;
};

export const useProjectState = (props: PropsT) => {
  const graftResourceStatesFromMemo = useGraftResourceStatesFromMemo({});

  // Mutations
  const uploadSpecFiles = useUploadSpecFiles();
  const updateProject = useUpdateProject();

  const getProject = useObservableQuery(
    useGetProject(
      { projectId: props.projectId! },
      { enabled: !!props.projectId }
    ),
    {
      fetchAsLoad: true,
      debugLabel: 'getProject',
    }
  );

  const projectState = useBuilder(() => {
    const state = new ProjectState({
      getProject: () => {
        const project = getProject.data?.project;
        return R.head(
          graftResourceStatesFromMemo({
            resources: project ? [project] : [],
          })
        );
      },
      //
      updateProject: (values: ObjT) => {
        return trackPromise({
          name: 'updateProject',
          promise: updateProject.mutateAsync({
            project: projectState.projectCtr.data.project!,
            form: values.projectLeadForm,
          }),
        }).result;
      },
      //
      uploadSpecFiles: (files: File[]) => {
        return trackPromise({
          name: 'uploadSpecFiles',
          promise: uploadSpecFiles.mutateAsync({
            project: projectState.projectCtr.data.project!,
            files,
          }),
        }).result;
      },
    });

    return state;
  }) as ProjectState;

  React.useEffect(() => () => projectState.destroy(), [projectState]);

  return {
    projectState,
    getProject,
    uploadSpecFiles,
  };
};
