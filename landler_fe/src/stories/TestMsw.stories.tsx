import { Meta, StoryObj } from '@storybook/react';
import { BlogListView } from '/src/blogs/components';
import { handleMe } from '/src/mocks/users/handleMe';

const meta: Meta<typeof BlogListView> = {
  component: BlogListView,
  parameters: {
    msw: {
      handlers: [handleMe],
    },
  },
};

export default meta;

type Story = StoryObj<typeof BlogListView>;

export const Default: Story = {
  render: () => <BlogListView />,
};
