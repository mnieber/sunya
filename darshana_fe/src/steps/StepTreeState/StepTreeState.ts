import { action } from 'mobx';
import * as Skandha from 'skandha';
import { getReconstructedActorByKey } from '/src/actors/lib/getReconstructedActorByKey';
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
      this.stepTreeCtr.data.reconstructedActorByKey =
        getReconstructedActorByKey(step, this.stepTreeCtr.data.stepById);

      const maybeRoleName = actorKey[0].toLowerCase() + actorKey.slice(1);
      const preActorKey = step.preActorKeyByRoleName[maybeRoleName];
      const postActorKey = step.postActorKeyByRoleName[maybeRoleName];

      if (preActorKey || postActorKey) {
        this.stepTreeCtr.data.actorContext = {
          step,
          roleName: actorKey,
          actorKey: preActorKey,
          otherActorKey: postActorKey,
        };
      } else {
        this.stepTreeCtr.data.actorContext = { step, actorKey };
      }
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
