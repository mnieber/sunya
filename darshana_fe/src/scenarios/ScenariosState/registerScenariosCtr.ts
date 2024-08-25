import { mapDataToProps } from 'skandha';
import { registerCtr } from 'skandha-mobx';
import { ScenariosState } from './ScenariosState';
import { ScenarioT } from '/src/api/types/ScenarioT';

const mapData = (state: ScenariosState) => {
  const ctr = state.scenariosCtr;
  const getScenarioById = (x: string | undefined) =>
    x ? ctr.data.scenarioById[x] : undefined;

  mapDataToProps(ctr, {
    data: {
      scenarios: () => state.props.getScenarios(),
    },
    highlight: {
      highlightableIds: () =>
        ctr.data.scenarios.map((scenario: ScenarioT) => scenario.id),
      item: () => getScenarioById(ctr.highlight.itemId),
    },
  });
};

const setCallbacks = (state: ScenariosState) => {
  // Add any callbacks here if needed
};

export const registerScenariosCtr = (state: ScenariosState) => {
  registerCtr({
    ctr: state.scenariosCtr,
    options: { name: 'ScenariosState.Scenarios' },
    initCtr: () => {
      mapData(state);
      setCallbacks(state);
    },
  });
};
