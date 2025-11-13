import { initRS } from 'mobx-resource-states';
import { EntityT } from '/src/api/types/EntityT';
import { ObjT } from '/src/utils/types';

export type ResultT = EntityT & {
  name: string;
  owner?: string;
  isDone: boolean;
  resultType: 'ms' | 'bug' | 'generic' | 'meeting' | 'release';
  milestoneId: string;
  parentResultNames: string[];
  jiraTicketUrls: string[];
};

export type ResultByIdT = { [id: string]: ResultT };

export const createResult = (
  values: ObjT & { id: string; name: string }
): ResultT => {
  return initRS({
    id: values.id,
    name: values.name,
    owner: values.owner,
    isDone: values.isDone,
    resultType: values.resultType,
    milestoneId: values.milestoneId,
    parentResultNames: values.parentResultNames ?? [],
    jiraTicketUrls: values.jiraTicketUrls ?? [],
  } as ResultT);
};
