import { action, makeObservable, observable } from 'mobx';
import { stub } from 'skandha';

export class DashboardState {
  @observable buttonsPortalElm?: any = stub;

  @action setButtonsPortalElm = (elm: any) => {
    this.buttonsPortalElm = elm;
  };

  constructor() {
    makeObservable(this);
  }
}
