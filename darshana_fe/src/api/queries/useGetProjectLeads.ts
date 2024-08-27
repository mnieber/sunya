import { useQuery } from '@tanstack/react-query';
import { queryClient } from '/src/api/queryClient';
import { get } from '/src/api/restClient';
import { ProjectT } from '/src/api/types/ProjectT';
import { createQueryKey } from '/src/api/utils/createQueryKey';
import { waitOnDev } from '/src/utils/wait';

export type GetProjectLeadsArgsT = {};

export const getProjectLeads = (args: GetProjectLeadsArgsT) => {
  return get('/projects/leads/').then((response) => {
    return waitOnDev(100, { projectLeads: response.data as ProjectT[] });
  });
};

export type OptionsT = {
  enabled?: boolean;
};

export type QueryKeyT = GetProjectLeadsArgsT;

export function getProjectLeadsQueryKey(args: QueryKeyT) {
  return createQueryKey<QueryKeyT>('getProjectLeads', args);
}

export const useGetProjectLeads = (
  args: GetProjectLeadsArgsT = {},
  options?: OptionsT
) => {
  return useQuery({
    queryKey: getProjectLeadsQueryKey(args),
    queryFn: () => getProjectLeads(args),
    enabled: !!(options?.enabled ?? true),
  });
};

export const invalidateGetProjectLeads = (args: QueryKeyT = {}) => {
  return queryClient.invalidateQueries({
    queryKey: getProjectLeadsQueryKey(args),
  });
};
