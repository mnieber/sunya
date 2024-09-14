import { useQuery } from '@tanstack/react-query';
import { queryClient } from '/src/api/queryClient';
import { get } from '/src/api/restClient';
import { ProjectT } from '/src/api/types/ProjectT';
import { createQueryKey } from '/src/api/utils/createQueryKey';
import { waitOnDev } from '/src/utils/wait';

export type GetProjectLeadsArgsT = {};
export type OptionsT = {
  enabled?: boolean;
};

export type GetProjectLeadsQueryKeyT = GetProjectLeadsArgsT;
export function getProjectLeadsQueryKey(args: GetProjectLeadsQueryKeyT) {
  return createQueryKey<GetProjectLeadsQueryKeyT>('getProjectLeads', args);
}

export const getProjectLeadsUrl = '/projects/leads/list/';

export const getProjectLeads = (args: GetProjectLeadsArgsT) => {
  return get(getProjectLeadsUrl).then((response) => {
    return waitOnDev(100, { projectLeads: response.data as ProjectT[] });
  });
};

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

export const invalidateGetProjectLeads = (
  args: GetProjectLeadsQueryKeyT = {}
) => {
  return queryClient.invalidateQueries({
    queryKey: getProjectLeadsQueryKey(args),
  });
};
