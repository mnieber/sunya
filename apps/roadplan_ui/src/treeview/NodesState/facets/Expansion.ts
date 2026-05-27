import { data, input, operation, stub } from 'skandha';
import * as R from 'ramda';

export class Expansion {
  static className = () => 'Expansion';

  @input expandableIds: Array<string> = stub;
  @data isExpandedByItemId: { [key: string]: boolean } = {};

  @operation toggle(args: { itemId: string; value?: boolean }) {
    this.isExpandedByItemId[args.itemId] = R.isNil(args.value)
      ? !this.isExpandedByItemId[args.itemId]
      : args.value;
  }

  isExpanded(itemId: string): boolean {
    return !!this.isExpandedByItemId[itemId];
  }
}
