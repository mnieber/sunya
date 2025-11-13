import * as R from 'ramda';
import { data } from 'skandha';
import { AtlasBriefT } from '/src/api/types';

export class AtlasBriefsData {
  static className = () => 'AtlasBriefsData';

  @data atlasBriefs: AtlasBriefT[] = [];

  @data get atlasBriefById() {
    return R.indexBy(R.prop('id'), this.atlasBriefs);
  }
}
