import { EntityT } from '/src/api/types/EntityT';

export type ResultT = EntityT & {
  name: string;
};

export type ResultByIdT = { [id: string]: ResultT };
