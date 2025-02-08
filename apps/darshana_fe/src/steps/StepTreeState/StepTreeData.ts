import { data } from 'skandha';
import { ActorByKeyT } from '/src/api/types/ActorT';
import { StepT } from '/src/api/types/StepT';

export type ActorContextT = {
  step: StepT;
  actorKey: string;
  otherActorKey?: string;
  roleName?: string;
};

export class StepTreeData {
  static className = () => 'StepTreeData';

  @data rootStep: StepT | null = null;
  @data reconstructedActorByKey: ActorByKeyT | null = null;
  @data actorContext: ActorContextT | null = null;
  @data get stepById() {
    const result: { [id: string]: StepT } = {};

    const traverseSteps = (step: StepT | null) => {
      if (step) {
        result[step.id] = step;
        step.childSteps.forEach(traverseSteps);
      }
    };

    traverseSteps(this.rootStep);
    return result;
  }
}
