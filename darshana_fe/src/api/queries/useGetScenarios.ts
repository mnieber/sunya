import { useQuery } from '@tanstack/react-query';
import { queryClient } from '/src/api/queryClient';
import { get } from '/src/api/restClient';
import { createQueryKey } from '/src/api/utils/createQueryKey';
import { waitOnDev } from '/src/utils/wait';

export type GetScenariosArgsT = {};

export const getScenarios = (args: GetScenariosArgsT) => {
  return get(`/scenarios/list/`).then((response) => {
    return waitOnDev(100, { scenarios: response.data });
  });
};

export type OptionsT = {
  enabled?: boolean;
};

export type QueryKeyT = GetScenariosArgsT;

export function getScenariosQueryKey(args: QueryKeyT) {
  return createQueryKey<QueryKeyT>('getScenarios', args);
}

export const useGetScenarios = (
  args: GetScenariosArgsT,
  options?: OptionsT
) => {
  return useQuery({
    queryKey: getScenariosQueryKey(args),
    queryFn: () => getScenarios(args),
    enabled: !!(options?.enabled ?? true),
  });
};

export const invalidateGetScenarios = (args: QueryKeyT) => {
  return queryClient.invalidateQueries({
    queryKey: getScenariosQueryKey(args),
  });
};
