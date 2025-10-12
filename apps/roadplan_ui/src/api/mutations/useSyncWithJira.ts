import { useObservableMutation } from '/src/api/lib/ObservableMutation';
import { invalidateGetAtlasBriefs } from '/src/api/queries/useGetAtlasBriefs';
import { post } from '/src/api/restClient';
import { AtlasT } from '/src/api/types/AtlasT';
import { waitOnDev } from '/src/utils/wait';

export type SyncWithJiraArgsT = {
  atlas: AtlasT;
};

export const syncWithJira = (args: SyncWithJiraArgsT) => {
  const url = `/roadmaps/${args.atlas.id}/sync-with-jira/`;
  return post(url, {})
    .then((response) => {
      return waitOnDev(1000, response);
    })
    .catch((error) => {
      // Handle specific error cases if needed
      throw error;
    });
};

export const useSyncWithJira = () => {
  return useObservableMutation({
    mutationFn: syncWithJira,
    onSuccess: (response: any, args: SyncWithJiraArgsT) => {
      invalidateGetAtlasBriefs({});
    },
  });
};
