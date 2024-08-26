import { initRS } from 'mobx-resource-states';
import { EntityT } from '/src/api/types/EntityT';
import { ScenarioT } from '/src/api/types/ScenarioT';
import { createUUID } from '/src/utils/ids';
import { ObjT } from '/src/utils/types';

export type ProjectT = EntityT & {
  name: string;
  scenarios: ScenarioT[];
};

export type ProjectByIdT = { [id: string]: ProjectT };

export const createProject = (values: ObjT): ProjectT => {
  return initRS({
    id: createUUID(),
    name: values.name ?? 'New project',
    scenarios: values.scenarios ?? [],
  } as ProjectT);
};
