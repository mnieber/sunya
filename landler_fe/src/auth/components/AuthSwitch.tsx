import { Redirect, Route, Switch } from 'wouter';
import { SignInPage } from '/src/auth/components/SignInPage';
import { type AuthRoutesT } from '/src/auth/routeTable';
import { type BlogsRoutesT } from '/src/blogs/routeTable';
import { getRouteFns } from '/src/routes/routeTable';

export const AuthSwitch = () => {
  const routeFns = getRouteFns<BlogsRoutesT & AuthRoutesT>();

  return (
    <Switch>
      <Route path={routeFns.home()}>
        <Redirect to="/blogs" />
      </Route>
      <Route path={routeFns.signIn()}>
        <SignInPage />
      </Route>
    </Switch>
  );
};
