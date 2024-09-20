import { z } from 'zod';
import { useObservableMutation } from '/src/api/lib/ObservableMutation';
import { invalidateGetProjectLeads } from '/src/api/queries/useGetProjectLeads';
import { post } from '/src/api/restClient';
import { parseResponse } from '/src/api/utils/parseResponse';
import { ObjT } from '/src/utils/types';
import { waitOnDev } from '/src/utils/wait';

export type DeleteProjectsArgsT = {
  projectIds: string[];
};

export const deleteProjects = (args: DeleteProjectsArgsT) => {
  const url = `/projects/delete/`;
  return post(url, {
    project_ids: args.projectIds,
  })
    .then((response) => {
      const schema = z.object({
        deletedCount: z.number(),
      });
      const res = parseResponse(schema, response.data);

      return waitOnDev(1000, res);
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
