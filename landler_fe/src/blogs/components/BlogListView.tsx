import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { BlogT } from '/src/api/types';
import { BlogListViewItem } from '/src/blogs/components';
import { blogsCtx } from '/src/blogs/hooks/useBlogsContext';
import { L } from '/src/frames/layout';
import { isLoading } from '/src/resourceStates/getState';
import { cn } from '/src/utils/classnames';

// Import styles
import './BlogListView.scss';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  blogs: blogsCtx.blogs,
  blogsNav: blogsCtx.blogsNav,
};

export const BlogListView = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    if (isLoading(props.blogs)) {
      return <div>Loading...</div>;
    }

    const blogDivs = props.blogs.map((blog: BlogT) => {
      const { url } = props.blogsNav.toBlog(blog.slug);
      return <BlogListViewItem key={blog.id} blog={blog} url={url} />;
    });

    return (
      <div
        className={cn('BlogListView', [L.col.skewer(), 'p-4', props.className])}
        tabIndex={1}
      >
        {blogDivs}
      </div>
    );
  }, ContextProps)
);
