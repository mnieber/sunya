import { Cbs } from 'aspiration';
import * as R from 'ramda';
import { mapDataToProps } from 'skandha';
import { Selection, handleSelectItem } from 'skandha-facets';
import { registerCtr } from 'skandha-mobx';
import { AtlasBriefsState } from '/src/atlases/AtlasBriefsState';

const mapData = (state: AtlasBriefsState) => {
  const ctr = state.atlasBriefsCtr;
  const getAtlasBriefById = (x: string) => ctr.data.atlasBriefById[x];

  mapDataToProps(ctr, {
    data: {
      atlasBriefs: () => {
        return state.props.getAtlasBriefs();
      },
    },
    selection: {
      selectableIds: () => R.map(R.prop('id'), ctr.data.atlasBriefs),
    },
    highlight: {
      item: () =>
        ctr.highlight.itemId
          ? getAtlasBriefById(ctr.highlight.itemId)
          : undefined,
    },
  });
};

const setCallbacks = (state: AtlasBriefsState) => {
  const ctr = state.atlasBriefsCtr;

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

export const registerAtlasBriefsCtr = (state: AtlasBriefsState) => {
  registerCtr({
    ctr: state.atlasBriefsCtr,
    options: { name: 'AtlasBriefsState.AtlasBriefs' },
    initCtr: () => {
      mapData(state);
      setCallbacks(state);
    },
  });
};
