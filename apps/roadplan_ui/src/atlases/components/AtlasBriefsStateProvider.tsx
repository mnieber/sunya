import { makeAutoObservable } from 'mobx';
import { observer } from 'mobx-react-lite';
import { updateSources } from 'mobx-resource-states';
import React from 'react';
import { isQueryLoading } from '/src/api/lib/ObservableQuery';
import { AtlasBriefsContext } from '/src/atlases/hooks/useAtlasBriefsContext';
import { useAtlasBriefsState } from '/src/atlases/hooks/useAtlasBriefsState';
import { createGetProps } from '/src/utils/createGetProps';
import { useBuilder } from '/src/utils/hooks/useBuilder';

export type PropsT = React.PropsWithChildren<{}>;

export const AtlasBriefsStateProvider = observer((props: PropsT) => {
  const { atlasBriefsState, getAtlasBriefs } = useAtlasBriefsState({});

  const cache = useBuilder(() =>
    makeAutoObservable({
      get atlasBrief() {
        return updateSources(
          {
            resource: atlasBriefsState.atlasBriefsCtr.highlight.item,
            resourceName: 'atlasBrief',
          },
          ['loading', () => isQueryLoading(getAtlasBriefs), 'atlasBrief']
        );
      },
      get atlasBriefs() {
        return updateSources(
          { resource: atlasBriefsState.atlasBriefsCtr.data.atlasBriefs },
          ['loading', () => isQueryLoading(getAtlasBriefs), 'getAtlasBriefs']
        );
      },
    })
  );

  const getAtlasBriefsContext = () => {
    return createGetProps({
      atlasBriefsState: () => atlasBriefsState,
      atlasBriefs: () => cache.atlasBriefs,
      atlasBrief: () => cache.atlasBrief,
      atlasBriefsHighlight: () => atlasBriefsState.atlasBriefsCtr.highlight,
      atlasBriefsSelection: () => atlasBriefsState.atlasBriefsCtr.selection,
    });
  };

  return (
    <AtlasBriefsContext.Provider value={getAtlasBriefsContext()}>
      {props.children}
    </AtlasBriefsContext.Provider>
  );
});
