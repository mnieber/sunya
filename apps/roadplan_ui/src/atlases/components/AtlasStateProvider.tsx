import { withContextProps } from 'react-props-from-context';
import { makeAutoObservable } from 'mobx';
import { observer } from 'mobx-react-lite';
import { updateSources } from 'mobx-resource-states';
import React from 'react';
import { isQueryLoading } from '/src/api/lib/ObservableQuery';
import { AtlasContext } from '/src/atlases/hooks/useAtlasContext';
import { useAtlasState } from '/src/atlases/hooks/useAtlasState';
import { createGetProps } from '/src/utils/createGetProps';
import { useBuilder } from '/src/utils/hooks/useBuilder';
import { atlasesCtx } from '/src/atlases/hooks/useAtlasesContext';

export type PropsT = React.PropsWithChildren<{}>;

const ContextProps = {
  atlasBrief: atlasesCtx.atlasBrief,
};

export const AtlasStateProvider = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const { atlasState, getAtlas } = useAtlasState({
      getAtlasBrief: () => props.atlasBrief,
    });

    const cache = useBuilder(() =>
      makeAutoObservable({
        get atlas() {
          return updateSources(
            {
              resource: atlasState.atlasCtr.data.atlas,
              resourceName: 'atlas',
            },
            ['loading', () => isQueryLoading(getAtlas), 'atlas']
          );
        },
        get filteredAtlas() {
          return updateSources(
            {
              resource: atlasState.atlasCtr.data.filteredAtlas,
              resourceName: 'atlas',
            },
            ['loading', () => isQueryLoading(getAtlas), 'atlas']
          );
        },
        get roadmap() {
          return updateSources(
            {
              resource: atlasState.roadmapsCtr.highlight.item,
              resourceName: 'roadmap',
            },
            ['loading', () => isQueryLoading(getAtlas), 'roadmap']
          );
        },
        get roadmaps() {
          return updateSources(
            { resource: atlasState.roadmapsCtr.data.roadmaps },
            ['loading', () => isQueryLoading(getAtlas), 'roadmaps']
          );
        },
        get result() {
          return updateSources(
            {
              resource: atlasState.resultsCtr.highlight.item,
              resourceName: 'result',
            },
            ['loading', () => isQueryLoading(getAtlas), 'result']
          );
        },
        get results() {
          return updateSources(
            { resource: atlasState.resultsCtr.data.results },
            ['loading', () => isQueryLoading(getAtlas), 'results']
          );
        },
      })
    );

    const getAtlasContext = () => {
      return createGetProps({
        atlasState: () => atlasState,
        atlas: () => cache.atlas,
        filteredAtlas: () => cache.filteredAtlas,
        atlasFiltering: () => atlasState.atlasCtr.filtering,
        roadmaps: () => cache.roadmaps,
        roadmap: () => cache.roadmap,
        roadmapsHighlight: () => atlasState.roadmapsCtr.highlight,
        roadmapExpansion: () => atlasState.roadmapsCtr.expansion,
        results: () => cache.results,
        result: () => cache.result,
        resultsHighlight: () => atlasState.resultsCtr.highlight,
        resultsSelection: () => atlasState.resultsCtr.selection,
      });
    };

    return (
      <AtlasContext.Provider value={getAtlasContext()}>
        {props.children}
      </AtlasContext.Provider>
    );
  }, ContextProps)
);
