import { useQuery } from '@tanstack/react-query';
import { get } from '/src/api/restClient';
import { wait } from '/src/utils/wait';

export type ArgsT = {
  blogSlug: string;
};

export const getBlogPosts = (args: ArgsT) => {
  return get(`/blogs/${args.blogSlug}/blog-posts/list`).then((response) => {
    return wait(import.meta.env.DEV ? 1000 : 0, { blogPosts: response.data });
  });
};

export type OptionsT = {
  enabled?: boolean;
};

export const useGetBlogPosts = (args: ArgsT, options?: OptionsT) => {
  return useQuery({
    queryKey: ['getBlogPosts', args.blogSlug],
    queryFn: () => getBlogPosts(args),
    enabled: !!(options?.enabled ?? true),
  });
};
