import { history } from '/src/routes/history';
import { navHandler, RouteSpecT } from '/src/routes/navHandler';
import { generatePath } from '/src/routes/utils/generatePath';

export const projectsRoutes = {
  projects: () => '/projects',
  project: () => '/projects/:projectId',
};

export class ProjectsNav {
  projects(params: {}, callerId?: string): RouteSpecT {
    return navHandler().run('projects', params, callerId);
  }
  project(params: { projectId: string }, callerId?: string): RouteSpecT {
    return navHandler().run('project', params, callerId);
  }
}

export class DefaultProjectsNavHandler extends ProjectsNav {
  projects(params: {}, callerId?: string) {
    return {
      url: generatePath(projectsRoutes.projects(), params),
      nav: history.push,
    };
  }

  project(params: { projectId: string }, callerId?: string) {
    return {
      url: generatePath(projectsRoutes.project(), params),
      nav: history.push,
    };
  }
}

export const projectsNav = new ProjectsNav();
