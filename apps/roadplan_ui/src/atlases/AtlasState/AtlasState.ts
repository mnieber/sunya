import * as Skandha from 'skandha';
import { Highlight, Selection } from 'skandha-facets';
import { RoadmapT, ResultT } from '/src/api/types';
import { RoadmapsData } from '/src/atlases/AtlasState/RoadmapsData';
import { ResultsData } from '/src/atlases/AtlasState/facets/ResultsData';
import { AtlasData } from '/src/atlases/AtlasState/facets/AtlasData';
import { AtlasFiltering } from '/src/atlases/AtlasState/facets/AtlasFiltering';
import { RoadmapExpansion } from '/src/atlases/AtlasState/facets/RoadmapExpansion';
import { registerRoadmapsCtr } from '/src/atlases/AtlasState/registerRoadmapsCtr';
import { registerAtlasCtr } from '/src/atlases/AtlasState/registerAtlasCtr';
import { registerResultsCtr } from '/src/atlases/AtlasState/registerResultsCtr';
import { AtlasT } from '/src/api/types/AtlasT';

export type PropsT = {
  getAtlas: () => AtlasT;
};

export class AtlasState {
  props: PropsT;

  atlasCtr = {
    data: new AtlasData(),
    filtering: new AtlasFiltering(),
  };

  roadmapsCtr = {
    data: new RoadmapsData(),
    highlight: new Highlight<RoadmapT>(),
    expansion: new RoadmapExpansion(),
  };

  resultsCtr = {
    data: new ResultsData(),
    highlight: new Highlight<ResultT>(),
    selection: new Selection<ResultT>(),
  };

  destroy() {
    Skandha.cleanUpCtr(this);
  }

  constructor(props: PropsT) {
    this.props = props;
    registerAtlasCtr(this);
    registerRoadmapsCtr(this);
    registerResultsCtr(this);
  }
}
