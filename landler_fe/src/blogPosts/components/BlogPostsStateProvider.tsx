/*
The BlogPostsStateProvider calls useBlogPostsState to instantiate the BlogPostsState.
It creates a cache object that exposes the blogPosts property, which is a tracked resource.
This resource is loading when the getBlogPosts query is loading, and updating if the
deleteBlogPosts mutation is running.
Finally, it exposes the contents of BlogPostsState as a set of default properties.

Continue by:
- reading the useBlogPostsState.tsx file.
- reading the BlogPostsState.ts file.
*/

import { makeAutoObservable } from 'mobx';
import { observer } from 'mobx-react-lite';
import React from 'react';
import { isRunning } from '/src/api/ObservableMutation';
import { isQueryLoading } from '/src/api/ObservableQuery';
import { BlogPostsContext } from '/src/blogPosts/hooks/useBlogPostsContext';
import { useBlogPostsState } from '/src/blogPosts/hooks/useBlogPostsState';
import { updateSources } from '/src/resourceStates';
import { createGetProps } from '/src/utils/createGetProps';
import { useBuilder } from '/src/utils/hooks/useBuilder';

export type PropsT = React.PropsWithChildren<{}>;

export const BlogPostsStateProvider = observer((props: PropsT) => {
  const { blogPostsState, getBlogPosts, deleteBlogPosts } = useBlogPostsState(
    {}
  );

  const cache = useBuilder(() =>
    makeAutoObservable({
      get blogPosts() {
        return updateSources(
          { resource: blogPostsState.blogPostsCtr.data.filteredBlogPosts },
          ['loading', () => isQueryLoading(getBlogPosts), 'getBlogPosts'],
          ['updating', () => isRunning(deleteBlogPosts), 'deleteBlogPosts']
        );
      },
    })
  );

  const getBlogPostsContext = () => {
    return createGetProps({
      blogPostsState: () => blogPostsState,
      blogPosts: () => cache.blogPosts,
      blogPostsDeletion: () => blogPostsState.blogPostsCtr.deletion,
      blogPostsFiltering: () => blogPostsState.blogPostsCtr.filtering,
      blogPostsHighlight: () => blogPostsState.blogPostsCtr.highlight,
      blogPostsSelection: () => blogPostsState.blogPostsCtr.selection,
    });
  };

  return (
    <BlogPostsContext.Provider value={getBlogPostsContext()}>
      {props.children}
    </BlogPostsContext.Provider>
  );
});
