import { observer } from 'mobx-react-lite';
import * as R from 'ramda';
import React from 'react';
import { withContextProps } from 'react-props-from-context';
import { AccountMenu } from '/src/frames/components/AccountMenu';
import { dashboardCtx } from '/src/frames/hooks/useDashboardStateContext';
import { L } from '/src/frames/layout';
import { Breadcrumb } from '/src/projects/components/Breadcrumb';
import { cn } from '/src/utils/classnames';

// Import styles
import './DashboardFrame.scss';

type PropsT = React.PropsWithChildren<{
  className?: any;
}>;

const DefaultProps = {
  setButtonsPortalElm: dashboardCtx.setButtonsPortalElm,
};

export const DashboardFrame = observer(
  withContextProps((props: PropsT & typeof DefaultProps) => {
    return (
      <div className={cn('DashboardFrame', L.row.canvas(), props.className)}>
        <div
          className={cn(
            'DashboardFrame__LeftSideBar',
            R.values({
              //
              layout: ['max-w-64 p-4', L.col.banner()],
              color: ['bg-gray-700'],
            })
          )}
        >
          <div
            className={cn(
              'DashboardFrame__ButtonsCard',
              L.col.banner(),
              'p-4',
              'bg-blue-400',
              props.className
            )}
            ref={(elm) => props.setButtonsPortalElm(elm)}
          ></div>
        </div>
        <div
          className={cn(
            'DashboardFrame__Canvas',
            R.values({
              //
              layout: ['p-4', L.col.canvas()],
              color: ['bg-gray-800'],
            })
          )}
        >
          <div
            className={cn(
              'DashboardFrame__TopBar',
              R.values({
                //
                layout: ['p-4', L.col.flagPoleRev()],
              })
            )}
          >
            <AccountMenu />
          </div>
          <Breadcrumb />
          {props.children}
        </div>
      </div>
    );
  }, DefaultProps)
);

export const DashboardFrameS = {};
