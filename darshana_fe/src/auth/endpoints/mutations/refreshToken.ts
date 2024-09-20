import { z } from 'zod';
import { getRefreshToken, post, setAuthTokens } from '/src/api/restClient';
import { parseResponse } from '/src/api/utils/parseResponse';
import { waitOnDev } from '/src/utils/wait';

export function refreshToken() {
  const url = '/users/refresh-token/';
  return post(url, {
    refresh_token: getRefreshToken(),
  }).then((response) => {
    const schema = z.object({
      token: z.string(),
      refreshToken: z.string(),
    });
    const res = parseResponse(schema, response.data);

    setAuthTokens(res.token, res.refreshToken);
    return waitOnDev(1000, response);
  });
}
