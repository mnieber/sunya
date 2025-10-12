import { setupWorker } from 'msw/browser';
import { handleMe } from '/src/mocks/users/handleMe';
import { passthroughHandlers } from './defaultPassthrough';
import { handleGetAtlas } from '/src/mocks/queries/handleGetAtlas';
import { handleGetAtlasBriefs } from '/src/mocks/queries/handleGetAtlasBriefs';

export const handlers = [
  // Add more handlers here (but don't commit them to main)
  handleMe,
  handleGetAtlas,
  handleGetAtlasBriefs,
  ...passthroughHandlers,
];

export const worker = setupWorker(...handlers);
