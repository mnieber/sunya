import { history } from '/src/routes/history';
import { navHandler, RouteSpecT } from '/src/routes/navHandler';
import { generatePath } from '/src/routes/utils/generatePath';

export const roadmapsRoutes = {
  roadmap: () => '/roadmaps/:roadmapSlug',
  roadmaps: () => '/roadmaps',
};

export class RoadmapsNav {
  roadmap(params: { roadmapSlug: string }, callerId?: string): RouteSpecT {
    return navHandler().run('roadmap', params, callerId);
  }
  roadmaps(params: {}, callerId?: string): RouteSpecT {
    return navHandler().run('roadmaps', params, callerId);
  }
}

export class DefaultRoadmapsNavHandler extends RoadmapsNav {
  roadmap(params: { roadmapSlug: string }, callerId?: string) {
    return {
      url: generatePath(roadmapsRoutes.roadmap(), params),
      nav: history.push,
    };
  }

  roadmaps(params: {}, callerId?: string) {
    return {
      url: generatePath(roadmapsRoutes.roadmaps(), params),
      nav: history.push,
    };
  }
}

export const roadmapsNav = new RoadmapsNav();
