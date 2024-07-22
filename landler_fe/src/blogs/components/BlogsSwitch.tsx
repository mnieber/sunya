import { Route } from 'wouter';
import { BlogsPage } from '/src/blogs/components';
import { blogsRoutes } from '/src/blogs/routes';

export const BlogsSwitch = () => {
  return (
    <Route path={blogsRoutes.blogList()}>
      <BlogsPage className="" />
    </Route>
  );
};
