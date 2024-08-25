import { useQuery } from '@tanstack/react-query';
import { queryClient } from '/src/api/queryClient';
import { get } from '/src/api/restClient';
import { createQueryKey } from '/src/api/utils/createQueryKey';
import { waitOnDev } from '/src/utils/wait';

export type GetBlogsArgsT = {};

export const getBlogs = (args: GetBlogsArgsT) => {
  return get(`/blogs/list/`).then((response) => {
    return waitOnDev(1000, { blogs: response.data });
  });
};

export type QueryKeyT = GetBlogsArgsT;

export function getBlogsQueryKey(args: QueryKeyT) {
  return createQueryKey<QueryKeyT>('getBlogs', args);
}

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
