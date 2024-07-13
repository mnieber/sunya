import React from 'react';
import { useObservableQuery } from '/src/api/hooks';
import { useGetBlogs } from '/src/api/queries/useGetBlogs';
import { BlogsState } from '/src/blogs/BlogsState';
import { useBuilder } from '/src/utils/hooks/useBuilder';
import { useGraftResourceStatesFromMemo } from '/src/utils/hooks/useGraftResourceStatesFromMemo';

export type PropsT = {};

export const useBlogsState = (props: PropsT) => {
  const graftResourceStatesFromMemo = useGraftResourceStatesFromMemo({});

  // Queries
  const getBlogs = useObservableQuery(useGetBlogs(), {
    fetchAsLoad: true,
    debugLabel: 'getBlogs',
  });

  const blogsState = useBuilder(() => {
    const state = new BlogsState({
      //
      getBlogs: () => {
        return graftResourceStatesFromMemo({
          resources: getBlogs.data?.blogs ?? [],
        });
      },
    });

    return state;
  }) as BlogsState;

  React.useEffect(() => () => blogsState.destroy(), [blogsState]);

  return {
    blogsState,
    getBlogs,
  };
};
