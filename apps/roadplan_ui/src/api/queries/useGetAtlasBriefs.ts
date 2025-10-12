import { useQuery } from '@tanstack/react-query';
import { z } from 'zod';
import { queryClient } from '/src/api/queryClient';
import { get } from '/src/api/restClient';
import { AtlasBriefSchema } from '/src/api/types/AtlasBriefSchema';
import { createQueryKey } from '/src/api/utils/createQueryKey';
import { parseResponse } from '/src/api/utils/parseResponse';
import { waitOnDev } from '/src/utils/wait';
import { parseAtlasBriefSchemas } from '/src/api/utils/parseAtlasBriefSchemas';

export type GetAtlasBriefsArgsT = {};

export type QueryKeyT = GetAtlasBriefsArgsT;
export function getAtlasBriefsQueryKey(args: QueryKeyT) {
  return createQueryKey<QueryKeyT>('getAtlasBriefs', args);
}

export const getAtlasBriefsUrl = `/atlas_briefs/list/`;

export const getAtlasBriefs = (args: GetAtlasBriefsArgsT) => {
  return get(getAtlasBriefsUrl).then((response) => {
    const res = parseResponse(z.array(AtlasBriefSchema), response.data);

    return waitOnDev(1000, { atlasBriefs: parseAtlasBriefSchemas(res) });
  });
};

export const useGetAtlasBriefs = () => {
  return useQuery({
    queryKey: getAtlasBriefsQueryKey({}),
    queryFn: () => getAtlasBriefs({}),
  });
};

export const invalidateGetAtlasBriefs = (args: QueryKeyT) => {
  return queryClient.invalidateQueries({
    queryKey: getAtlasBriefsQueryKey(args),
  });
};
