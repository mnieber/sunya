import * as R from 'ramda';
import { data } from 'skandha';
import { ProjectEntryT } from '/src/api/types/ProjectEntryT';

export class ProjectEntriesData {
  static className = () => 'ProjectEntriesData';

  @data projectEntries: ProjectEntryT[] = [];

  @data get projectEntryById() {
    return R.indexBy(R.prop('id'), this.projectEntries);
  }
}
