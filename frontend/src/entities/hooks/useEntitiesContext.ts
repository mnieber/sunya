import React from 'react';
import { Highlight } from 'skandha-facets';
import { EntitiesState } from '/src/entities/EntitiesState';

export const EntitiesContext = React.createContext<any>(null);

export const useEntitiesContext = () => {
  const context = React.useContext(EntitiesContext);
  if (!context) {
    throw new Error(
      'useEntitiesContext must be used within a EntitiesContext.Provider'
    );
  }
  return context;
};

export const entitiesCtx = {
  entitiesState: [useEntitiesContext, 'entitiesState'] as any as EntitiesState,
  entity: [useEntitiesContext, 'entity'] as any as EntityT,
  entities: [useEntitiesContext, 'entities'] as any as EntityT[],
  entitiesHighlight: [
    useEntitiesContext,
    'entitiesHighlight',
  ] as any as Highlight,
};
