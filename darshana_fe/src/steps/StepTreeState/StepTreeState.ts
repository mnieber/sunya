import * as Skandha from 'skandha';
import { updateReconstructedActor } from '/src/actors/lib/updateReconstructedActor';
import { StepT } from '/src/api/types/StepT';
import { StepTreeData } from '/src/steps/StepTreeState/StepTreeData';
import { registerStepTreeCtr } from '/src/steps/StepTreeState/registerStepTreeCtr';
import { bindActionsCtr } from '/src/utils/bindActionsCtr';

export type PropsT = {
  getRootStep: () => StepT;
};

export class StepTreeState {
  props: PropsT;

  stepTreeCtr = {
    data: new StepTreeData(),
  };

  actions = {
    setHighlightedStep: (step: StepT) => {
      this.stepTreeCtr.data.reconstructedActor = updateReconstructedActor(step);
    },
  };

  destroy() {
    Skandha.cleanUpCtr(this);
  }

  constructor(props: PropsT) {
    this.props = props;
    bindActionsCtr(this.actions, this);
    registerStepTreeCtr(this);
  }
}
