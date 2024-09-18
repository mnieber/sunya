import { data } from 'skandha';
import { ActorT } from '/src/api/types/ActorT';
import { StepT } from '/src/api/types/StepT';

export class StepTreeData {
  static className = () => 'StepTreeData';

  @data rootStep: StepT | null = null;
  @data reconstructedActor: ActorT | null = null;
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
