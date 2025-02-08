// Import styles. This needs to be done before importing any components.
import '/src/frames/styles/index.css';
import '/src/frames/styles/index.scss';

import type { Preview } from '@storybook/react';
import { initialize, mswDecorator } from 'msw-storybook-addon';

// Initialize MSW
initialize();

// Provide the MSW addon decorator globally
export const decorators = [mswDecorator];

const preview: Preview = {
  parameters: {
    controls: {
      matchers: {
        color: /(background|color)$/i,
        date: /Date$/i,
      },
    },
  },
};

export default preview;
