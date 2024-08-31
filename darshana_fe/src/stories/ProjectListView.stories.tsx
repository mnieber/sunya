import { Meta, StoryFn } from '@storybook/react';
import { passthroughHandlers } from '/src/mocks/browser/defaultPassthrough';
import { handleGetProject } from '/src/mocks/queries/handleGetProject';
import { handleGetProjectLeads } from '/src/mocks/queries/handleGetProjectLeads';
import { MockStepTreeStateProvider } from '/src/mocks/steps/components/MockStepTreeStateProvider';
import { ProjectListView } from '/src/projects/components/ProjectListView';

export default {
  title: 'Components/ProjectListView',
  component: ProjectListView,
  parameters: {
    msw: {
      handlers: [
        handleGetProjectLeads,
        handleGetProject,
        ...passthroughHandlers,
      ],
    },
  },
  decorators: [
    (Story) => (
      <div style={{ padding: '3rem' }}>
        <Story />
      </div>
    ),
  ],
} as Meta;

const Template: StoryFn = () => <ProjectListView />;

export const Default = Template.bind({});
Default.decorators = [
  (Story) => (
    <MockStepTreeStateProvider>
      <Story />
    </MockStepTreeStateProvider>
  ),
];
