import { observable } from 'mobx';

export const flags = observable({
  logQueries: true,
  logSkandha: true,
  logResourceStates: true,
});
