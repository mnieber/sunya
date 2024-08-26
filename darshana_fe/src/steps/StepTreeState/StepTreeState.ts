import * as Skandha from 'skandha';
import { getReconstructedActor } from '/src/actors/lib/getReconstructedActor';
import { ActorT } from '/src/api/types/ActorT';
import { StepT } from '/src/api/types/StepT';
import { StepTreeData } from '/src/steps/StepTreeState/StepTreeData';
import { registerStepTreeCtr } from '/src/steps/StepTreeState/registerStepTreeCtr';
import { bindActionsCtr } from '/src/utils/bindActionsCtr';

export type PropsT = {
  getRootStep: () => StepT | null;
};

export class StepTreeState {
  props: PropsT;

  stepTreeCtr = {
    data: new StepTreeData(),
  };

  actionsCtr = {
    setHighlightedActor: (step: StepT, actor: ActorT) => {
      this.stepTreeCtr.data.reconstructedActor = getReconstructedActor(
        step,
        actor
      );
    },
  };

  destroy() {
    Skandha.cleanUpCtr(this);
  }

  constructor(props: PropsT) {
    this.props = props;
    bindActionsCtr(this.actionsCtr, this);
    registerStepTreeCtr(this);
  }
}
