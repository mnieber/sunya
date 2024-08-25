import { mapDataToProps } from 'skandha';
import { registerCtr } from 'skandha-mobx';
import { StepTreeState } from '/src/steps/StepTreeState';

const mapData = (state: StepTreeState) => {
  const ctr = state.stepTreeCtr;

  mapDataToProps(ctr, {
    data: {
      rootStep: () => state.props.getRootStep(),
    },
  });
};

const setCallbacks = (state: StepTreeState) => {};

export const registerStepTreeCtr = (state: StepTreeState) => {
  registerCtr({
    ctr: state.stepTreeCtr,
    options: { name: 'StepTreeState.StepTree' },
    initCtr: () => {
      mapData(state);
      setCallbacks(state);
    },
  });
};
