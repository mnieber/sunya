import { makeAutoObservable } from 'mobx';
import { observer } from 'mobx-react-lite';
import { updateSources } from 'mobx-resource-states';
import React from 'react';
import { useEntitiesState } from '/src/entities/hooks/useEntitiesState';
import { useBuilder } from '/src/utils/hooks/useBuilder';

export type PropsT = React.PropsWithChildren<{}>;

const ContextProps = {};

export const EntitiesStateProvider = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const { entitiesState: state } = useEntitiesState({
      /* MOONLEAP TODO */
    });

    const cache = useBuilder(() =>
      makeAutoObservable({
        get entities() {
          return updateSources(
            {
              resource: state.entitiesCtr.store.items,
              resourceName: 'entities',
            },
            ['loading', () => 'MOONLEAP TODO'],
            ['updating', () => 'MOONLEAP TODO']
          );
        },
        get entity() {
          return updateSources(
            { resource: state.entitiesCtr.highlight.item },
            ['loading', () => 'MOONLEAP TODO'],
            ['updating', () => 'MOONLEAP TODO']
          );
        },
      })
    );

    const getEntitiesContext = () => {
      return createGetProps(
        R.mergeAll([
          {
            entitiesState: () => state,
          },
          {
            entities: () => cache.entities,
            entity: () => cache.entity,
            entitiesHighlight: () => state.entitiesCtr.highlight,
          },
        ])
      );
    };

    return (
      <EntitiesContext.Provider value={getEntitiesContext()}>
        {props.children}
      </EntitiesContext.Provider>
    );
  }, ContextProps)
);
