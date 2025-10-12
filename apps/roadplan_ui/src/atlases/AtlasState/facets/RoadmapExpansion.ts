import { withCbs, type CallbackMap } from 'aspiration';
import { data, operation } from 'skandha';

export class RoadmapExpansion {
  static className = () => 'RoadmapExpansion';

  callbackMap = {} as CallbackMap<{
    toggleExpandCompletedMilestones: {};
    toggleExpandFutureMilestones: {};
  }>;

  @data expandCompletedMilestones: boolean = true;
  @data expandFutureMilestones: boolean = true;

  @operation toggleExpandCompletedMilestones(args: { value?: boolean }) {
    return withCbs(
      this.callbackMap,
      'toggleExpandCompletedMilestones',
      args,
      () => {
        this.expandCompletedMilestones =
          args.value !== undefined
            ? args.value
            : !this.expandCompletedMilestones;
      }
    );
  }

  @operation toggleExpandFutureMilestones(args: { value?: boolean }) {
    return withCbs(
      this.callbackMap,
      'toggleExpandFutureMilestones',
      args,
      () => {
        this.expandFutureMilestones =
          args.value !== undefined ? args.value : !this.expandFutureMilestones;
      }
    );
  }
}
