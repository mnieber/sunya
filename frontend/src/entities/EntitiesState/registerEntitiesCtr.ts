import { addCleanUpFunctionToCtr, cleanUpCtr, mapDataToProps } from 'skandha';
import { registerCtr } from 'skandha-mobx';
import { EntitiesState } from '/src/entities/EntitiesState';
import { getIds } from '/src/utils/ids';

const mapData = (state: EntitiesState) => {
  const ctr = state.entitiesCtr;

  const getEntityById = (x: string | undefined) =>
    x ? ctr.store.itemById[x] : undefined;

  mapDataToProps(ctr, {
    store: {
      items: () => state.props.getEntities(),
    },
    highlight: {
      highlightableIds: () => getIds(ctr.store.items ?? []),
      item: () => getEntityById(ctr.highlight.itemId),
    },
  });
};

const setCallbacks = (state: EntitiesState) => {
  const ctr = state.entitiesCtr;
  addCleanUpFunctionToCtr(state, () => cleanUpCtr(ctr));
};

export const registerEntitiesCtr = (state: EntitiesState) => {
  registerCtr({
    ctr: state.entitiesCtr,
    options: { name: 'EntitiesState.Entities' },
    initCtr: () => {
      mapData(state);
      setCallbacks(state);
    },
  });
};
