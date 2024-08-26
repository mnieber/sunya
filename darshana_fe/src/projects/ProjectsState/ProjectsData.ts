// File: src/projects/ProjectsState/ProjectsData.ts

import * as R from 'ramda';
import { data } from 'skandha';
import { ProjectT } from '/src/api/types/ProjectT';

export class ProjectsData {
  static className = () => 'ProjectsData';

  @data projects: ProjectT[] = [];

  @data get projectById() {
    return R.indexBy(R.prop('id'), this.projects);
  }
}
