import { action, computed, makeObservable, observable } from 'mobx';
import * as R from 'ramda';
import { States } from '/src/auth/endpoints/states';
import { ObjT } from '/src/utils/types';

const lutSuccess = {
  signIn: States.SIGN_IN_SUCCEEDED,
};

const lutFailure = {
  signIn: States.SIGN_IN_FAILED,
};

export class AuthState {
  @observable errors: string[] = [];
  @observable initialState: string;
  @observable state: string;
  @observable details: ObjT = {};

  constructor(initialState: string) {
    makeObservable(this);
    this.state = this.initialState = initialState;
  }

  @computed get hasErrors() {
    return !R.isEmpty(this.errors);
  }

  @action reset = () => {
    this.errors = [];
    this.state = this.initialState;
    this.details = {};
  };

  isTrackedQuery = (queryName: string) => {
    return ['signIn'].includes(queryName);
  };

  @action onUpdated(queryName: string, data: ObjT) {
    if (this.isTrackedQuery(queryName)) {
      this.errors = data.errors ?? [];
      this.state =
        data.errors && data.errors.length > 0
          ? (lutFailure[queryName as keyof typeof lutFailure] as string)
          : (lutSuccess[queryName as keyof typeof lutSuccess] as string);
    }
  }

  @action onUpdating(queryName: string) {
    if (this.isTrackedQuery(queryName)) {
      this.reset();
    }
  }

  @action onErrored(queryName: string, message: string) {
    if (this.isTrackedQuery(queryName)) {
      this.details = { message: message };
      this.errors = [lutFailure[queryName as keyof typeof lutFailure]];
      this.state = lutFailure[queryName as keyof typeof lutSuccess];
    }
  }
}
