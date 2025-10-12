import { ObjT } from '/src/utils/types';
import { MilestoneT, ResultT, RoadmapT } from '/src/api/types';

export type NodeT = {
  resource: RoadmapT | MilestoneT | ResultT;
  resourceType: 'roadmap' | 'milestone' | 'result';
  id: string;
  parentNode?: NodeT;
};

export const createNode = (values: ObjT): NodeT => {
  return {
    resource: values.resource,
    resourceType: values.resourceType,
    id: values.id ?? values.resource.id,
    parentNode: values.parentNode,
  } as NodeT;
};
