import { observer } from 'mobx-react-lite';
import { InPortal } from 'react-reverse-portal';
import { withContextProps } from 'react-props-from-context';
import { appCtx } from '/src/app/hooks/useAppContext';
import { CreateAtlasButton } from '/src/atlases/components/CreateAtlasButton';
import { SyncAtlasWithJiraButton } from '/src/jira/components';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  appState: appCtx.appState,
};

export const AtlasMenu = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    return (
      <>
        <InPortal node={props.appState.portals.createAtlasButton}>
          <CreateAtlasButton />
        </InPortal>
        <InPortal node={props.appState.portals.syncAtlasWithJiraButton}>
          <SyncAtlasWithJiraButton />
        </InPortal>
      </>
    );
  }, ContextProps)
);
