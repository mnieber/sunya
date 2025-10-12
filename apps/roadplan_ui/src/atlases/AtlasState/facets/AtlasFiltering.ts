import { withCbs, type CallbackMap } from 'aspiration';
import { data, operation } from 'skandha';

export class AtlasFiltering {
  static className = () => 'AtlasFiltering';

  callbackMap = {} as CallbackMap<{
    toggleShowCompletedMilestones: {};
    toggleShowFutureMilestones: {};
  }>;

  @data showCompletedMilestones: boolean = true;
  @data showFutureMilestones: boolean = true;

  @operation toggleShowCompletedMilestones(args: { value?: boolean }) {
    return withCbs(
      this.callbackMap,
      'toggleShowCompletedMilestones',
      args,
      () => {
        this.showCompletedMilestones =
          args.value !== undefined ? args.value : !this.showCompletedMilestones;
      }
    );
  }

  @operation toggleShowFutureMilestones(args: { value?: boolean }) {
    return withCbs(this.callbackMap, 'toggleShowFutureMilestones', args, () => {
      this.showFutureMilestones =
        args.value !== undefined ? args.value : !this.showFutureMilestones;
    });
  }
}
