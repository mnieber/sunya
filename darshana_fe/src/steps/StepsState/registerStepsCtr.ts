import { addCleanUpFunctionToCtr, cleanUpCtr, mapDataToProps } from 'skandha';
import { registerCtr } from 'skandha-mobx';
import { StepsState } from '/src/steps/StepsState';
import { getIds } from '/src/utils/ids';

const mapData = (state: StepsState) => {
  const ctr = state.stepsCtr;

  const getStepById = (x: string | undefined) =>
    x ? ctr.store.itemById[x] : undefined;

  mapDataToProps(ctr, {
    store: {
      items: () => state.props.getSteps(),
    },
    highlight: {
      highlightableIds: () => getIds(ctr.store.items ?? []),
      item: () => getStepById(ctr.highlight.itemId),
    },
  });
};

const setCallbacks = (state: StepsState) => {
  const ctr = state.stepsCtr;
  addCleanUpFunctionToCtr(state, () => cleanUpCtr(ctr));
};

export const registerStepsCtr = (state: StepsState) => {
  registerCtr({
    ctr: state.stepsCtr,
    options: { name: 'StepsState.Steps' },
    initCtr: () => {
      mapData(state);
      setCallbacks(state);
    },
  });
};
