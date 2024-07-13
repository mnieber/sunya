import { EntityT } from '/src/api/types/EntityT';

export type BlogT = EntityT & {
  name: string;
  slug: string;
};

export type BlogByIdT = { [id: string]: BlogT };
