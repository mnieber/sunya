import * as R from 'ramda';
import React from 'react';
import { useObservableQuery } from '/src/api/hooks';
import { useGetProject } from '/src/api/queries/useGetProject';
import { ProjectState } from '/src/projects/ProjectState';
import { useBuilder } from '/src/utils/hooks/useBuilder';
import { useGraftResourceStatesFromMemo } from '/src/utils/hooks/useGraftResourceStatesFromMemo';

export type PropsT = {
  projectId?: string;
};

export const useProjectState = (props: PropsT) => {
  const graftResourceStatesFromMemo = useGraftResourceStatesFromMemo({});

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
    });

    return state;
  }) as ProjectState;

  React.useEffect(() => () => projectState.destroy(), [projectState]);

  return {
    projectState,
    getProject,
  };
};
