import { useQuery } from '@tanstack/react-query';
import { queryClient } from '/src/api/queryClient';
import { get } from '/src/api/restClient';
import { ProjectT } from '/src/api/types/ProjectT';
import { createQueryKey } from '/src/api/utils/createQueryKey';
import { waitOnDev } from '/src/utils/wait';

export type GetProjectEntriesArgsT = {};

export const getProjectEntries = (args: GetProjectEntriesArgsT) => {
  return get('/projects/entries/').then((response) => {
    return waitOnDev(100, { projectEntries: response.data as ProjectT[] });
  });
};

export type OptionsT = {
  enabled?: boolean;
};

export type QueryKeyT = GetProjectEntriesArgsT;

export function getProjectEntriesQueryKey(args: QueryKeyT) {
  return createQueryKey<QueryKeyT>('getProjectEntries', args);
}

export const useGetProjectEntries = (
  args: GetProjectEntriesArgsT = {},
  options?: OptionsT
) => {
  return useQuery({
    queryKey: getProjectEntriesQueryKey(args),
    queryFn: () => getProjectEntries(args),
    enabled: !!(options?.enabled ?? true),
  });
};

export const invalidateGetProjectEntries = (args: QueryKeyT = {}) => {
  return queryClient.invalidateQueries({
    queryKey: getProjectEntriesQueryKey(args),
  });
};
