import { withCbs, type CallbackMap } from 'aspiration';
import { data, operation } from 'skandha';

export class Zoom {
  static className = () => 'Zoom';

  callbackMap = {} as CallbackMap<{
    toggle: {};
  }>;

  @data isEnabled: boolean = false;

  @operation toggle(args: { mode?: boolean }) {
    return withCbs(this.callbackMap, 'toggle', args, (cbs) => {
      if (args.mode !== undefined) {
        this.isEnabled = args.mode;
      } else {
        this.isEnabled = !this.isEnabled;
      }
    });
  }
}
