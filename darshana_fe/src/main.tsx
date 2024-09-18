// Import styles. This needs to be done before importing any components.
import '/src/frames/styles/index.css';
import '/src/frames/styles/index.scss';

import setupLocatorUI from '@locator/runtime';
import { toJS } from 'mobx';
import { applyFormatters } from 'mobx-log';
import { setOptions as setResourceStatesOptions } from 'mobx-resource-states';
import { IStaticMethods } from 'preline/preline';
import React from 'react';
import ReactDOM from 'react-dom/client';
import { setOptions as setSkandhaOptions } from 'skandha';
import { App } from '/src/app/components';
import { flags } from '/src/app/flags';
import { log } from '/src/utils/logging';

if (process.env.NODE_ENV === 'development') {
  setupLocatorUI();
}

declare global {
  interface Window {
    HSStaticMethods: IStaticMethods;
  }
}

const strict = false;

if (import.meta.env.DEV) {
  applyFormatters();
}

setSkandhaOptions({
  logging: flags.logSkandha,
  formatObject: toJS,
});

setResourceStatesOptions({
  logging: flags.logResourceStates,
  log: log,
});

const isProduction = process.env.NODE_ENV === 'production';

async function enableMocking(): Promise<void> {
  if (isProduction || !flags.useMsw) {
    return;
  }

  const { worker } = await import('./mocks/browser');

  // `worker.start()` returns a Promise that resolves
  // once the Service Worker is up and ready to intercept requests.
  await worker.start();
}

const PrelineInitializer: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  React.useEffect(() => {
    // @ts-ignore
    import('preline/preline').then(({ HSStaticMethods }) => {
      HSStaticMethods.autoInit();
    });
  }, []);

  return <>{children}</>;
};

enableMocking().then(() => {
  const root = ReactDOM.createRoot(
    document.getElementById('root') as HTMLElement
  );

  const body = (
    <PrelineInitializer>
      <App />
    </PrelineInitializer>
  );

  root.render(strict ? <React.StrictMode>{body}</React.StrictMode> : body);
});
