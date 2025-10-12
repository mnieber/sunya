import * as R from 'ramda';
import { data } from 'skandha';
import { RoadmapT } from '/src/api/types';

export class RoadmapsData {
  static className = () => 'RoadmapsData';

  @data roadmaps: RoadmapT[] = [];

  @data get roadmapById() {
    return R.indexBy(R.prop('id'), this.roadmaps);
  }
}
