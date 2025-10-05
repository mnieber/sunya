import { useQuery } from '@tanstack/react-query';
import { z } from 'zod';
import { queryClient } from '/src/api/queryClient';
import { RoadmapSchema } from '/src/api/types/RoadmapSchema';
import { createQueryKey } from '/src/api/utils/createQueryKey';
import { parseResponse } from '/src/api/utils/parseResponse';
import { roadmapsData } from '/src/api/queries/roadmapsData';

export type GetRoadmapsArgsT = {};

export type QueryKeyT = GetRoadmapsArgsT;
export function getRoadmapsQueryKey(args: QueryKeyT) {
  return createQueryKey<QueryKeyT>('getRoadmaps', args);
}

export const getRoadmaps = (args: GetRoadmapsArgsT) => {
  return Promise.resolve().then(() => {
    const res = parseResponse(z.array(RoadmapSchema), roadmapsData);

    return { roadmaps: res };
  });
};

export const useGetRoadmaps = () => {
  return useQuery({
    queryKey: getRoadmapsQueryKey({}),
    queryFn: () => getRoadmaps({}),
  });
};

export const invalidateGetRoadmaps = (args: QueryKeyT) => {
  return queryClient.invalidateQueries({
    queryKey: getRoadmapsQueryKey(args),
  });
};
