import { Redirect, Route, Switch } from 'wouter';
import { SignInPage } from '/src/auth/components/SignInPage';
import { authRoutes } from '/src/auth/routes';

export const AuthSwitch = () => {
  return (
    <Switch>
      <Route path={authRoutes.home()}>
        <Redirect to="/blogs" />
      </Route>
      <Route path={authRoutes.signIn()}>
        <SignInPage />
      </Route>
    </Switch>
  );
};
