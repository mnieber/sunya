import { EntityT } from '/src/api/types/EntityT';

export type RoadmapT = EntityT & {
  name: string;
};

export type RoadmapByIdT = { [id: string]: RoadmapT };
