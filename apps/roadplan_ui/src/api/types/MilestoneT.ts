import { EntityT } from '/src/api/types/EntityT';

export type MilestoneT = EntityT & {
  title: string;
};

export type MilestoneByIdT = { [id: string]: MilestoneT };
