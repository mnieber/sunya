import { Meta, StoryFn } from '@storybook/react';
import { passthroughHandlers } from '/src/mocks/browser/defaultPassthrough';
import { handleGetProject } from '/src/mocks/queries/handleGetProject';
import { handleGetProjectLeads } from '/src/mocks/queries/handleGetProjectLeads';
import { MockStepTreeStateProvider } from '/src/mocks/steps/components/MockStepTreeStateProvider';
import { ProjectsPage } from '/src/projects/components/ProjectsPage';

export default {
  title: 'Components/ProjectsPage',
  component: ProjectsPage,
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

const Template: StoryFn = () => <ProjectsPage />;

export const Default = Template.bind({});
Default.decorators = [
  (Story) => (
    <MockStepTreeStateProvider>
      <Story />
    </MockStepTreeStateProvider>
  ),
];
