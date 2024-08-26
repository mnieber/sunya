// File: src/projects/ProjectsState/registerProjectsCtr.ts

import * as R from 'ramda';
import { mapDataToProps } from 'skandha';
import { registerCtr } from 'skandha-mobx';
import { ProjectsState } from '/src/projects/ProjectsState/ProjectsState';

const mapData = (state: ProjectsState) => {
  const ctr = state.projectsCtr;
  const getProjectById = (x: string) => ctr.data.projectById[x];

  mapDataToProps(ctr, {
    data: {
      projects: () => state.props.getProjects(),
    },
    highlight: {
      highlightableIds: () => R.map(R.prop('id'), ctr.data.projects),
      item: () =>
        ctr.highlight.itemId ? getProjectById(ctr.highlight.itemId) : undefined,
    },
  });
};

const setCallbacks = (state: ProjectsState) => {
  const ctr = state.projectsCtr;

  ctr.highlight.callbackMap = {
    set: {},
  };
};

export const registerProjectsCtr = (state: ProjectsState) => {
  registerCtr({
    ctr: state.projectsCtr,
    options: { name: 'ProjectsState.Projects' },
    initCtr: () => {
      mapData(state);
      setCallbacks(state);
    },
  });
};
