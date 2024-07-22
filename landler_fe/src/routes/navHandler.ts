import { DefaultAuthNavHandler } from '/src/auth/routes';
import { DefaultBlogsNavHandler } from '/src/blogs/routes';

export type RouteSpecT = {
  url: string;
  nav: (url: string) => void;
};

export class NavHandler {
  navHandlers: any[] = [];
  defaultNavHandlers: any[] = [];

  installNavHandler(navHandler: any) {
    this.navHandlers.push(navHandler);
  }

  installDefaultNavHandler(navHandler: any) {
    this.defaultNavHandlers.push(navHandler);
  }

  run(name: string, params: any, callerId?: string) {
    for (const handlers of [this.navHandlers, this.defaultNavHandlers]) {
      for (const navHandler of handlers) {
        const handlerFn = navHandler[name];
        if (!handlerFn) {
          continue;
        }

        const result = handlerFn(params, callerId);
        if (result) {
          return result;
        }
      }
    }
    throw new Error(`No nav handler found for ${name}`);
  }
}

export const navTo = (routeAndNav: RouteSpecT) => {
  routeAndNav.nav(routeAndNav.url);
};

export const createNavHandler = () => {
  const navHandler = new NavHandler();
  navHandler.installDefaultNavHandler(new DefaultBlogsNavHandler());
  navHandler.installDefaultNavHandler(new DefaultAuthNavHandler());
  return navHandler;
};

let _navHandler: NavHandler | undefined = undefined;

export const navHandler = () => {
  if (!_navHandler) {
    _navHandler = createNavHandler();
  }
  return _navHandler;
};
