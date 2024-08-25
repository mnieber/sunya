import * as Skandha from 'skandha';
import { Highlight } from 'skandha-facets';
import { registerScenariosCtr } from './registerScenariosCtr';
import { ScenarioT } from '/src/api/types/ScenarioT';
import { ScenariosData } from '/src/scenarios/ScenariosState/ScenariosData';

export type PropsT = {
  getScenarios: () => ScenarioT[];
};

export class ScenariosState {
  props: PropsT;

  scenariosCtr = {
    data: new ScenariosData(),
    highlight: new Highlight<ScenarioT>(),
  };

  destroy() {
    Skandha.cleanUpCtr(this);
  }

  constructor(props: PropsT) {
    this.props = props;
    registerScenariosCtr(this);
  }
}
