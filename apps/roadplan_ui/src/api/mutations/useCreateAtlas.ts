import { useObservableMutation } from '/src/api/lib/ObservableMutation';
import { invalidateGetAtlasBriefs } from '/src/api/queries/useGetAtlasBriefs';
import { post } from '/src/api/restClient';
import { AtlasBriefSchema } from '/src/api/types/AtlasBriefSchema';
import { parseResponse } from '/src/api/utils/parseResponse';
import { waitOnDev } from '/src/utils/wait';

export type CreateAtlasArgsT = {};

export const createAtlas = (args: CreateAtlasArgsT) => {
  const url = `/atlases/create/`;
  return post(url, { create_atlas_form: {} })
    .then((response) => {
      const res = parseResponse(AtlasBriefSchema, response.data);

      return waitOnDev(1000, res);
    })
    .catch((error) => {
      throw error;
    });
};

export const useCreateAtlas = () => {
  return useObservableMutation({
    mutationFn: createAtlas,
    onSuccess: (response: any, args: CreateAtlasArgsT) => {
      invalidateGetAtlasBriefs({});
    },
  });
};
