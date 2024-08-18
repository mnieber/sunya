import { useObservableMutation } from '/src/api/lib/ObservableMutation';
import { invalidateGetBlogPosts } from '/src/api/queries/useGetBlogPosts';
import { post } from '/src/api/restClient';
import { BlogT } from '/src/api/types/BlogT';
import { ObjT } from '/src/utils/types';
import { waitOnDev } from '/src/utils/wait';

export type CreateBlogPostArgsT = {
  blog: BlogT;
  form: {
    title: string;
    content: string;
  };
};

export const createBlogPost = (args: CreateBlogPostArgsT) => {
  const url = `/blogs/${args.blog.id}/blog-posts/create/`;
  return post(url, {
    createBlogPostForm: args.form,
    blogId: args.blog.id,
  })
    .then((response) => {
      return waitOnDev(1000, response);
    })
    .catch((error) => {
      const errorCodes = error.response.data;
      if (errorCodes.includes('BLOG_NOT_FOUND')) {
        return waitOnDev(1000, {
          success: false,
        });
      }

      throw error;
    });
};

export const useCreateBlogPost = () => {
  return useObservableMutation({
    mutationFn: createBlogPost,
    onSuccess: (response: ObjT, args: CreateBlogPostArgsT) => {
      invalidateGetBlogPosts({ blogSlug: args.blog.slug });
    },
  });
};
