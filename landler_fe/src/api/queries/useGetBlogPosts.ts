import { useQuery } from '@tanstack/react-query';
import { queryClient } from '/src/api/queryClient';
import { get } from '/src/api/restClient';
import { createQueryKey } from '/src/auth/utils/createQueryKey';
import { waitOnDev } from '/src/utils/wait';

export type ArgsT = {
  blogSlug: string;
};

export const getBlogPosts = (args: ArgsT) => {
  return get(`/blogs/${args.blogSlug}/blog-posts/list/`).then((response) => {
    return waitOnDev(100, { blogPosts: response.data });
  });
};

export type OptionsT = {
  enabled?: boolean;
};

export type QueryKeyT = ArgsT;

export function getBlogPostsQueryKey(args: QueryKeyT) {
  return createQueryKey<QueryKeyT>('getBlogPosts', args);
}

export const useGetBlogPosts = (args: ArgsT, options?: OptionsT) => {
  return useQuery({
    queryKey: getBlogPostsQueryKey(args),
    queryFn: () => getBlogPosts(args),
    enabled: !!(options?.enabled ?? true),
  });
};

export const invalidateGetBlogPosts = (args: QueryKeyT) => {
  return queryClient.invalidateQueries({
    queryKey: getBlogPostsQueryKey(args),
  });
};
