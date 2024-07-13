import { makeAutoObservable } from 'mobx';
import { observer } from 'mobx-react-lite';
import React from 'react';
import { isQueryLoading } from '/src/api/ObservableQuery';
import { BlogsContext } from '/src/blogs/hooks/useBlogsContext';
import { useBlogsState } from '/src/blogs/hooks/useBlogsState';
import { BlogsNav, BlogsRoutesT } from '/src/blogs/routeTable';
import { updateSources } from '/src/resourceStates';
import { getRouteFns } from '/src/routes/routeTable';
import { createGetProps } from '/src/utils/createGetProps';
import { useBuilder } from '/src/utils/hooks/useBuilder';

export type PropsT = React.PropsWithChildren<{}>;

export const BlogsStateProvider = observer((props: PropsT) => {
  const { blogsState, getBlogs } = useBlogsState({});

  const cache = useBuilder(() =>
    makeAutoObservable({
      get blog() {
        return updateSources(
          {
            resource: blogsState.blogsCtr.highlight.item,
            resourceName: 'blog',
          },
          ['loading', () => isQueryLoading(getBlogs), 'blog']
        );
      },
      get blogs() {
        return updateSources({ resource: blogsState.blogsCtr.data.blogs }, [
          'loading',
          () => isQueryLoading(getBlogs),
          'getBlogs',
        ]);
      },
    })
  );

  const blogsNav = useBuilder(
    () => new BlogsNav({ routeFns: getRouteFns<BlogsRoutesT>() })
  );

  const getBlogsContext = () => {
    return createGetProps({
      blogsState: () => blogsState,
      blogs: () => cache.blogs,
      blog: () => cache.blog,
      blogsHighlight: () => blogsState.blogsCtr.highlight,
      blogsSelection: () => blogsState.blogsCtr.selection,
      blogsNav: () => blogsNav,
    });
  };

  return (
    <BlogsContext.Provider value={getBlogsContext()}>
      {props.children}
    </BlogsContext.Provider>
  );
});
