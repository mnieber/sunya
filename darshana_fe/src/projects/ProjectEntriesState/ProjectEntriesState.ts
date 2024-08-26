import * as Skandha from 'skandha';
import { Highlight } from 'skandha-facets';
import { ProjectEntryT } from '/src/api/types/ProjectEntryT';
import { ProjectEntriesData } from '/src/projects/ProjectEntriesState/ProjectEntriesData';
import { registerProjectEntriesCtr } from '/src/projects/ProjectEntriesState/registerProjectEntriesCtr';

export type PropsT = {
  getProjectEntries: () => ProjectEntryT[];
};

export class ProjectEntriesState {
  props: PropsT;

  projectEntriesCtr = {
    data: new ProjectEntriesData(),
    highlight: new Highlight<ProjectEntryT>(),
  };

  destroy() {
    Skandha.cleanUpCtr(this);
  }

  constructor(props: PropsT) {
    this.props = props;
    registerProjectEntriesCtr(this);
  }
}
