import * as Skandha from 'skandha';
import { Highlight } from 'skandha-facets';
import { ProjectLeadT } from '/src/api/types/ProjectLeadT';
import { ProjectLeadsData } from '/src/projects/ProjectLeadsState/ProjectLeadsData';
import { registerProjectLeadsCtr } from '/src/projects/ProjectLeadsState/registerProjectLeadsCtr';

export type PropsT = {
  getProjectLeads: () => ProjectLeadT[];
};

export class ProjectLeadsState {
  props: PropsT;

  projectLeadsCtr = {
    data: new ProjectLeadsData(),
    highlight: new Highlight<ProjectLeadT>(),
  };

  destroy() {
    Skandha.cleanUpCtr(this);
  }

  constructor(props: PropsT) {
    this.props = props;
    registerProjectLeadsCtr(this);
  }
}
