import * as Skandha from 'skandha';
import { Highlight, Store } from 'skandha-facets';
import { EntityT } from '/src/api/types/EntityT';

// Local imports
import { registerEntitiesCtr } from './registerEntitiesCtr';

export type PropsT = {
  getEntities: () => EntityT[];
};

export class EntitiesState {
  props: PropsT;

  entitiesCtr = {
    highlight: new Highlight<EntityT>(),
    store: new Store<EntityT>(),
  };

  getSummary() {
    return {
      entities: Skandha.getCtrState(this.entitiesCtr),
    };
  }

  destroy() {
    Skandha.cleanUpCtr(this);
  }

  constructor(props: PropsT) {
    this.props = props;
    registerEntitiesCtr(this);
  }
}
