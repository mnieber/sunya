import { history } from '/src/routes/history';
import { navHandler, RouteSpecT } from '/src/routes/navHandler';
import { generatePath } from '/src/routes/utils/generatePath';

export const authRoutes = {
  home: () => '/',
  signIn: () => '/sign-in',
};

export class AuthNav {
  home(params: {}, callerId?: string): RouteSpecT {
    return navHandler().run('home', params, callerId);
  }
  signIn(params: {}, callerId?: string): RouteSpecT {
    return navHandler().run('signIn', params, callerId);
  }
}

export class DefaultAuthNavHandler extends AuthNav {
  home(params: {}, callerId?: string) {
    return {
      url: generatePath(authRoutes.home(), {}),
      nav: history.push,
    };
  }
  signIn(params: {}, callerId?: string) {
    return {
      url: generatePath(authRoutes.signIn(), {}),
      nav: history.push,
    };
  }
}

export const authNav = new AuthNav();
