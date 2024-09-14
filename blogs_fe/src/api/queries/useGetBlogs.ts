import { useQuery } from '@tanstack/react-query';
import { queryClient } from '/src/api/queryClient';
import { get } from '/src/api/restClient';
import { createQueryKey } from '/src/api/utils/createQueryKey';
import { waitOnDev } from '/src/utils/wait';

export type GetBlogsArgsT = {};

export type QueryKeyT = GetBlogsArgsT;
export function getBlogsQueryKey(args: QueryKeyT) {
  return createQueryKey<QueryKeyT>('getBlogs', args);
}

export const getBlogsUrl = `/blogs/list/`;

export const getBlogs = (args: GetBlogsArgsT) => {
  return get(getBlogsUrl).then((response) => {
    return waitOnDev(1000, { blogs: response.data });
  });
};

export const useGetBlogs = () => {
  return useQuery({
    queryKey: getBlogsQueryKey({}),
    queryFn: () => getBlogs({}),
  });
};

export const invalidateGetBlogs = (args: QueryKeyT) => {
  return queryClient.invalidateQueries({
    queryKey: getBlogsQueryKey(args),
  });
};
