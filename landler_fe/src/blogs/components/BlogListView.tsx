import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { BlogT } from '/src/api/types';
import { BlogListViewItem } from '/src/blogs/components';
import { blogsCtx } from '/src/blogs/hooks/useBlogsContext';
import { isLoading } from '/src/resourceStates/getState';

// Import styles
import './BlogListView.scss';

export type PropsT = {};

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
      <div className="BlogListView" tabIndex={1}>
        {blogDivs}
      </div>
    );
  }, ContextProps)
);
