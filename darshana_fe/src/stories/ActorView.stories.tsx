import { Meta, StoryFn } from '@storybook/react';
import { ActorView } from '/src/actors/components/ActorView';
import { StepTreeContext } from '/src/steps/hooks/useStepTreeContext';

export default {
  title: 'Components/ActorView',
  component: ActorView,
  decorators: [
    (Story) => (
      <div style={{ padding: '3rem' }}>
        <Story />
      </div>
    ),
  ],
} as Meta;

const Template: StoryFn = (args) => <ActorView {...args} />;

export const Default = Template.bind({});
Default.decorators = [
  (Story) => (
    <StepTreeContext.Provider
      value={{
        reconstructedActor: {
          id: 'actor1',
          key: 'example:actor',
          fields: {
            name: 'John Doe',
            email: 'john@example.com',
            role: 'User',
          },
          changed_fields: ['email'],
        },
      }}
    >
      <Story />
    </StepTreeContext.Provider>
  ),
];

export const NoChangedFields = Template.bind({});
NoChangedFields.decorators = [
  (Story) => (
    <StepTreeContext.Provider
      value={{
        reconstructedActor: {
          id: 'actor2',
          key: 'another:actor',
          fields: {
            name: 'Jane Smith',
            age: 30,
            department: 'HR',
          },
          changed_fields: [],
        },
      }}
    >
      <Story />
    </StepTreeContext.Provider>
  ),
];

export const AllFieldsChanged = Template.bind({});
AllFieldsChanged.decorators = [
  (Story) => (
    <StepTreeContext.Provider
      value={{
        reconstructedActor: {
          id: 'actor3',
          key: 'fully-changed:actor',
          fields: {
            username: 'superuser',
            accessLevel: 'Admin',
            lastLogin: '2023-05-01',
          },
          changed_fields: ['username', 'accessLevel', 'lastLogin'],
        },
      }}
    >
      <Story />
    </StepTreeContext.Provider>
  ),
];

export const NoActor = Template.bind({});
NoActor.decorators = [
  (Story) => (
    <StepTreeContext.Provider
      value={{
        reconstructedActor: null,
      }}
    >
      <Story />
    </StepTreeContext.Provider>
  ),
];
