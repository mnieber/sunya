import { observer } from 'mobx-react-lite';
import * as R from 'ramda';
import React from 'react';
import { withContextProps } from 'react-props-from-context';
import { useParams } from 'wouter';
import { ProjectEntryT } from '/src/api/types/ProjectEntryT';
import { projectEntriesCtx } from '/src/projects/hooks/useProjectEntriesContext';
import { useRefUrl } from '/src/routes/hooks/useRefUrl';
import { UrlEffectView } from '/src/utils/components';
import { ObjT } from '/src/utils/types';

type PropsT = {};

const ContextProps = {
  projectEntries: projectEntriesCtx.projectEntries,
  projectEntry: projectEntriesCtx.projectEntry,
  projectEntriesHighlight: projectEntriesCtx.projectEntriesHighlight,
};

export const SelectProjectEntryEffect = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const params = useParams() as ObjT;
    const { updateRefUrl, hasUrlChanged } = useRefUrl();

    const { projectEntriesHighlight, projectEntry, projectEntries } = props;
    const projectEntryFromUrl = R.find(
      (x: ProjectEntryT) => x.id === params.projectId
    )(projectEntries);
    const isProjectEntryInSyncWithUrl =
      projectEntry?.id === projectEntryFromUrl?.id;

    const selectProjectEntry = (projectEntry?: ProjectEntryT) => {
      projectEntriesHighlight.set({ itemId: projectEntry?.id });
    };

    React.useEffect(() => {
      // If there is a new url
      if (hasUrlChanged) {
        if (projectEntryFromUrl) {
          updateRefUrl();
          if (!isProjectEntryInSyncWithUrl) {
            selectProjectEntry(projectEntryFromUrl);
          }
        } else {
          selectProjectEntry(undefined);
        }
      }
    });

    return (
      <UrlEffectView
        resourceName="projectEntry"
        isInSync={isProjectEntryInSyncWithUrl}
        className="absolute"
      />
    );
  }, ContextProps)
);
