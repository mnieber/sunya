import * as Skandha from 'skandha';
import { Highlight, Selection } from 'skandha-facets';
import { RoadmapT } from '/src/api/types';
import { RoadmapsData } from '/src/roadmaps/RoadmapsState/RoadmapsData';
import { registerRoadmapsCtr } from '/src/roadmaps/RoadmapsState/registerRoadmapsCtr';

export type PropsT = {
  getRoadmaps: () => RoadmapT[];
};

export class RoadmapsState {
  props: PropsT;

  roadmapsCtr = {
    data: new RoadmapsData(),
    highlight: new Highlight<RoadmapT>(),
    selection: new Selection<RoadmapT>(),
  };

  destroy() {
    Skandha.cleanUpCtr(this);
  }

  constructor(props: PropsT) {
    this.props = props;
    registerRoadmapsCtr(this);
  }
}
