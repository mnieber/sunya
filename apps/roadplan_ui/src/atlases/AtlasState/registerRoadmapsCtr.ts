import { mapDataToProps } from 'skandha';
import { registerCtr } from 'skandha-mobx';
import { AtlasState } from '/src/atlases/AtlasState';

const mapData = (state: AtlasState) => {
  const ctr = state.roadmapsCtr;
  const getRoadmapById = (x: string) => ctr.data.roadmapById[x];

  mapDataToProps(ctr, {
    data: {
      roadmaps: () => state.props.getAtlas()?.roadmaps || [],
    },
    highlight: {
      item: () =>
        ctr.highlight.itemId ? getRoadmapById(ctr.highlight.itemId) : undefined,
    },
  });
};

const setCallbacks = (state: AtlasState) => {};

export const registerRoadmapsCtr = (state: AtlasState) => {
  registerCtr({
    ctr: state.roadmapsCtr,
    options: { name: 'AtlasState.Roadmaps' },
    initCtr: () => {
      mapData(state);
      setCallbacks(state);
    },
  });
};
