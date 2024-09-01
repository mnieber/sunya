import { useObservableMutation } from '/src/api/lib/ObservableMutation';
import { invalidateGetProjectLeads } from '/src/api/queries/useGetProjectLeads';
import { post } from '/src/api/restClient';
import { ObjT } from '/src/utils/types';
import { waitOnDev } from '/src/utils/wait';

export type DeleteProjectsArgsT = {
  projectIds: string[];
};

export const deleteProjects = (args: DeleteProjectsArgsT) => {
  const url = `/projects/delete/`;
  return post(url, {
    projectIds: args.projectIds,
  })
    .then((response) => {
      return waitOnDev(1000, response);
    })
    .catch((error) => {
      // Handle specific error cases if needed
      throw error;
    });
};

export const useDeleteProjects = () => {
  return useObservableMutation({
    mutationFn: deleteProjects,
    onSuccess: (response: ObjT, args: DeleteProjectsArgsT) => {
      invalidateGetProjectLeads();
    },
  });
};
