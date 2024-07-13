import * as R from 'ramda';
import React from 'react';
import { Deletion, Highlight, Selection } from 'skandha-facets';
import { BlogPostT } from '/src/api/types';
import { BlogPostsState } from '/src/blogPosts/BlogPostsState';

export const BlogPostsContext = React.createContext<any>(null);

export const useBlogPostsContext = () => {
  const context = React.useContext(BlogPostsContext);
  if (!context) {
    throw new Error(
      'useBlogPostsContext must be used within a BlogPostsContext.Provider'
    );
  }
  return context;
};

export const blogPostsCtx = R.mergeAll([
  {
    blogPostsState: [
      useBlogPostsContext,
      'blogPostsState',
    ] as any as BlogPostsState,
    blogPosts: [useBlogPostsContext, 'blogPosts'] as any as BlogPostT[],
    blogPostsDeletion: [
      useBlogPostsContext,
      'blogPostsDeletion',
    ] as any as Deletion,
    blogPostsHighlight: [
      useBlogPostsContext,
      'blogPostsHighlight',
    ] as any as Highlight,
    blogPostsSelection: [
      useBlogPostsContext,
      'blogPostsSelection',
    ] as any as Selection,
  },
]);
