/*
The useBlogPostsState function is a hook that creates the BlogPostsState.
It creates a ObservableQuery (getBlogPosts) and an ObservableMutation (deleteBlogPosts).
When it creates the BlogPostsState, it implements the getBlogPosts and deleteBlogPosts methods that
connect the BlogPostsState to the "outside world".
The trackPromise function is used to put the selected blogPost's in an "updating" state while
the deleteBlogPosts mutation is in progress.

You can continue by:

- diving into the details (e.g. useGraftResourceStatesFromMemo, or trackPromise), or
- returning to BlogPostsStateProvider.tsx.

On a first reading, it's probably best to return to BlogPostsStateProvider.tsx.
*/

import React from 'react';
import { useDeleteBlogPosts } from '/src/api/endpoints';
import { useObservableQuery } from '/src/api/hooks';
import { DeleteBlogPostsArgsT } from '/src/api/mutations';
import { useGetBlogPosts } from '/src/api/queries/useGetBlogPosts';
import { BlogPostT } from '/src/api/types';
import { BlogPostsState } from '/src/blogPosts/BlogPostsState';
import { trackPromise } from '/src/resourceStates/trackPromise';
import { useBuilder } from '/src/utils/hooks/useBuilder';
import { useGraftResourceStatesFromMemo } from '/src/utils/hooks/useGraftResourceStatesFromMemo';
import { lookUp } from '/src/utils/ids';

export type PropsT = {};

export const useBlogPostsState = (props: PropsT) => {
  const graftResourceStatesFromMemo = useGraftResourceStatesFromMemo({});

  // Mutations
  const deleteBlogPosts = useDeleteBlogPosts();

  // Queries
  const getBlogPosts = useObservableQuery(useGetBlogPosts(), {
    fetchAsLoad: true,
    debugLabel: 'getBlogPosts',
  });

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
            blogPostIds: ids,
          } as DeleteBlogPostsArgsT),
        }).result;
      },
    });

    // Initialize state.blogPostsCtr.filtering
    state.blogPostsCtr.filtering.apply({
      filter: (blogPosts: BlogPostT[]) => {
        return blogPosts.filter((x: BlogPostT) => x.state === 'done');
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
