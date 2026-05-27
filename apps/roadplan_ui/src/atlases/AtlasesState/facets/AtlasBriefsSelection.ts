import { Selection, handleSelectItem } from 'skandha-facets';
import { AtlasBriefT } from '/src/api/types';
import { AtlasesState } from '/src/atlases/AtlasesState';

export class AtlasBriefsSelection extends Selection<AtlasBriefT> {
  constructor(private state: AtlasesState) {
    super();
  }

  protected performSelection(args: {
    itemId: string;
    isCtrl: boolean;
    isShift: boolean;
  }): void {
    handleSelectItem(this, args);
    if (!args.isCtrl && !args.isShift) {
      this.state.atlasBriefsCtr.highlight.set({ itemId: args.itemId });
    }
  }
}
