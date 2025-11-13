import { history } from '/src/routes/history';
import { navHandler, RouteSpecT } from '/src/routes/navHandler';
import { generatePath } from '/src/routes/utils/generatePath';

export const jiraRoutes = {
  syncAtlasWithJira: () => '/jira/sync-atlas',
};

export class JiraNav {
  syncAtlasWithJira(params: {}, callerId?: string): RouteSpecT {
    return navHandler().run('syncAtlasWithJira', params, callerId);
  }
}

export class DefaultJiraNavHandler extends JiraNav {
  syncAtlasWithJira(params: {}, callerId?: string) {
    return {
      url: generatePath(jiraRoutes.syncAtlasWithJira(), params),
      nav: history.push,
    };
  }
}

export const jiraNav = new JiraNav();
