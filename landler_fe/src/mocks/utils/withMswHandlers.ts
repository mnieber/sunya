import { RequestHandler } from 'msw';
import { setupServer } from 'msw/node';

export const withMswHandlers = (handlers: RequestHandler[], testSuite: () => void) => {
  const server = setupServer(...handlers);

  return () => {
    beforeAll(() => server.listen());
    afterEach(() => server.resetHandlers());
    afterAll(() => server.close());
    testSuite();
  };
};
