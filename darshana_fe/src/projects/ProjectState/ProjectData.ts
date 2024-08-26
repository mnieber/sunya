import { data } from 'skandha';
import { ProjectT } from '/src/api/types/ProjectT';

export class ProjectData {
  static className = () => 'ProjectData';

  @data project?: ProjectT = undefined;
}
