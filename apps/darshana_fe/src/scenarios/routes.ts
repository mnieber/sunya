import { history } from '/src/routes/history';
import { navHandler, RouteSpecT } from '/src/routes/navHandler';
import { generatePath } from '/src/routes/utils/generatePath';

export const scenariosRoutes = {
  scenario: () => '/projects/:projectId/scenarios/:scenarioId',
};

export class ScenariosNav {
  scenario(params: { projectId: string; scenarioId: string }, callerId?: string): RouteSpecT {
    return navHandler().run('scenario', params, callerId);
  }
}

export class DefaultScenariosNavHandler extends ScenariosNav {
  scenario(params: { projectId: string; scenarioId: string }, callerId?: string) {
    return {
      url: generatePath(scenariosRoutes.scenario(), params),
      nav: history.push,
    };
  }
}

export const scenariosNav = new ScenariosNav();
