import { useObservableMutation } from '/src/api/lib/ObservableMutation';
import { invalidateGetProject } from '/src/api/queries/useGetProject';
import { post } from '/src/api/restClient';
import { ProjectLeadSchema } from '/src/api/types/ProjectLeadSchema';
import { ProjectT } from '/src/api/types/ProjectT';
import { parseResponse } from '/src/api/utils/parseResponse';
import { ObjT } from '/src/utils/types';
import { waitOnDev } from '/src/utils/wait';

export type UpdateProjectArgsT = {
  project: ProjectT;
  updateProjectForm: {
    name: string;
    description: string;
  };
};

export const updateProject = (args: UpdateProjectArgsT) => {
  const url = `/projects/${args.project.id}/update/`;
  return post(url, {
    update_project_form: args.updateProjectForm,
  })
    .then((response) => {
      const res = parseResponse(ProjectLeadSchema, response.data);

      return waitOnDev(1000, res);
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

export const useUpdateProject = () => {
  return useObservableMutation({
    mutationFn: updateProject,
    onSuccess: (response: ObjT, args: UpdateProjectArgsT) => {
      invalidateGetProject({ projectId: args.project.id });
    },
  });
};
