import { useObservableMutation } from '/src/api/lib/ObservableMutation';
import { get } from '/src/api/restClient';
import { createQueryKey } from '/src/auth/utils/createQueryKey';
import { waitOnDev } from '/src/utils/wait';

export type GetBlogTagsArgsT = {
  inputValue: string;
};

export const getBlogTags = (args: GetBlogTagsArgsT) => {
  return get(`/blogs/tags/?inputValue=${args.inputValue}`).then((response) => {
    return waitOnDev(1000, response.data);
  });
};

export type QueryKeyT = GetBlogTagsArgsT;

export function getBlogTagsQueryKey(args: QueryKeyT) {
  return createQueryKey<QueryKeyT>('getBlogTags', args);
}

export const useGetBlogTags = () => {
  return useObservableMutation({
    mutationFn: getBlogTags,
  });
};
