import React from 'react';
import { useObservableQuery } from '/src/api/hooks';
import { useGetAtlasBriefs } from '/src/api/queries/useGetAtlasBriefs';
import { AtlasBriefsState } from '/src/atlases/AtlasBriefsState';
import { useBuilder } from '/src/utils/hooks/useBuilder';
import { useGraftResourceStatesFromMemo } from '/src/utils/hooks/useGraftResourceStatesFromMemo';

export type PropsT = {};

export const useAtlasBriefsState = (props: PropsT) => {
  const graftResourceStatesFromMemo = useGraftResourceStatesFromMemo({});

  // Queries
  const getAtlasBriefs = useObservableQuery(useGetAtlasBriefs(), {
    fetchAsLoad: true,
    debugLabel: 'getAtlasBriefs',
  });

  const atlasBriefsState = useBuilder(() => {
    const state = new AtlasBriefsState({
      //
      getAtlasBriefs: () => {
        return graftResourceStatesFromMemo({
          resources: getAtlasBriefs.data?.atlasBriefs ?? [],
        });
      },
    });

    return state;
  }) as AtlasBriefsState;

  React.useEffect(() => () => atlasBriefsState.destroy(), [atlasBriefsState]);

  return {
    atlasBriefsState,
    getAtlasBriefs,
  };
};
