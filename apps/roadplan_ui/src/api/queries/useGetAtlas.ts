import { generatePath } from '/src/routes/utils/generatePath';
import { useQuery } from '@tanstack/react-query';
import { queryClient } from '/src/api/queryClient';
import { get } from '/src/api/restClient';
import { AtlasSchema } from '/src/api/types/AtlasSchema';
import { createQueryKey } from '/src/api/utils/createQueryKey';
import { parseResponse } from '/src/api/utils/parseResponse';
import { parseAtlasSchema } from '/src/api/utils/parseAtlasSchema';
import { waitOnDev } from '/src/utils/wait';

export type GetAtlasArgsT = {
  atlasId: string;
};
export type OptionsT = {
  enabled?: boolean;
};

export type QueryKeyT = GetAtlasArgsT;
export function getAtlasQueryKey(args: QueryKeyT) {
  return createQueryKey<QueryKeyT>('getAtlas', args);
}

export const getAtlasUrl = `/atlases/:atlasId/`;

export const getAtlas = (args: GetAtlasArgsT) => {
  return get(generatePath(getAtlasUrl, { atlasId: args.atlasId })).then(
    (response) => {
      const res = parseResponse(AtlasSchema, response.data);

      return waitOnDev(1000, { atlas: parseAtlasSchema(res) });
    }
  );
};

export const useGetAtlas = (args: GetAtlasArgsT, options: OptionsT) => {
  return useQuery({
    queryKey: getAtlasQueryKey(args),
    queryFn: () => getAtlas(args),
    enabled: !!(options?.enabled ?? true),
  });
};

export const invalidateGetAtlas = (args: QueryKeyT) => {
  return queryClient.invalidateQueries({
    queryKey: getAtlasQueryKey(args),
  });
};
