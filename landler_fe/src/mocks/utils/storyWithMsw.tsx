import { initialize, mswDecorator } from 'msw-storybook-addon';
import { ReactElement, useEffect, useState } from 'react';

// Initialize MSW
initialize();

// Create a decorator
export const storyWithMsw = (Story: () => ReactElement, handlers: any[]) => {
  const [isReady, setIsReady] = useState(false);

  useEffect(() => {
    mswDecorator.worker.use(...handlers);
    setIsReady(true);

    return () => {
      mswDecorator.worker.resetHandlers();
    };
  }, [handlers]);

  if (!isReady) {
    return null;
  }

  return <Story />;
};
