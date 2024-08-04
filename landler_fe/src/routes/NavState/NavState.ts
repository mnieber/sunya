import { action, makeObservable, observable } from 'mobx';
import * as R from 'ramda';
import { history } from '/src/routes/history';
import { pathname } from '/src/utils/urls';

export class NavState {
  @observable navPoint?: {
    url: string;
  };

  @action storeNavPoint() {
    this.navPoint = {
      url: pathname(),
    };
  }

  @action restoreNavPoint() {
    if (R.isNil(this.navPoint)) return false;
    history.push(this.navPoint!.url);
    return true;
  }

  get hasNavPoint() {
    return !R.isNil(this.navPoint);
  }

  constructor() {
    makeObservable(this);
  }
}
