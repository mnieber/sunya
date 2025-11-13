import { z } from 'zod';
import { AtlasBriefSchema } from '/src/api/types/AtlasBriefSchema';
import { http, HttpResponse } from 'msw';
import { getAtlasBriefsUrl } from '/src/api/queries/useGetAtlasBriefs';
import { hostUrl } from '/src/api/restClient';
import { joinUrls } from '/src/utils/urls';
import { convertDataToSnakeCase } from '/src/api/utils/convertDataToSnakeCase';

export const handleGetAtlasBriefs = http.get(
  joinUrls(hostUrl, getAtlasBriefsUrl),
  () => {
    return HttpResponse.json(
      convertDataToSnakeCase(z.array(AtlasBriefSchema), [
        {
          id: '11111111-f82a-4b6a-9390-288e165dd5ed',
          isSyncedWithJira: false,
          createdAt: '2024-01-01T00:00:00.000Z',
        },
        {
          id: '22222222-f82a-4b6a-9390-288e165dd5ed',
          isSyncedWithJira: false,
          createdAt: '2024-02-01T00:00:00.000Z',
        },
      ])
    );
  }
);
