import { http, HttpResponse } from 'msw';
import { hostUrl } from '/src/api/restClient';
import { joinUrls } from '/src/utils/urls';
import { loadUserIdUrl } from '/src/auth/endpoints/queries/useLoadUserId';

export type HandleMeResponse = {
  data: string;
};

export const handleMe = http.get(joinUrls(hostUrl, loadUserIdUrl), () => {
  return HttpResponse.json({
    data: 'fancy data string',
  } as HandleMeResponse);
});
