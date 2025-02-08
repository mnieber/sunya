import { observer } from 'mobx-react-lite';
import * as R from 'ramda';
import React from 'react';
import { withContextProps } from 'react-props-from-context';
import { useParams } from 'wouter';
import { ProjectLeadT } from '/src/api/types/ProjectLeadT';
import { projectLeadsCtx } from '/src/projects/hooks/useProjectLeadsContext';
import { useRefUrl } from '/src/routes/hooks/useRefUrl';
import { UrlEffectView } from '/src/utils/components';
import { ObjT } from '/src/utils/types';

type PropsT = {};

const ContextProps = {
  projectLeads: projectLeadsCtx.projectLeads,
  projectLead: projectLeadsCtx.projectLead,
  projectLeadsHighlight: projectLeadsCtx.projectLeadsHighlight,
};

export const SelectProjectLeadEffect = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const params = useParams() as ObjT;
    const { updateRefUrl, hasUrlChanged } = useRefUrl();

    const { projectLeadsHighlight, projectLead, projectLeads } = props;
    const projectLeadFromUrl = R.find(
      (x: ProjectLeadT) => x.id === params.projectId
    )(projectLeads);
    const isProjectLeadInSyncWithUrl =
      projectLead?.id === projectLeadFromUrl?.id;

    const selectProjectLead = (projectLead?: ProjectLeadT) => {
      projectLeadsHighlight.set({ itemId: projectLead?.id });
    };

    React.useEffect(() => {
      // If there is a new url
      if (hasUrlChanged) {
        if (projectLeadFromUrl) {
          updateRefUrl();
          if (!isProjectLeadInSyncWithUrl) {
            selectProjectLead(projectLeadFromUrl);
          }
        } else {
          selectProjectLead(undefined);
        }
      }
    });

    return (
      <UrlEffectView
        resourceName="projectLead"
        isInSync={isProjectLeadInSyncWithUrl}
        className="absolute"
      />
    );
  }, ContextProps)
);
