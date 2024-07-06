import { useQuery } from '@tanstack/react-query';
import { get } from '/src/api/restClient';
import { wait } from '/src/utils/wait';

export type ArgsT = {
  blogId: string;
};

export const getBlogPosts = (args: ArgsT) => {
  return get(`/blogs/${args.blogId}/blog_posts`).then((response) => {
    return wait(import.meta.env.DEV ? 1000 : 0, response);
  });
};

export const useGetBlogPosts = () => {
  return useQuery({
    queryKey: ['getBlogPosts'],
    queryFn: () => getBlogPosts(),
  });
};
