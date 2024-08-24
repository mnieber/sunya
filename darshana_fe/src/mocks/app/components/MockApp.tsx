import { MockDashboardFrame } from '/src/mocks/frames/components/MockDashboardFrame';
import { MockMainView } from '/src/mocks/frames/components/MockMainView';
import { MockStepTreeView } from '/src/mocks/scenarios/components/MockStepTreeView';

export const MockApp = () => {
  return (
    <MockDashboardFrame>
      <MockMainView className="">
        <MockStepTreeView />
      </MockMainView>
    </MockDashboardFrame>
  );
};
