import { useObservableMutation } from '/src/api/lib/ObservableMutation';
import { invalidateGetProjectLeads } from '/src/api/queries/useGetProjectLeads';
import { post } from '/src/api/restClient';
import { ObjT } from '/src/utils/types';
import { waitOnDev } from '/src/utils/wait';

export type CreateProjectArgsT = {
  form: {
    name: string;
    description: string;
  };
};

export const createProject = (args: CreateProjectArgsT) => {
  const url = `/projects/create/`;
  return post(url, {
    createProjectForm: args.form,
  })
    .then((response) => {
      return waitOnDev(1000, response);
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
