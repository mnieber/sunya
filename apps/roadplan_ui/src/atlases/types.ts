import { ResultT } from '/src/api/types/ResultT';
import { MilestoneT } from '/src/api/types/MilestoneT';
import { RoadmapT } from '/src/api/types/RoadmapT';

export type AtlasLutT = {
  resultById: Record<string, ResultT>;
  milestoneById: Record<string, MilestoneT>;
  roadmapById: Record<string, RoadmapT>;
};
