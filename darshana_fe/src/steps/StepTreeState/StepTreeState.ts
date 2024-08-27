import { action } from 'mobx';
import * as Skandha from 'skandha';
import { getReconstructedActor } from '/src/actors/lib/getReconstructedActor';
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
    setHighlightedActor: action((step: StepT, actorKey: string) => {
      this.stepTreeCtr.data.reconstructedActor = getReconstructedActor(
        step,
        actorKey
      );
    }),
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
