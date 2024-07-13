import { useObservableMutation } from '/src/api/ObservableMutation';
import { queryClient } from '/src/api/queryClient';
import { post } from '/src/api/restClient';
import { BlogT } from '/src/api/types/BlogT';
import { ObjT } from '/src/utils/types';
import { wait } from '/src/utils/wait';

export type ArgsT = {
  blog: BlogT;
  blogPostIds: string[];
};

export const deleteBlogPosts = (args: ArgsT) => {
  const url = `/blogs/${args.blog.id}/blog-posts/delete/`;
  return post(url, {
    deleteBlogPostsForm: {
      blogPostIds: args.blogPostIds,
    },
  }).then((response) => {
    return wait(import.meta.env.DEV ? 1000 : 0, {});
  });
};

export const useDeleteBlogPosts = () => {
  return useObservableMutation({
    mutationFn: deleteBlogPosts,
    onSuccess: (response: ObjT, args: ArgsT) => {
      queryClient.setQueryData(['getBlogPosts'], (data: any) => {
        return {
          blogPosts: data.blogPosts.filter(
            (x: any) => !args.blogPostIds.includes(x.id)
          ),
        };
      });
    },
  });
};
