import { observer } from 'mobx-react-lite';
import { OutPortal } from 'react-reverse-portal';
import { withContextProps } from 'react-props-from-context';
import { appCtx } from '/src/app/hooks/useAppContext';
import { AccountMenu } from '/src/frames/components/AccountMenu';
import { L } from '/src/frames/layout';
import { cn } from '/src/utils/classnames';

// Import styles
import './Ribbon.scss';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  appState: appCtx.appState,
};

export const Ribbon = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    return (
      <div className={cn('Ribbon', L.row.bar(), props.className)}>
        <div className={cn('Ribbon__left', L.row.skewer())}>
          <OutPortal node={props.appState.portals.atlasHeader} />
          <OutPortal node={props.appState.portals.zoomButton} />
          <OutPortal node={props.appState.portals.showFutureMilestonesButton} />
          <OutPortal node={props.appState.portals.showCompletedMilestonesButton} />
        </div>
        <div className={cn('Ribbon__right', L.row.skewer())}>
          <AccountMenu />
        </div>
      </div>
    );
  }, ContextProps)
);
