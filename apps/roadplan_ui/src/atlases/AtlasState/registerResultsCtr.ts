import * as R from 'ramda';
import { mapDataToProps } from 'skandha';
import { registerCtr } from 'skandha-mobx';
import { AtlasState } from '/src/atlases/AtlasState';
import { buildResultsFromAtlas } from '/src/atlases/utils/buildResultsFromAtlas';

const mapData = (state: AtlasState) => {
  const ctr = state.resultsCtr;
  const getResultById = (x: string) => ctr.data.resultById[x];

  mapDataToProps(ctr, {
    data: {
      results: () => buildResultsFromAtlas(state.props.getAtlas()),
    },
    selection: {
      selectableIds: () => R.map(R.prop('id'), ctr.data.results),
    },
    highlight: {
      item: () =>
        ctr.highlight.itemId ? getResultById(ctr.highlight.itemId) : undefined,
    },
  });
};

export const registerResultsCtr = (state: AtlasState) => {
  registerCtr({
    ctr: state.resultsCtr,
    options: { name: 'AtlasState.Results' },
    initCtr: () => {
      mapData(state);
    },
  });
};
