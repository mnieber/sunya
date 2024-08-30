import { MockDashboardFrame } from '/src/mocks/frames/components/MockDashboardFrame';
import { FooView } from '/src/mocks/scenarios/components/FooView';
import { MockStepTreeView } from '/src/mocks/scenarios/components/MockStepTreeView';

export const MockApp = () => {
  return (
    <MockDashboardFrame>
      {true && <FooView />}
      {<MockStepTreeView />}
    </MockDashboardFrame>
  );
};
