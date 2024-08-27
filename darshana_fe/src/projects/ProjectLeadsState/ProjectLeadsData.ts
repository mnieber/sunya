import * as R from 'ramda';
import { data } from 'skandha';
import { ProjectLeadT } from '/src/api/types/ProjectLeadT';

export class ProjectLeadsData {
  static className = () => 'ProjectLeadsData';

  @data projectLeads: ProjectLeadT[] = [];

  @data get projectLeadById() {
    return R.indexBy(R.prop('id'), this.projectLeads);
  }
}
