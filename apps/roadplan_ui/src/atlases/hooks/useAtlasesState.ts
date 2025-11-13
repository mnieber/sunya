import React from 'react';
import { useObservableQuery } from '/src/api/hooks';
import { useCreateAtlas } from '/src/api/mutations';
import { useGetAtlasBriefs } from '/src/api/queries/useGetAtlasBriefs';
import { AtlasesState } from '/src/atlases/AtlasesState';
import { useBuilder } from '/src/utils/hooks/useBuilder';
import { useGraftResourceStatesFromMemo } from '/src/utils/hooks/useGraftResourceStatesFromMemo';

export type PropsT = {};

export const useAtlasesState = (props: PropsT) => {
  const graftResourceStatesFromMemo = useGraftResourceStatesFromMemo({});

  // Queries
  const getAtlasBriefs = useObservableQuery(useGetAtlasBriefs(), {
    fetchAsLoad: true,
    debugLabel: 'getAtlasBriefs',
  });

  // Mutations
  const createAtlas = useCreateAtlas();

  const atlasesState = useBuilder(() => {
    const state = new AtlasesState({
      //
      getAtlasBriefs: () => {
        return graftResourceStatesFromMemo({
          resources: getAtlasBriefs.data?.atlasBriefs ?? [],
        });
      },
      createAtlas: () => {
        return createAtlas.mutateAsync({});
      },
    });

    return state;
  }) as AtlasesState;

  React.useEffect(() => () => atlasesState.destroy(), [atlasesState]);

  return {
    atlasesState,
    getAtlasBriefs,
    createAtlas,
  };
};
