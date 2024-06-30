import { useQuery } from '@tanstack/react-query';
import { queryClient } from '/src/api/queryClient';
import getScenariosStub from '/src/api/stubs/getScenariosStub.json';
import { createQueryKey } from '/src/utils/createQueryKey';
import { ObjT } from '/src/utils/types';
import { wait } from '/src/utils/wait';

export type ArgsT = {};

export const getScenarios = (args: ArgsT) => {
  return Promise.resolve({ getScenarios: getScenariosStub }).then(
    (response: ObjT) => {
      return wait(import.meta.env.DEV ? 1000 : 0, response.getScenarios);
    }
  );
};

export type QueryKeyT = ArgsT;

export function queryKey(args: QueryKeyT) {
  return createQueryKey<QueryKeyT>('getScenarios', args);
}

export type OptionsT = {
  enabled?: boolean;
};

export const useGetScenarios = (args: ArgsT, options?: OptionsT) => {
  return useQuery({
    queryKey: queryKey(args),
    queryFn: () => getScenarios(args),
    enabled: !!(options?.enabled ?? true),
  });
};

export const invalidateGetScenarios = (args: QueryKeyT) => {
  return queryClient.invalidateQueries({
    queryKey: queryKey(args),
  });
};
