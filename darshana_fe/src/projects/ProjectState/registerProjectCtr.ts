import { Cbs } from 'aspiration';
import { Edit } from 'skandha-facets';

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

const setCallbacks = (state: ProjectState) => {
  const ctr = state.projectCtr;

  ctr.edit.callbackMap = {
    save: {
      saveItem(this: Cbs<Edit['save']>) {
        return state.props.saveProject(this.args.values);
      },
    },
    cancel: {},
  };
};

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
