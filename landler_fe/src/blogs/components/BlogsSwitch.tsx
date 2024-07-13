import { Route } from 'wouter';
import { BlogPostListView } from '/src/blogPosts/components';
import { DeleteBlogPostsButton } from '/src/blogPosts/components/DeleteBlogPostsButton';
import {
  BlogListView,
  BlogsPage,
  SelectBlogEffect,
} from '/src/blogs/components';
import { type BlogsRoutesT } from '/src/blogs/routeTable';
import { getRouteFns } from '/src/routes/routeTable';
import { cn } from '/src/utils/classnames';

export const BlogsSwitch = () => {
  const routeFns = getRouteFns<BlogsRoutesT>();

  return (
    <Route path={routeFns.blogList()}>
      <BlogsPage className="flex-grow">
        <BlogListView />
        <Route path={routeFns.blog()}>
          <SelectBlogEffect />
          <div className={cn('flex flex-col items-center')}>
            <BlogPostListView />
            <DeleteBlogPostsButton className="mt-8" />
          </div>
        </Route>
      </BlogsPage>
    </Route>
  );
};
