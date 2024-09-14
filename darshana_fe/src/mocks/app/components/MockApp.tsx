import { MockDashboardFrame } from '/src/mocks/frames/components/MockDashboardFrame';
import { MockStepTreeView } from '/src/mocks/scenarios/components/MockStepTreeView';

export const MockApp = () => {
  return <MockDashboardFrame>{<MockStepTreeView />}</MockDashboardFrame>;
};
