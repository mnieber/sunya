import { AtlasBriefT } from '/src/api/types';
import React from 'react';
import { useObservableQuery } from '/src/api/hooks';
import { useGetAtlas } from '/src/api/queries/useGetAtlas';
import { AtlasState } from '/src/atlases/AtlasState';
import { useBuilder } from '/src/utils/hooks/useBuilder';

export type PropsT = {
  getAtlasBrief: () => AtlasBriefT;
};

export const useAtlasState = (props: PropsT) => {
  // Queries
  const getAtlas = useObservableQuery(
    useGetAtlas(
      { atlasId: props.getAtlasBrief()?.id ?? '' },
      { enabled: !!props.getAtlasBrief() }
    ),
    {
      fetchAsLoad: true,
      debugLabel: 'getAtlas',
    }
  );

  const atlasState = useBuilder(() => {
    const state = new AtlasState({
      //
      getAtlas: () => {
        return getAtlas.data?.atlas;
      },
    });

    return state;
  }) as AtlasState;

  React.useEffect(() => () => atlasState.destroy(), [atlasState]);

  return {
    atlasState,
    getAtlas,
  };
};
