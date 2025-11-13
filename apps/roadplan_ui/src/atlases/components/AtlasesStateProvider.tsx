import { makeAutoObservable } from 'mobx';
import { observer } from 'mobx-react-lite';
import { updateSources } from 'mobx-resource-states';
import React from 'react';
import { isQueryLoading } from '/src/api/lib/ObservableQuery';
import { AtlasesContext } from '/src/atlases/hooks/useAtlasesContext';
import { useAtlasesState } from '/src/atlases/hooks/useAtlasesState';
import { createGetProps } from '/src/utils/createGetProps';
import { useBuilder } from '/src/utils/hooks/useBuilder';

export type PropsT = React.PropsWithChildren<{}>;

export const AtlasesStateProvider = observer((props: PropsT) => {
  const { atlasesState, getAtlasBriefs, createAtlas } = useAtlasesState({});

  const cache = useBuilder(() =>
    makeAutoObservable({
      get atlasBrief() {
        return updateSources(
          {
            resource: atlasesState.atlasBriefsCtr.highlight.item,
            resourceName: 'atlasBrief',
          },
          ['loading', () => isQueryLoading(getAtlasBriefs), 'atlasBrief']
        );
      },
      get atlasBriefs() {
        return updateSources(
          { resource: atlasesState.atlasBriefsCtr.data.atlasBriefs },
          ['loading', () => isQueryLoading(getAtlasBriefs), 'getAtlasBriefs']
        );
      },
    })
  );

  const getAtlasesContext = () => {
    return createGetProps({
      atlasesState: () => atlasesState,
      atlasBriefs: () => cache.atlasBriefs,
      atlasBrief: () => cache.atlasBrief,
      atlasBriefsHighlight: () => atlasesState.atlasBriefsCtr.highlight,
      atlasBriefsSelection: () => atlasesState.atlasBriefsCtr.selection,
      isCreatingAtlas: () => createAtlas.status === 'loading',
    });
  };

  return (
    <AtlasesContext.Provider value={getAtlasesContext()}>
      {props.children}
    </AtlasesContext.Provider>
  );
});
