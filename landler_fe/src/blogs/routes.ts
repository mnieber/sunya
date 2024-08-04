import { history } from '/src/routes/history';
import { navHandler, RouteSpecT } from '/src/routes/navHandler';
import { generatePath } from '/src/routes/utils/generatePath';

export const blogsRoutes = {
  createBlog: () => '/blogs/create/_',
  blog: () => '/blogs/:blogSlug',
};

export class BlogsNav {
  blog(params: { blogSlug: string }, callerId?: string): RouteSpecT {
    return navHandler().run('blog', params, callerId);
  }
  createBlog(params: {}, callerId?: string): RouteSpecT {
    return navHandler().run('createBlog', params, callerId);
  }
}

export class DefaultBlogsNavHandler extends BlogsNav {
  blog(params: { blogSlug: string }, callerId?: string) {
    return {
      url: generatePath(blogsRoutes.blog(), params),
      nav: history.push,
    };
  }

  createBlog(params: {}, callerId?: string) {
    return {
      url: generatePath(blogsRoutes.createBlog(), params),
      nav: history.push,
    };
  }
}

export const blogsNav = new BlogsNav();
