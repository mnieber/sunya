import * as R from 'ramda';
import { data } from 'skandha';
import { ScenarioT } from '/src/api/types/ScenarioT';

export class ScenariosData {
  static className = () => 'ScenariosData';

  @data scenarios: ScenarioT[] = [];

  @data get scenarioById() {
    return R.indexBy(R.prop('id'), this.scenarios);
  }
}
