// File: src/projects/ProjectsState/ProjectsState.ts

import * as Skandha from 'skandha';
import { Highlight } from 'skandha-facets';
import { ProjectT } from '/src/api/types/ProjectT';
import { ProjectsData } from '/src/projects/ProjectsState/ProjectsData';
import { registerProjectsCtr } from '/src/projects/ProjectsState/registerProjectsCtr';

export type PropsT = {
  getProjects: () => ProjectT[];
};

export class ProjectsState {
  props: PropsT;

  projectsCtr = {
    data: new ProjectsData(),
    highlight: new Highlight<ProjectT>(),
  };

  destroy() {
    Skandha.cleanUpCtr(this);
  }

  constructor(props: PropsT) {
    this.props = props;
    registerProjectsCtr(this);
  }
}
