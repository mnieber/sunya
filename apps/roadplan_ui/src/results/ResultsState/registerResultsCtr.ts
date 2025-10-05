import { Cbs } from 'aspiration';
import * as R from 'ramda';
import { mapDataToProps } from 'skandha';
import { Selection, handleSelectItem } from 'skandha-facets';
import { registerCtr } from 'skandha-mobx';
import { ResultT } from '/src/api/types';
import { ResultsState } from '/src/results/ResultsState';

const mapData = (state: ResultsState) => {
  const ctr = state.resultsCtr;
  const getResultById = (x: string | undefined) =>
    x ? ctr.data.resultById[x] : undefined;

  mapDataToProps(ctr, {
    data: {
      results: () => state.props.getResults(),
    },
    selection: {
      selectableIds: () => R.map(R.prop('id'), ctr.data.results),
      items: () =>
        ctr.selection.itemIds
          .map(getResultById)
          .filter((x?: ResultT) => !!x) as ResultT[],
    },
    highlight: {
      highlightableIds: () => R.map(R.prop('id'), ctr.data.results),
      item: () => getResultById(ctr.highlight.itemId),
    },
  });
};

const setCallbacks = (state: ResultsState) => {
  const ctr = state.resultsCtr;

  ctr.selection.callbackMap = {
    selectItem: {
      selectItem(this: Cbs<Selection['selectItem']>) {
        handleSelectItem(ctr.selection, this.args);
        if (!this.args.isCtrl && !this.args.isShift) {
          ctr.highlight.set({ itemId: this.args.itemId });
        }
      },
    },
  };
};

export const registerResultsCtr = (state: ResultsState) => {
  registerCtr({
    ctr: state.resultsCtr,
    options: { name: 'ResultsState.Results' },
    initCtr: () => {
      mapData(state);
      setCallbacks(state);
    },
  });
};
