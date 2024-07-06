import { useObservableMutation } from '/src/api/ObservableMutation';
import { queryClient } from '/src/api/queryClient';
import { ObjT } from '/src/utils/types';
import { wait } from '/src/utils/wait';

export type ArgsT = {
  blogPostIds: string[];
};

export const deleteBlogPosts = (args: ArgsT) => {
  return Promise.resolve({}).then((response: ObjT) => {
    return wait(import.meta.env.DEV ? 2000 : 0, response);
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
