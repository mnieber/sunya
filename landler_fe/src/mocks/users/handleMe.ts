import { http, HttpResponse } from 'msw';
import { getRestApiBaseUrlWithVersion } from 'src/api/rest/client';

export type HandleMeResponse = {
  data: string;
};

export const handleMe = http.get(`${getRestApiBaseUrlWithVersion()}/user/me/`, () => {
  return HttpResponse.json({
    data: 'fancy data string',
  } as HandleMeResponse);
});
