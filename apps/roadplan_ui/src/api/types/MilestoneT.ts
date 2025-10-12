import { initRS } from 'mobx-resource-states';
import { EntityT } from '/src/api/types/EntityT';
import { ResultT } from '/src/api/types/ResultT';
import { ObjT } from '/src/utils/types';

export type MilestoneT = EntityT & {
  title: string;
  markdownContent: string;
  roadmapId: string;
  results: ResultT[];
  nr: number;
  isFuture: boolean;
  isCompleted: boolean;
};

export type MilestoneByIdT = { [id: string]: MilestoneT };

export const createMilestone = (
  values: ObjT & { title: string; id: string }
): MilestoneT => {
  return initRS({
    id: values.id,
    title: values.title,
    roadmapId: values.roadmapId,
    markdownContent: values.markdownContent ?? '',
    results: values.results ?? [],
    nr: values.nr ?? -1,
    isFuture: values.isFuture ?? false,
    isCompleted: values.isCompleted ?? false,
  } as MilestoneT);
};
