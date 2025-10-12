import * as Skandha from 'skandha';
import { Highlight, Selection } from 'skandha-facets';
import { AtlasBriefT } from '/src/api/types';
import { AtlasBriefsData } from '/src/atlases/AtlasBriefsState/AtlasBriefsData';
import { registerAtlasBriefsCtr } from '/src/atlases/AtlasBriefsState/registerAtlasBriefsCtr';

export type PropsT = {
  getAtlasBriefs: () => AtlasBriefT[];
};

export class AtlasBriefsState {
  props: PropsT;

  atlasBriefsCtr = {
    data: new AtlasBriefsData(),
    highlight: new Highlight<AtlasBriefT>(),
    selection: new Selection<AtlasBriefT>(),
  };

  destroy() {
    Skandha.cleanUpCtr(this);
  }

  constructor(props: PropsT) {
    this.props = props;
    registerAtlasBriefsCtr(this);
  }
}
