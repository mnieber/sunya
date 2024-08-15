import * as Skandha from 'skandha';
import { Highlight, Store } from 'skandha-facets';
import { StepT } from '/src/api/types/StepT';

// Local imports
import { registerStepsCtr } from './registerStepsCtr';

export type PropsT = {
  getSteps: () => StepT[];
};

export class StepsState {
  props: PropsT;

  stepsCtr = {
    highlight: new Highlight<StepT>(),
    store: new Store<StepT>(),
  };

  getSummary() {
    return {
      steps: Skandha.getCtrState(this.stepsCtr),
    };
  }

  destroy() {
    Skandha.cleanUpCtr(this);
  }

  constructor(props: PropsT) {
    this.props = props;
    registerStepsCtr(this);
  }
}
