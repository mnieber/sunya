import { history } from '/src/routes/history';
import { navHandler, RouteSpecT } from '/src/routes/navHandler';
import { generatePath } from '/src/routes/utils/generatePath';

export const resultsRoutes = {};

export class ResultsNav {}

export class DefaultResultsNavHandler extends ResultsNav {}

export const resultsNav = new ResultsNav();
