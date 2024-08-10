import { history } from '/src/routes/history';
import { navHandler, RouteSpecT } from '/src/routes/navHandler';
import { generatePath } from '/src/routes/utils/generatePath';

export const mockUserSettingsRoutes = {
  userSettings: () => '/userSettings',
};

export class UserSettingsNav {
  userSettings(params: {}, callerId?: string): RouteSpecT {
    return navHandler().run('userSettings', params, callerId);
  }
}

export class DefaultUserSettingsNavHandler extends UserSettingsNav {
  userSettings(params: {}, callerId?: string) {
    return {
      url: generatePath(mockUserSettingsRoutes.userSettings(), params),
      nav: history.push,
    };
  }
}

export const userSettingsNav = new UserSettingsNav();
