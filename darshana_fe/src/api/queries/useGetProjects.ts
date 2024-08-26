// File: src/api/queries/useGetProjects.ts

import { useQuery } from '@tanstack/react-query';
import { queryClient } from '/src/api/queryClient';
import { get } from '/src/api/restClient';
import { ProjectT } from '/src/api/types/ProjectT';
import { createQueryKey } from '/src/api/utils/createQueryKey';
import { waitOnDev } from '/src/utils/wait';

export type GetProjectsArgsT = {};

export const getProjects = (args: GetProjectsArgsT) => {
  return get('/projects/list/').then((response) => {
    return waitOnDev(100, { projects: response.data as ProjectT[] });
  });
};

export type OptionsT = {
  enabled?: boolean;
};

export type QueryKeyT = GetProjectsArgsT;

export function getProjectsQueryKey(args: QueryKeyT) {
  return createQueryKey<QueryKeyT>('getProjects', args);
}

export const useGetProjects = (
  args: GetProjectsArgsT = {},
  options?: OptionsT
) => {
  return useQuery({
    queryKey: getProjectsQueryKey(args),
    queryFn: () => getProjects(args),
    enabled: !!(options?.enabled ?? true),
  });
};

export const invalidateGetProjects = (args: QueryKeyT = {}) => {
  return queryClient.invalidateQueries({
    queryKey: getProjectsQueryKey(args),
  });
};
