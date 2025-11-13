import * as R from 'ramda';
import React from 'react';
import { Highlight, Selection } from 'skandha-facets';
import { AtlasBriefT } from '/src/api/types';
import { AtlasesState } from '/src/atlases/AtlasesState';

export const AtlasesContext = React.createContext<any>(null);

export const useAtlasesContext = () => {
  const context = React.useContext(AtlasesContext);
  if (!context) {
    throw new Error(
      'useAtlasesContext must be used within a AtlasesContext.Provider'
    );
  }
  return context;
};

export const atlasesCtx = R.mergeAll([
  {
    atlasesState: [useAtlasesContext, 'atlasesState'] as any as AtlasesState,
    atlasBriefs: [useAtlasesContext, 'atlasBriefs'] as any as AtlasBriefT[],
    atlasBrief: [useAtlasesContext, 'atlasBrief'] as any as AtlasBriefT,
    atlasBriefsHighlight: [
      useAtlasesContext,
      'atlasBriefsHighlight',
    ] as any as Highlight,
    atlasBriefsSelection: [
      useAtlasesContext,
      'atlasBriefsSelection',
    ] as any as Selection,
    isCreatingAtlas: [useAtlasesContext, 'isCreatingAtlas'] as any as boolean,
  },
]);
