import { useObservableMutation } from '/src/api/lib/ObservableMutation';
import { invalidateGetBlogPosts } from '/src/api/queries/useGetBlogPosts';
import { post } from '/src/api/restClient';
import { BlogPostT } from '/src/api/types';
import { BlogT } from '/src/api/types/BlogT';
import { ObjT } from '/src/utils/types';
import { waitOnDev } from '/src/utils/wait';

export type UpdateBlogPostArgsT = {
  blog: BlogT;
  blogPost: BlogPostT;
  form: {
    title?: string;
    content?: string;
  };
};

export const updateBlogPost = (args: UpdateBlogPostArgsT) => {
  const url = `/blogs/${args.blog.id}/blog-posts/${args.blogPost.id}/update/`;
  return post(url, {
    updateBlogPostForm: args.form,
    blogId: args.blog.id,
    blogPostId: args.blogPost.id,
  })
    .then((response) => {
      return waitOnDev(1000, response);
    })
    .catch((error) => {
      const errorCodes = error.response.data;
      if (errorCodes.includes('BLOG_NOT_FOUND')) {
        // TODO return this error and use it in UpdateBlogPostForm
        return waitOnDev(1000, {
          success: false,
        });
      }
      if (errorCodes.includes('BLOG_POST_NOT_FOUND')) {
        // TODO return this error and use it in UpdateBlogPostForm
        return waitOnDev(1000, {
          success: false,
        });
      }

      throw error;
    });
};

export const useUpdateBlogPost = () => {
  return useObservableMutation({
    mutationFn: updateBlogPost,
    onSuccess: (response: ObjT, args: UpdateBlogPostArgsT) => {
      invalidateGetBlogPosts({ blogSlug: args.blog.slug });
    },
  });
};
