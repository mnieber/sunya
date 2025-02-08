import { observer } from 'mobx-react-lite';
import { Route, Switch } from 'wouter';
import { MockUserSettingsPage } from '/src/mocks/userSettings/components/MockUserSettingsPage';
import { mockUserSettingsRoutes } from '/src/mocks/userSettings/routes';
import { ext } from '/src/routes/navHandler';

type PropsT = {};

export const MockUserSettingsSwitch = observer((props: PropsT) => {
  return (
    <Switch>
      <Route path={ext(mockUserSettingsRoutes.userSettings())}>
        <MockUserSettingsPage />
      </Route>
    </Switch>
  );
});
