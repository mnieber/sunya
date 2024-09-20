import { useQuery } from '@tanstack/react-query';
import { queryClient } from '/src/api/queryClient';
import { get } from '/src/api/restClient';
import { getPaginatedSchema } from '/src/api/types/PaginatedSchema';
import { PaginatedT } from '/src/api/types/PaginatedT';
import { ProjectLeadSchema } from '/src/api/types/ProjectLeadSchema';
import { ProjectLeadT } from '/src/api/types/ProjectLeadT';
import { createQueryKey } from '/src/api/utils/createQueryKey';
import { parseResponse } from '/src/api/utils/parseResponse';
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
    const schema = getPaginatedSchema(ProjectLeadSchema);
    const res = parseResponse(schema, response.data);

    return waitOnDev(100, {
      projectLeads: res as PaginatedT<ProjectLeadT>,
    });
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
