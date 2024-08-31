import * as Skandha from 'skandha';
import { Deletion, Edit, Highlight } from 'skandha-facets';
import { ProjectLeadT } from '/src/api/types/ProjectLeadT';
import { ProjectLeadsData } from '/src/projects/ProjectLeadsState/ProjectLeadsData';
import { registerProjectLeadsCtr } from '/src/projects/ProjectLeadsState/registerProjectLeadsCtr';
import { bindActionsCtr } from '/src/utils/bindActionsCtr';
import { ObjT } from '/src/utils/types';

export type PropsT = {
  getProjectLeads: () => ProjectLeadT[];
  deleteProjects: (ids: string[]) => Promise<any>;
  createProject: (values: ObjT) => Promise<any>;
  saveProject: (values: ObjT) => Promise<any>;
};

export class ProjectLeadsState {
  props: PropsT;

  projectLeadsCtr = {
    data: new ProjectLeadsData(),
    highlight: new Highlight<ProjectLeadT>(),
    deletion: new Deletion(),
    edit: new Edit(),
  };

  actionsCtr = {
    createProject: (values: ObjT) => {
      return this.props.createProject(values);
    },
  };

  destroy() {
    Skandha.cleanUpCtr(this);
  }

  constructor(props: PropsT) {
    this.props = props;
    bindActionsCtr(this.actionsCtr, this);
    registerProjectLeadsCtr(this);
  }
}
