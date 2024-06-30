import * as Skandha from 'skandha';
import { Highlight, Selection, Store } from 'skandha-facets';
import { ScenarioT } from '/src/api/types/ScenarioT';

// Local imports
import { registerScenariosCtr } from './registerScenariosCtr';

export type PropsT = {
  getScenarios: () => ScenarioT[];
};

export class ScenariosState {
  props: PropsT;

  scenariosCtr = {
    highlight: new Highlight<ScenarioT>(),
    selection: new Selection<ScenarioT>(),
    store: new Store<ScenarioT>(),
  };

  getSummary() {
    return {
      scenarios: Skandha.getCtrState(this.scenariosCtr),
    };
  }

  destroy() {
    Skandha.cleanUpCtr(this);
  }

  constructor(props: PropsT) {
    this.props = props;
    registerScenariosCtr(this);
  }
}
