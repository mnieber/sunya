import { mapDataToProps } from 'skandha';
import { registerCtr } from 'skandha-mobx';
import { ProjectState } from './ProjectState';
import { ScenarioT } from '/src/api/types/ScenarioT';

const mapData = (state: ProjectState) => {
  const ctr = state.scenariosCtr;
  const getScenarioById = (x: string | undefined) =>
    x ? ctr.data.scenarioById[x] : undefined;

  mapDataToProps(ctr, {
    data: {
      scenarios: () => state.projectCtr.data.project?.scenarios ?? [],
    },
    highlight: {
      highlightableIds: () =>
        ctr.data.scenarios.map((scenario: ScenarioT) => scenario.id),
      item: () => getScenarioById(ctr.highlight.itemId),
    },
  });
};

const setCallbacks = (state: ProjectState) => {
  // Add any callbacks here if needed
};

export const registerScenariosCtr = (state: ProjectState) => {
  registerCtr({
    ctr: state.scenariosCtr,
    options: { name: 'ProjectState.Scenarios' },
    initCtr: () => {
      mapData(state);
      setCallbacks(state);
    },
  });
};
