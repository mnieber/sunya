import { getRefreshToken, post, setAuthTokens } from '/src/api/restClient';
import { wait } from '/src/utils/wait';

export function refreshToken() {
  const url = '/users/refresh-token/';
  return post(url, {
    refreshToken: getRefreshToken(),
  }).then((response) => {
    setAuthTokens(response.data.token, response.data.refreshToken);
    return wait(import.meta.env.DEV ? 1000 : 0, {});
  });
}
