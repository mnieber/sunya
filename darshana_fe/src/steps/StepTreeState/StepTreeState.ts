import * as Skandha from 'skandha';
import { Data } from 'skandha-facets';
import { updateReconstructedActor } from '/src/actors/lib/updateReconstructedActor';
import { ActorT } from '/src/api/types/ActorT';
import { StepT } from '/src/api/types/StepT';

export type PropsT = {
  getRootStep: () => StepT | null;
};

type StepTreeDataT = {
  rootStep: StepT | null;
  reconstructed_actor: ActorT | null;
};

export class StepTreeState {
  props: PropsT;

  stepTreeCtr = {
    data: new Data<StepTreeDataT>(),
  };

  actions = {
    setHighlightedStep: (step: StepT) => {
      this.stepTreeCtr.data.reconstructed_actor =
        updateReconstructedActor(step);
    },
  };

  destroy() {
    Skandha.cleanUpCtr(this);
  }

  constructor(props: PropsT) {
    this.props = props;
    registerStepTreeCtr(this);
  }
}
