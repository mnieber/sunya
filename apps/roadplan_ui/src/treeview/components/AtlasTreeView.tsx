import { MilestoneT, RoadmapT } from '/src/api/types';
import { observer } from 'mobx-react-lite';
import { isLoading } from 'mobx-resource-states';
import * as R from 'ramda';
import KeyboardEventHandler from 'react-keyboard-event-handler';
import { withContextProps } from 'react-props-from-context';
import { createSelectionKeyHandlers } from 'skandha-facets';
import { NodeT } from '/src/treeview/types';
import { atlasCtx } from '/src/atlases/hooks/useAtlasContext';
import { nodesCtx } from '/src/treeview/hooks/useNodesContext';
import { RoadmapNodeView } from '/src/atlases/components/RoadmapNodeView';
import { MilestoneNodeView } from '/src/atlases/components/MilestoneNodeView';
import { ResultNodeView } from '/src/atlases/components/ResultNodeView';
import { L } from '/src/frames/layout';
import { createKeyDownHandler } from '/src/utils';
import { cn } from '/src/utils/classnames';
import { type ResultT } from '/src/api/types';
import { isNodeVisible } from '/src/treeview/utils/isNodeVisible';

import './AtlasTreeView.scss';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  atlas: atlasCtx.filteredAtlas,
  nodes: nodesCtx.nodes,
  nodesExpansion: nodesCtx.nodesExpansion,
  nodesInZoomMode: nodesCtx.nodesInZoomMode,
  nodesExpansionInZoomMode: nodesCtx.nodesExpansionInZoomMode,
  nodesZoom: nodesCtx.nodesZoom,
  nodesState: nodesCtx.nodesState,
  resultsSelection: atlasCtx.resultsSelection,
  resultsHighlight: atlasCtx.resultsHighlight,
};

export const AtlasTreeView = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    if (isLoading(props.nodes)) {
      return (
        <div className={cn('AtlasTreeView', props.className)}>Loading...</div>
      );
    }

    const keyHandlers = createSelectionKeyHandlers(props.resultsSelection);

    // Use zoom mode nodes and expansion when zoom is enabled
    const activeNodes = props.nodesZoom.isEnabled
      ? props.nodesInZoomMode
      : props.nodes;
    const activeExpansion = props.nodesZoom.isEnabled
      ? props.nodesExpansionInZoomMode
      : props.nodesExpansion;

    const visibleNodes = activeNodes.filter((node) =>
      isNodeVisible(node, activeExpansion)
    );

    const nodeDivs = visibleNodes.map((node: NodeT) => {
      if (node.resourceType === 'roadmap') {
        return (
          <RoadmapNodeView
            key={node.id}
            roadmap={node.resource as RoadmapT}
            nodeId={node.id}
            expansion={activeExpansion}
          />
        );
      }

      if (node.resourceType === 'milestone') {
        return (
          <MilestoneNodeView
            key={node.id}
            milestone={node.resource as MilestoneT}
            nodeId={node.id}
            expansion={activeExpansion}
          />
        );
      }

      if (node.resourceType === 'result') {
        const result = node.resource as ResultT;
        const roadmap = node.parentNode!.parentNode!.resource as RoadmapT;

        return (
          <ResultNodeView
            key={node.id}
            result={result}
            selectItem={props.resultsSelection.selectItem.bind(
              props.resultsSelection
            )}
            highlightItem={props.resultsHighlight.set.bind(
              props.resultsHighlight
            )}
            isSelected={props.resultsSelection.itemIds.includes(node.id)}
            isZoomedResult={
              props.nodesZoom.isEnabled &&
              props.resultsSelection.itemIds.includes(result.id)
            }
            hideCheckbox={props.nodesZoom.isEnabled}
            roadmapOwner={roadmap.owner}
            className={{
              'ResultNodeView--selected':
                props.resultsSelection.itemIds.includes(node.id),
              'ResultNodeView--highlighted':
                props.resultsHighlight.itemId === node.id,
            }}
          />
        );
      }

      return null;
    });

    return (
      <KeyboardEventHandler
        handleKeys={R.keys(keyHandlers)}
        onKeyEvent={createKeyDownHandler(keyHandlers)}
      >
        <div
          className={cn('AtlasTreeView', [L.col.banner()], props.className)}
          tabIndex={1}
        >
          {nodeDivs}
        </div>
      </KeyboardEventHandler>
    );
  }, ContextProps)
);
