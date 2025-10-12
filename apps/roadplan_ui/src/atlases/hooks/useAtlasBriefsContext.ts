import * as R from 'ramda';
import React from 'react';
import { Highlight, Selection } from 'skandha-facets';
import { AtlasBriefT } from '/src/api/types';
import { AtlasBriefsState } from '/src/atlases/AtlasBriefsState';

export const AtlasBriefsContext = React.createContext<any>(null);

export const useAtlasBriefsContext = () => {
  const context = React.useContext(AtlasBriefsContext);
  if (!context) {
    throw new Error(
      'useAtlasBriefsContext must be used within a AtlasBriefsContext.Provider'
    );
  }
  return context;
};

export const atlasBriefsCtx = R.mergeAll([
  {
    atlasBriefsState: [
      useAtlasBriefsContext,
      'atlasBriefsState',
    ] as any as AtlasBriefsState,
    atlasBriefs: [useAtlasBriefsContext, 'atlasBriefs'] as any as AtlasBriefT[],
    atlasBrief: [useAtlasBriefsContext, 'atlasBrief'] as any as AtlasBriefT,
    atlasBriefsHighlight: [
      useAtlasBriefsContext,
      'atlasBriefsHighlight',
    ] as any as Highlight,
    atlasBriefsSelection: [
      useAtlasBriefsContext,
      'atlasBriefsSelection',
    ] as any as Selection,
  },
]);
