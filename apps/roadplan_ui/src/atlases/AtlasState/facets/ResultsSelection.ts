import { Selection, handleSelectItem } from 'skandha-facets';
import { ResultT } from '/src/api/types';
import { AtlasState } from '/src/atlases/AtlasState';

export class ResultsSelection extends Selection<ResultT> {
  constructor(private state: AtlasState) {
    super();
  }

  protected performSelection(args: {
    itemId: string;
    isCtrl: boolean;
    isShift: boolean;
  }): void {
    handleSelectItem(this, args);
  }
}
