import { getAuthRouteTable } from '/src/auth/routeTable';
import { getBlogsRouteTable } from '/src/blogs/routeTable';
import { RouteFnByNameT, RouteTable } from '/src/routes/utils/RouteTable';

export const createRouteTable = () => {
  const routeTable = new RouteTable();
  routeTable.addTable(getAuthRouteTable(), '');
  routeTable.addTable(getBlogsRouteTable(), '');
  return routeTable;
};

export const routeTable = createRouteTable();

export const getRouteFns = <T>() => {
  return routeTable.routeFnByName as RouteFnByNameT<T>;
};
