import { Route, Switch } from 'wouter';
import { BlogsPage } from '/src/blogs/components';
import { framesRoutes } from '/src/frames/routes';

export const BlogsSwitch = () => {
  return (
    <Switch>
      <Route path={framesRoutes.dashboard()}>
        <BlogsPage className="grow" />
      </Route>
    </Switch>
  );
};
