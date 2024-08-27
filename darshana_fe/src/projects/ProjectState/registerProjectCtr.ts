import { mapDataToProps } from 'skandha';
import { registerCtr } from 'skandha-mobx';
import { ProjectState } from '/src/projects/ProjectState';

const mapData = (state: ProjectState) => {
  const ctr = state.projectCtr;

  mapDataToProps(ctr, {
    data: {
      project: () => state.props.getProject(),
    },
  });
};

const setCallbacks = (state: ProjectState) => {};

export const registerProjectCtr = (state: ProjectState) => {
  registerCtr({
    ctr: state.projectCtr,
    options: { name: 'ProjectState.Project' },
    initCtr: () => {
      mapData(state);
      setCallbacks(state);
    },
  });
};
