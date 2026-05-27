import * as R from 'ramda';
import { mapDataToProps } from 'skandha';
import { registerCtr } from 'skandha-mobx';
import { AtlasesState } from '/src/atlases/AtlasesState';

const mapData = (state: AtlasesState) => {
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

export const registerAtlasBriefsCtr = (state: AtlasesState) => {
  registerCtr({
    ctr: state.atlasBriefsCtr,
    options: { name: 'AtlasesState.AtlasBriefs' },
    initCtr: () => {
      mapData(state);
    },
  });
};
