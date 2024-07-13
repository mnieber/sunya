import React from 'react';
import { useDeleteBlogPosts } from '/src/api/endpoints';
import { useObservableQuery } from '/src/api/hooks';
import { DeleteBlogPostsArgsT } from '/src/api/mutations';
import { useGetBlogPosts } from '/src/api/queries/useGetBlogPosts';
import { BlogPostT } from '/src/api/types';
import { BlogT } from '/src/api/types/BlogT';
import { BlogPostsState } from '/src/blogPosts/BlogPostsState';
import { trackPromise } from '/src/resourceStates/trackPromise';
import { useBuilder } from '/src/utils/hooks/useBuilder';
import { useGraftResourceStatesFromMemo } from '/src/utils/hooks/useGraftResourceStatesFromMemo';
import { lookUp } from '/src/utils/ids';

export type PropsT = {
  getBlog: () => BlogT | undefined;
};

export const useBlogPostsState = (props: PropsT) => {
  const graftResourceStatesFromMemo = useGraftResourceStatesFromMemo({});

  // Mutations
  const deleteBlogPosts = useDeleteBlogPosts();

  // Queries
  const getBlogPosts = useObservableQuery(
    useGetBlogPosts(
      { blogSlug: props.getBlog()?.slug ?? '' },
      { enabled: !!props.getBlog() }
    ),
    {
      fetchAsLoad: true,
      debugLabel: 'getBlogPosts',
    }
  );

  const blogPostsState = useBuilder(() => {
    const state = new BlogPostsState({
      //
      getBlogPosts: () => {
        return graftResourceStatesFromMemo({
          resources: getBlogPosts.data?.blogPosts ?? [],
        });
      },
      //
      deleteBlogPosts: (ids: string[]) => {
        const blogPosts = lookUp(
          ids,
          blogPostsState.blogPostsCtr.data.blogPostById
        );
        return trackPromise({
          name: 'deleteBlogPosts',
          states: { updating: blogPosts },
          promise: deleteBlogPosts.mutateAsync({
            blog: props.getBlog(),
            blogPostIds: ids,
          } as DeleteBlogPostsArgsT),
        }).result;
      },
    });

    state.blogPostsCtr.filtering.apply({
      filter: (blogPosts: BlogPostT[]) => {
        return blogPosts.filter((x: BlogPostT) => x.isPublished);
      },
    });
    state.blogPostsCtr.filtering.setEnabled({ flag: false });

    return state;
  }) as BlogPostsState;

  React.useEffect(() => () => blogPostsState.destroy(), [blogPostsState]);

  return {
    blogPostsState,
    getBlogPosts,
    deleteBlogPosts,
  };
};
