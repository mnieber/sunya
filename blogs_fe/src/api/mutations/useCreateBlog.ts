import { useObservableMutation } from '/src/api/lib/ObservableMutation';
import { invalidateGetBlogs } from '/src/api/queries/useGetBlogs';
import { post } from '/src/api/restClient';
import { ObjT } from '/src/utils/types';
import { waitOnDev } from '/src/utils/wait';

export type CreateBlogArgsT = {
  form: {
    name: string;
    description: string;
  };
};

export const createBlog = (args: CreateBlogArgsT) => {
  const url = `/blogs/create/`;
  return post(url, {
    createBlogForm: args.form,
  })
    .then((response) => {
      return waitOnDev(1000, response);
    })
    .catch((error) => {
      const errorCodes = error.response.data;
      if (errorCodes.includes('BLOG_WITH_NAME_EXISTS')) {
        return waitOnDev(1000, {
          success: false,
        });
      }

      throw error;
    });
};

export const useCreateBlog = () => {
  return useObservableMutation({
    mutationFn: createBlog,
    onSuccess: (response: ObjT, args: CreateBlogArgsT) => {
      invalidateGetBlogs({});
    },
  });
};
