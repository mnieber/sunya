import { MockDashboardFrame } from '/src/mocks/frames/components/MockDashboardFrame';
import { MockMainView } from '/src/mocks/frames/components/MockMainView';
import { MockUserSettingsSwitch } from '/src/mocks/userSettings/components/MockUserSettingsSwitch';

export const MockApp = () => {
  return (
    <MockDashboardFrame>
      <MockMainView className="">
        <MockUserSettingsSwitch />
      </MockMainView>
    </MockDashboardFrame>
  );
};
