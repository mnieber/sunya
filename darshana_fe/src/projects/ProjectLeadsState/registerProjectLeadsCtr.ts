import { Cbs } from 'aspiration';
import * as R from 'ramda';
import { mapDataToProps } from 'skandha';
import { Deletion, Edit } from 'skandha-facets';
import { registerCtr } from 'skandha-mobx';
import { ProjectLeadsState } from '/src/projects/ProjectLeadsState/ProjectLeadsState';

const mapData = (state: ProjectLeadsState) => {
  const ctr = state.projectLeadsCtr;
  const getProjectLeadById = (x: string) => ctr.data.projectLeadById[x];

  mapDataToProps(ctr, {
    data: {
      projectLeads: () => state.props.getProjectLeads(),
    },
    highlight: {
      highlightableIds: () => R.map(R.prop('id'), ctr.data.projectLeads),
      item: () =>
        ctr.highlight.itemId
          ? getProjectLeadById(ctr.highlight.itemId)
          : undefined,
    },
  });
};

const setCallbacks = (state: ProjectLeadsState) => {
  const ctr = state.projectLeadsCtr;

  ctr.deletion.callbackMap = {
    delete: {
      deleteItems(this: Cbs<Deletion['delete']>) {
        return state.props.deleteProjects(this.args.itemIds);
      },
    },
  };

  ctr.edit.callbackMap = {
    save: {
      saveItem(this: Cbs<Edit['save']>) {
        return state.props.saveProject(this.args.values);
      },
    },
    cancel: {},
  };

  ctr.highlight.callbackMap = {
    set: {},
  };
};

export const registerProjectLeadsCtr = (state: ProjectLeadsState) => {
  registerCtr({
    ctr: state.projectLeadsCtr,
    options: { name: 'ProjectLeadsState.ProjectLeads' },
    initCtr: () => {
      mapData(state);
      setCallbacks(state);
    },
  });
};
