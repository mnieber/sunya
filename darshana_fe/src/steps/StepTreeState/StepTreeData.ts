import { data } from 'skandha';
import { ActorT } from '/src/api/types/ActorT';
import { StepT } from '/src/api/types/StepT';

export class StepTreeData {
  static className = () => 'StepTreeData';

  @data rootStep: StepT | null = null;
  @data reconstructedActor: ActorT | null = null;
}
