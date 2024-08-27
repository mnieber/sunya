import { initRS } from 'mobx-resource-states';
import { createUUID } from '/src/utils/ids';
import { ObjT } from '/src/utils/types';

export type ActorT = {
  key: string;
  fields: { [key: string]: any };
  changed_fields: string[];
};

export type ActorByIdT = { [id: string]: ActorT };

export const createActor = (values: ObjT): ActorT => {
  return initRS({
    id: createUUID(),
    key: values.key ?? '',
    fields: values.fields ?? {},
    changed_fields: values.changed_fields ?? [],
  } as ActorT);
};
