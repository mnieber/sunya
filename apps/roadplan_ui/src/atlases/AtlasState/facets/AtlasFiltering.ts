import { data, operation } from 'skandha';

export class AtlasFiltering {
  static className = () => 'AtlasFiltering';

  @data showCompletedMilestones: boolean = false;
  @data showFutureMilestones: boolean = false;

  @operation toggleShowCompletedMilestones(args: { value?: boolean }) {
    this.showCompletedMilestones =
      args.value !== undefined ? args.value : !this.showCompletedMilestones;
  }

  @operation toggleShowFutureMilestones(args: { value?: boolean }) {
    this.showFutureMilestones =
      args.value !== undefined ? args.value : !this.showFutureMilestones;
  }
}
