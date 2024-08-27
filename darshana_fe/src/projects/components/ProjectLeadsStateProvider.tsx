import { makeAutoObservable } from 'mobx';
import { observer } from 'mobx-react-lite';
import { updateSources } from 'mobx-resource-states';
import React from 'react';
import { isQueryLoading } from '/src/api/lib/ObservableQuery';
import { ProjectLeadsContext } from '/src/projects/hooks/useProjectLeadsContext';
import { useProjectLeadsState } from '/src/projects/hooks/useProjectLeadsState';
import { createGetProps } from '/src/utils/createGetProps';
import { useBuilder } from '/src/utils/hooks/useBuilder';

export type PropsT = React.PropsWithChildren<{}>;

export const ProjectLeadsStateProvider = observer((props: PropsT) => {
  const { projectLeadsState, getProjectLeads } = useProjectLeadsState({});

  const cache = useBuilder(() =>
    makeAutoObservable({
      get projectLead() {
        return updateSources(
          {
            resource: projectLeadsState.projectLeadsCtr.highlight.item,
            resourceName: 'projectLead',
          },
          ['loading', () => isQueryLoading(getProjectLeads), 'projectLead']
        );
      },
      get projectLeads() {
        return updateSources(
          {
            resource: projectLeadsState.projectLeadsCtr.data.projectLeads,
          },
          ['loading', () => isQueryLoading(getProjectLeads), 'getProjectLeads']
        );
      },
    })
  );

  const getProjectLeadsContext = () => {
    return createGetProps({
      projectLeadsState: () => projectLeadsState,
      projectLeads: () => cache.projectLeads,
      projectLead: () => cache.projectLead,
      projectLeadsHighlight: () => projectLeadsState.projectLeadsCtr.highlight,
    });
  };

  return (
    <ProjectLeadsContext.Provider value={getProjectLeadsContext()}>
      {props.children}
    </ProjectLeadsContext.Provider>
  );
});
