import { observer } from 'mobx-react-lite';
import React from 'react';
import { withContextProps } from 'react-props-from-context';
import { DashboardState } from '/src/frames/DashboardState';
import { DashboardStateContext } from '/src/frames/hooks/useDashboardStateContext';
import { createGetProps } from '/src/utils/createGetProps';
import { useBuilder } from '/src/utils/hooks';

export type PropsT = React.PropsWithChildren<{}>;

const ContextProps = {};

export const DashboardStateProvider = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const dashboardState = useBuilder(() => new DashboardState());

    const getDashboardStateContext = () => {
      return createGetProps({
        dashboardState: () => dashboardState,
        buttonsPortalElm: () => dashboardState.buttonsPortalElm,
        setButtonsPortalElm: () => dashboardState.setButtonsPortalElm,
      });
    };

    return (
      <DashboardStateContext.Provider value={getDashboardStateContext()}>
        {props.children}
      </DashboardStateContext.Provider>
    );
  }, ContextProps)
);
