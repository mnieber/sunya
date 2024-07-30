import { initRS } from 'mobx-resource-states';
import { EntityT } from '/src/api/types/EntityT';
import { createUUID } from '/src/utils/ids';
import { ObjT } from '/src/utils/types';

export type BlogT = EntityT & {
  name: string;
  slug: string;
};

export type BlogByIdT = { [id: string]: BlogT };

export const createBlog = (values: ObjT): BlogT => {
  return initRS({
    id: createUUID(),
    isTransient: true,
    name: values.name ?? 'New blog',
    slug: '-',
  } as BlogT);
};
