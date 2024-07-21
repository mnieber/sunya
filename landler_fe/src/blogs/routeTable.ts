import { history } from '/src/routes/history';
import { RouteTable } from '/src/routes/utils/RouteTable';

export const getBlogsRouteTable = () => {
  const routeTable = new RouteTable();
  routeTable.addRoutes(routes);
  return routeTable;
};

export const routes = {
  blogList: () => '/blogs/:blogSlug?',
  blog: () => '/blogs/:blogSlug',
};

export type BlogsRoutesT = {
  blogList: () => string;
  blog: (params: { blogSlug: string }) => string;
};

export class BlogsNav {
  routeFns: BlogsRoutesT;

  constructor(args: { routeFns: BlogsRoutesT }) {
    this.routeFns = args.routeFns;
  }

  toBlogList() {
    return {
      url: this.routeFns.blogList(),
      nav: history.push,
    };
  }

  toBlog(blogSlug: string) {
    return {
      url: this.routeFns.blog({ blogSlug }),
      nav: history.push,
    };
  }
}
