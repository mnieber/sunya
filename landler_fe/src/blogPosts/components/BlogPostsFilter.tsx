/*
The BlogPostsFilter is very simple. It only toggles the value of blogPostsFiltering.isEnabled.

Note that because we are using MobX, and because the Skandha facets are made observable with
the registerCtr function from skandha-mobx, the component will update automatically when
the value of blogPostsFiltering.isEnabled changes.
*/

import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { blogPostsCtx } from '/src/blogPosts/hooks/useBlogPostsContext';
import { cn } from '/src/utils/classnames';

// Import styles
import './BlogPostsFilter.scss';

export type PropsT = {
  className?: any;
};

export const ContextProps = {
  blogPostsFiltering: blogPostsCtx.blogPostsFiltering,
};

export const BlogPostsFilter = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const toggleFilter = () =>
      props.blogPostsFiltering.setEnabled({
        flag: !props.blogPostsFiltering.isEnabled,
      });

    return (
      <div className={cn('BlogPostsFilter', 'flex flex-row items-center')}>
        <input
          className={cn('BlogPostListView__FilterCheckbox', 'mr-3')}
          type="checkbox"
          checked={props.blogPostsFiltering.isEnabled}
          onChange={() => toggleFilter()}
        />
        <div className="my-4 cursor-pointer" onClick={() => toggleFilter()}>
          Only show published blog posts
        </div>
      </div>
    );
  }, ContextProps)
);
