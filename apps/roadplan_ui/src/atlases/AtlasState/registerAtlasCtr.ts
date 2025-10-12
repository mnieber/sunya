import { mapDataToProps } from 'skandha';
import { registerCtr } from 'skandha-mobx';
import { AtlasState } from '/src/atlases/AtlasState';
import { getFilteredAtlas } from '/src/atlases/utils/getFilteredAtlas';

const mapData = (state: AtlasState) => {
  const ctr = state.atlasCtr;

  mapDataToProps(ctr, {
    data: {
      atlas: () => state.props.getAtlas(),
      filteredAtlas: () =>
        getFilteredAtlas(ctr.data.atlas, {
          showCompletedMilestones: ctr.filtering.showCompletedMilestones,
          showFutureMilestones: ctr.filtering.showFutureMilestones,
        }),
    },
  });
};

export const registerAtlasCtr = (state: AtlasState) => {
  registerCtr({
    ctr: state.atlasCtr,
    options: { name: 'AtlasState.Atlas' },
    initCtr: () => {
      mapData(state);
    },
  });
};
