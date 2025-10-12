import { Cbs } from 'aspiration';
import * as R from 'ramda';
import { mapDataToProps } from 'skandha';
import { Selection, handleSelectItem, Highlight } from 'skandha-facets';
import { registerCtr } from 'skandha-mobx';
import { AtlasState } from '/src/atlases/AtlasState';
import { buildResultsFromAtlas } from '/src/atlases/utils/buildResultsFromAtlas';
import { findMilestoneAndRoadmapByResultId } from '/src/atlases/utils/findMilestoneAndRoadmapByResultId';

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

const setCallbacks = (state: AtlasState) => {
  const ctr = state.resultsCtr;

  ctr.selection.callbackMap = {
    selectItem: {
      selectItem(this: Cbs<Selection['selectItem']>) {
        handleSelectItem(ctr.selection, this.args);
      },
    },
  };

  ctr.highlight.callbackMap = {
    set: {
      exit(this: Cbs<Highlight['set']>) {
        helpers.highlightRoadmapWhenResultIsHighlighted(state);
      },
    },
  };
};

const helpers = {
  highlightRoadmapWhenResultIsHighlighted: (state: AtlasState) => {
    if (R.isNil(state.resultsCtr.highlight.itemId)) return;

    const { roadmap } = findMilestoneAndRoadmapByResultId(
      state.atlasCtr.data.atlas!,
      state.resultsCtr.highlight.itemId
    );
    if (roadmap) {
      state.roadmapsCtr.highlight.set({ itemId: roadmap.id });
    }
  },
};

export const registerResultsCtr = (state: AtlasState) => {
  registerCtr({
    ctr: state.resultsCtr,
    options: { name: 'AtlasState.Results' },
    initCtr: () => {
      mapData(state);
      setCallbacks(state);
    },
  });
};
