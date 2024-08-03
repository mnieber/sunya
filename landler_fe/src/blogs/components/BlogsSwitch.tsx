import { Route, Switch } from 'wouter';
import { BlogsPage } from '/src/blogs/components';
import { BlogFormView } from '/src/blogs/components/BlogFormView';
import { CreateBlogEffect } from '/src/blogs/components/CreateBlogEffect';
import { blogsRoutes } from '/src/blogs/routes';

export const BlogsSwitch = () => {
  return (
    <Switch>
      <Route path={blogsRoutes.blogList()}>
        <BlogsPage className="grow" />
      </Route>
      <Route path={blogsRoutes.createBlog()}>
        <CreateBlogEffect />
        <BlogFormView className="grow" />
      </Route>
    </Switch>
  );
};
