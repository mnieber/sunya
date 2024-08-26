import * as R from 'ramda';
import { mapDataToProps } from 'skandha';
import { registerCtr } from 'skandha-mobx';
import { ProjectEntriesState } from '/src/projects/ProjectEntriesState/ProjectEntriesState';

const mapData = (state: ProjectEntriesState) => {
  const ctr = state.projectEntriesCtr;
  const getProjectEntryById = (x: string) => ctr.data.projectEntryById[x];

  mapDataToProps(ctr, {
    data: {
      projectEntries: () => state.props.getProjectEntries(),
    },
    highlight: {
      highlightableIds: () => R.map(R.prop('id'), ctr.data.projectEntries),
      item: () =>
        ctr.highlight.itemId
          ? getProjectEntryById(ctr.highlight.itemId)
          : undefined,
    },
  });
};

const setCallbacks = (state: ProjectEntriesState) => {
  const ctr = state.projectEntriesCtr;

  ctr.highlight.callbackMap = {
    set: {},
  };
};

export const registerProjectEntriesCtr = (state: ProjectEntriesState) => {
  registerCtr({
    ctr: state.projectEntriesCtr,
    options: { name: 'ProjectEntriesState.ProjectEntries' },
    initCtr: () => {
      mapData(state);
      setCallbacks(state);
    },
  });
};
