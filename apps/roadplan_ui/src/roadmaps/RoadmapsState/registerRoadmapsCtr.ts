import { Cbs } from 'aspiration';
import * as R from 'ramda';
import { mapDataToProps } from 'skandha';
import {
  Edit,
  Selection,
  handleSelectItem,
  topOfTheList,
} from 'skandha-facets';
import { registerCtr } from 'skandha-mobx';
import { RoadmapsState } from '/src/roadmaps/RoadmapsState';
import { ObjT } from '/src/utils/types';

const mapData = (state: RoadmapsState) => {
  const ctr = state.roadmapsCtr;
  const getRoadmapById = (x: string) => ctr.data.roadmapById[x];

  mapDataToProps(ctr, {
    data: {
      roadmaps: () => state.props.getRoadmaps(),
    },
    selection: {
      selectableIds: () => R.map(R.prop('id'), ctr.data.roadmaps),
    },
    highlight: {
      item: () =>
        ctr.highlight.itemId ? getRoadmapById(ctr.highlight.itemId) : undefined,
    },
  });
};

const setCallbacks = (state: RoadmapsState) => {
  const ctr = state.roadmapsCtr;

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

export const registerRoadmapsCtr = (state: RoadmapsState) => {
  registerCtr({
    ctr: state.roadmapsCtr,
    options: { name: 'RoadmapsState.Roadmaps' },
    initCtr: () => {
      mapData(state);
      setCallbacks(state);
    },
  });
};
