import { setupWorker } from 'msw/browser';
import { passthroughHandlers } from './defaultPassthrough';
import { handleGetBlogTags } from '/src/mocks/queries/handleGetBlogTags';

export const handlers = [
  // Add more handlers here (but don't commit them to main)
  handleGetBlogTags,
  ...passthroughHandlers,
];

export const worker = setupWorker(...handlers);
