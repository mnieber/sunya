import * as Skandha from 'skandha';
import { Highlight } from 'skandha-facets';
import { AtlasBriefT } from '/src/api/types';
import { AtlasBriefsData } from '/src/atlases/AtlasesState/AtlasBriefsData';
import { AtlasBriefsSelection } from '/src/atlases/AtlasesState/facets/AtlasBriefsSelection';
import { registerAtlasBriefsCtr } from '/src/atlases/AtlasesState/registerAtlasBriefsCtr';

export type PropsT = {
  getAtlasBriefs: () => AtlasBriefT[];
  createAtlas: () => Promise<any>;
};

export class AtlasesState {
  props: PropsT;

  atlasBriefsCtr = {
    data: new AtlasBriefsData(),
    highlight: new Highlight<AtlasBriefT>(),
    selection: new AtlasBriefsSelection(this),
  };

  createAtlas() {
    return this.props.createAtlas();
  }

  destroy() {
    Skandha.cleanUpCtr(this);
  }

  constructor(props: PropsT) {
    this.props = props;
    registerAtlasBriefsCtr(this);
  }
}
