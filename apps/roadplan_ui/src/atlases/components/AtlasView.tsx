import { observer } from 'mobx-react-lite';
import { isLoading } from 'mobx-resource-states';
import { InPortal } from 'react-reverse-portal';
import { withContextProps } from 'react-props-from-context';
import { Panel, PanelGroup, PanelResizeHandle } from 'react-resizable-panels';
import { atlasCtx } from '/src/atlases/hooks/useAtlasContext';
import { appCtx } from '/src/app/hooks/useAppContext';
import { AtlasHeader } from '/src/atlases/components/AtlasHeader';
import { AtlasTreeView } from '/src/treeview/components/AtlasTreeView';
import { RoadmapView } from '/src/roadmaps/components/RoadmapView';
import { ZoomButton } from '/src/ribbon/components/ZoomButton';
import { ShowFutureMilestonesButton } from '/src/ribbon/components/ShowFutureMilestonesButton';
import { ShowCompletedMilestonesButton } from '/src/ribbon/components/ShowCompletedMilestonesButton';
import { cn } from '/src/utils/classnames';

import './AtlasView.scss';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  atlas: atlasCtx.filteredAtlas,
  appState: appCtx.appState,
};

export const AtlasView = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    if (isLoading(props.atlas)) {
      return <div className={cn('AtlasView', props.className)}>Loading...</div>;
    }
    if (!props.atlas) {
      return null;
    }

    return (
      <div className={cn('AtlasView', props.className)}>
        <InPortal node={props.appState.portals.atlasHeader}>
          <AtlasHeader />
        </InPortal>
        <InPortal node={props.appState.portals.zoomButton}>
          <ZoomButton />
        </InPortal>
        <InPortal node={props.appState.portals.showFutureMilestonesButton}>
          <ShowFutureMilestonesButton />
        </InPortal>
        <InPortal node={props.appState.portals.showCompletedMilestonesButton}>
          <ShowCompletedMilestonesButton />
        </InPortal>
        <div className="AtlasView__content">
          {props.appState.showRoadmapContents ? (
            <PanelGroup direction="horizontal">
              <Panel defaultSize={35} minSize={25}>
                <div className="AtlasView__panel-scroll h-full overflow-y-auto">
                  <AtlasTreeView />
                </div>
              </Panel>
              <PanelResizeHandle className="AtlasView__resize-handle" />
              <Panel defaultSize={65} minSize={40}>
                <div className="AtlasView__panel-scroll h-full flex flex-col overflow-hidden">
                  <RoadmapView />
                </div>
              </Panel>
            </PanelGroup>
          ) : (
            <div className="AtlasView__panel-scroll h-full overflow-y-auto">
              <AtlasTreeView />
            </div>
          )}
        </div>
      </div>
    );
  }, ContextProps)
);
