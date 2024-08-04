import { Route, Switch } from 'wouter';
import { BlogsPage } from '/src/blogs/components';
import { framesRoutes } from '/src/frames/routes';
import { ext } from '/src/routes/navHandler';

export const BlogsSwitch = () => {
  return (
    <Switch>
      <Route path={ext(framesRoutes.dashboard())}>
        <BlogsPage className="grow" />
      </Route>
    </Switch>
  );
};
