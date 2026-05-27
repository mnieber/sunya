import { data, operation } from 'skandha';

export class RoadmapExpansion {
  static className = () => 'RoadmapExpansion';

  @data expandCompletedMilestones: boolean = true;
  @data expandFutureMilestones: boolean = true;

  @operation toggleExpandCompletedMilestones(args: { value?: boolean }) {
    this.expandCompletedMilestones =
      args.value !== undefined ? args.value : !this.expandCompletedMilestones;
  }

  @operation toggleExpandFutureMilestones(args: { value?: boolean }) {
    this.expandFutureMilestones =
      args.value !== undefined ? args.value : !this.expandFutureMilestones;
  }
}
