import { Meta, StoryObj } from '@storybook/react';
import { BlogListView } from '/src/blogs/components';
import { handleMe } from '/src/mocks/users/handleMe';
import { storyWithMsw } from '/src/mocks/utils/storyWithMsw';

const meta: Meta<typeof BlogListView> = {
  component: BlogListView,
  decorators: [(Story) => storyWithMsw(Story, [handleMe])],
};

export default meta;
type Story = StoryObj<typeof BlogListView>;

export const Default: Story = {
  render: () => <BlogListView />,
};
