import { history } from '/src/routes/history';
import { navHandler, RouteSpecT } from '/src/routes/navHandler';
import { generatePath } from '/src/routes/utils/generatePath';

export const atlasesRoutes = {
  atlas: () => '/atlases/:atlasId',
  atlases: () => '/atlases',
};

export class AtlasesNav {
  atlas(params: { atlasId: string }, callerId?: string): RouteSpecT {
    return navHandler().run('atlas', params, callerId);
  }
  atlases(params: {}, callerId?: string): RouteSpecT {
    return navHandler().run('atlases', params, callerId);
  }
}

export class DefaultAtlasesNavHandler extends AtlasesNav {
  atlas(params: { atlasId: string }, callerId?: string) {
    return {
      url: generatePath(atlasesRoutes.atlas(), params),
      nav: history.push,
    };
  }

  atlases(params: {}, callerId?: string) {
    return {
      url: generatePath(atlasesRoutes.atlases(), params),
      nav: history.push,
    };
  }
}

export const atlasesNav = new AtlasesNav();
