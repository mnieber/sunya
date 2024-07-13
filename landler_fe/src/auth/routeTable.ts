import { history } from '/src/routes/history';

import { RouteTable } from '/src/routes/utils/RouteTable';

export const getAuthRouteTable = () => {
  const routeTable = new RouteTable();
  routeTable.addRoutes(routes);
  return routeTable;
};

export const routes = {
  home: () => '/',
  signIn: () => '/sign-in',
};

export type AuthRoutesT = {
  home: () => string;
  signIn: () => string;
};

export class AuthNav {
  routeFns: AuthRoutesT;

  constructor(args: { routeFns: AuthRoutesT }) {
    this.routeFns = args.routeFns;
  }

  home() {
    return {
      url: this.routeFns.home(),
      nav: history.push,
    };
  }

  signIn() {
    return {
      url: this.routeFns.signIn(),
      nav: history.push,
    };
  }
}
