import { setupWorker } from 'msw/browser';
import { passthroughHandlers } from './defaultPassthrough';

export const handlers = [
  // Add more handlers here (but don't commit them to main)
  ...passthroughHandlers,
];

export const worker = setupWorker(...handlers);
