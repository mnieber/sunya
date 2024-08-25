import { data, stub } from 'skandha';
import { ActorT } from '/src/api/types/ActorT';
import { StepT } from '/src/api/types/StepT';

export class StepTreeData {
  static className = () => 'StepTreeData';

  @data rootStep: StepT = stub();
  @data reconstructedActor: ActorT | null = null;
}
