import { initRS } from 'mobx-resource-states';
import { EntityT } from '/src/api/types/EntityT';
import { MilestoneT } from '/src/api/types/MilestoneT';
import { ObjT } from '/src/utils/types';

export type RoadmapT = EntityT & {
  name: string;
  owner: string;
  milestones: MilestoneT[];
};

export type RoadmapByIdT = { [id: string]: RoadmapT };

export const createRoadmap = (
  values: ObjT & { name: string; id: string }
): RoadmapT => {
  return initRS({
    id: values.id,
    name: values.name,
    owner: values.owner,
    milestones: values.milestones ?? [],
  } as RoadmapT);
};
