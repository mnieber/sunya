import * as R from 'ramda';
import React from 'react';
import { DashboardState } from '/src/frames/DashboardState';

export const DashboardStateContext = React.createContext<any>(null);

export const useDashboardStateContext = () => {
  const context = React.useContext(DashboardStateContext);
  if (!context) {
    throw new Error(
      'useDashboardStateContext must be used within a DashboardStateContext.Provider'
    );
  }
  return context;
};

export const dashboardCtx = R.mergeAll([
  {
    dashboardState: [
      useDashboardStateContext,
      'dashboardState',
    ] as any as DashboardState,
    setButtonsPortalElm: [
      useDashboardStateContext,
      'setButtonsPortalElm',
    ] as any as (elm: HTMLElement | null) => void,
    buttonsPortalElm: [
      useDashboardStateContext,
      'buttonsPortalElm',
    ] as any as HTMLElement | null,
  },
]);
