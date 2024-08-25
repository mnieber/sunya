import { initRS } from 'mobx-resource-states';
import { StepT } from './StepT';
import { EntityT } from '/src/api/types/EntityT';
import { createUUID } from '/src/utils/ids';
import { ObjT } from '/src/utils/types';

export type ScenarioT = EntityT & {
  name: string;
  root_step: StepT;
};

export type ScenarioByIdT = { [id: string]: ScenarioT };

export const createScenario = (values: ObjT): ScenarioT => {
  return initRS({
    id: createUUID(),
    name: values.name ?? 'New scenario',
    root_step: values.root_step ?? null,
  } as ScenarioT);
};
