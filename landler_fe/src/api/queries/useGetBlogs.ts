import { useQuery } from '@tanstack/react-query';
import { get } from '/src/api/restClient';
import { wait } from '/src/utils/wait';

export type ArgsT = {};

export const getBlogs = (args: ArgsT) => {
  return get(`/blogs/list`).then((response) => {
    return wait(import.meta.env.DEV ? 1000 : 0, { blogs: response.data });
  });
};

export const useGetBlogs = () => {
  return useQuery({
    queryKey: ['getBlogs'],
    queryFn: () => getBlogs({}),
  });
};
