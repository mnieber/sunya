import { useObservableMutation } from '/src/api/lib/ObservableMutation';
import { invalidateGetProjectLeads } from '/src/api/queries/useGetProjectLeads';
import { post } from '/src/api/restClient';
import { ProjectSchema } from '/src/api/types/ProjectSchema';
import { parseResponse } from '/src/api/utils/parseResponse';
import { ObjT } from '/src/utils/types';
import { waitOnDev } from '/src/utils/wait';

export type CreateProjectArgsT = {
  createProjectForm: {
    name: string;
    description: string;
  };
};

export const createProject = (args: CreateProjectArgsT) => {
  const url = `/projects/create/`;
  return post(url, {
    create_project_form: args.createProjectForm,
  })
    .then((response) => {
      const res = parseResponse(ProjectSchema, response.data);
      return waitOnDev(1000, res);
    })
    .catch((error) => {
      const errorCodes = error.response.data;
      if (errorCodes.includes('PROJECT_NAME_ALREADY_EXISTS')) {
        return waitOnDev(1000, {
          success: false,
        });
      }

      throw error;
    });
};

export const useCreateProject = () => {
  return useObservableMutation({
    mutationFn: createProject,
    onSuccess: (response: ObjT, args: CreateProjectArgsT) => {
      invalidateGetProjectLeads();
    },
  });
};
