import { useQuery } from '@tanstack/react-query';
import { queryClient } from '/src/api/queryClient';
import { get } from '/src/api/restClient';
import { ProjectSchema } from '/src/api/types/ProjectSchema';
import { ProjectT } from '/src/api/types/ProjectT';
import { createQueryKey } from '/src/api/utils/createQueryKey';
import { parseSchema } from '/src/api/utils/parseSchema';
import { waitOnDev } from '/src/utils/wait';

export type GetProjectArgsT = {
  projectId: string;
};

export const getProject = (args: GetProjectArgsT) => {
  return get(`/projects/${args.projectId}/`).then((response) => {
    return waitOnDev(100, {
      project: parseSchema(ProjectSchema, response.data) as ProjectT,
    });
  });
};

export type OptionsT = {
  enabled?: boolean;
};

export type QueryKeyT = GetProjectArgsT;

export function getProjectQueryKey(args: QueryKeyT) {
  return createQueryKey<QueryKeyT>('getProject', args);
}

export const useGetProject = (args: GetProjectArgsT, options?: OptionsT) => {
  return useQuery({
    queryKey: getProjectQueryKey(args),
    queryFn: () => getProject(args),
    enabled: !!(options?.enabled ?? true),
  });
};

export const invalidateGetProject = (args: QueryKeyT) => {
  return queryClient.invalidateQueries({
    queryKey: getProjectQueryKey(args),
  });
};
