import { Route } from 'wouter';
import { BlogsPage } from '/src/blogs/components';
import { type BlogsRoutesT } from '/src/blogs/routeTable';
import { getRouteFns } from '/src/routes/routeTable';

export const BlogsSwitch = () => {
  const routeFns = getRouteFns<BlogsRoutesT>();

  return (
    <Route path={routeFns.blogList()}>
      <BlogsPage className="mx-auto my-auto" />
    </Route>
  );
};
