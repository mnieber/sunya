import React from 'react';
import { EntitiesState } from '/src/entities/EntitiesState';
import { useBuilder } from '/src/utils/hooks/useBuilder';

export type PropsT = {};

export const useEntitiesState = (props: PropsT) => {
  const entitiesState = useBuilder<EntitiesState>(() => {
    return new EntitiesState({
      getEntities: () => {
        return graftResourceStatesFromMemo({
          resources: [] /* MOONLEAP TODO */,
        });
      },
    });
  }) as EntitiesState;

  React.useEffect(() => () => entitiesState.destroy(), [entitiesState]);

  return {
    entitiesState,
  };
};
