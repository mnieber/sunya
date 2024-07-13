import { makeAutoObservable } from 'mobx';
import { observer } from 'mobx-react-lite';
import React from 'react';
import { withContextProps } from 'react-props-from-context';
import { isRunning } from '/src/api/ObservableMutation';
import { isQueryLoading } from '/src/api/ObservableQuery';
import { BlogPostsContext } from '/src/blogPosts/hooks/useBlogPostsContext';
import { useBlogPostsState } from '/src/blogPosts/hooks/useBlogPostsState';
import { blogsCtx } from '/src/blogs/hooks/useBlogsContext';
import { updateSources } from '/src/resourceStates';
import { createGetProps } from '/src/utils/createGetProps';
import { useBuilder } from '/src/utils/hooks/useBuilder';

export type PropsT = React.PropsWithChildren<{}>;

const ContextProps = {
  blogsHighlight: blogsCtx.blogsHighlight,
};

export const BlogPostsStateProvider = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const { blogPostsState, getBlogPosts, deleteBlogPosts } = useBlogPostsState(
      { getBlog: () => props.blogsHighlight.item }
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
        blogPostsHighlight: () => blogPostsState.blogPostsCtr.highlight,
        blogPostsSelection: () => blogPostsState.blogPostsCtr.selection,
      });
    };

    return (
      <BlogPostsContext.Provider value={getBlogPostsContext()}>
        {props.children}
      </BlogPostsContext.Provider>
    );
  }, ContextProps)
);
