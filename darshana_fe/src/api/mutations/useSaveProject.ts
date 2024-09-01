import { useObservableMutation } from '/src/api/lib/ObservableMutation';
import { invalidateGetProject } from '/src/api/queries/useGetProject';
import { post } from '/src/api/restClient';
import { ProjectT } from '/src/api/types/ProjectT';
import { ObjT } from '/src/utils/types';
import { waitOnDev } from '/src/utils/wait';

export type SaveProjectArgsT = {
  project: ProjectT;
  form: {
    name: string;
    description: string;
  };
};

export const saveProject = (args: SaveProjectArgsT) => {
  const url = `/projects/${args.project.id}/save/`;
  return post(url, {
    saveProjectForm: args.form,
  })
    .then((response) => {
      return waitOnDev(1000, response);
    })
    .catch((error) => {
      const errorCodes = error.response.data;
      if (errorCodes.includes('PROJECT_NOT_FOUND')) {
        return waitOnDev(1000, {
          success: false,
        });
      }

      throw error;
    });
};

export const useSaveProject = () => {
  return useObservableMutation({
    mutationFn: saveProject,
    onSuccess: (response: ObjT, args: SaveProjectArgsT) => {
      invalidateGetProject({ projectId: args.project.id });
    },
  });
};
