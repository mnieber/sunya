import axios from 'axios';
import camelcaseKeys from 'camelcase-keys';
import snakecaseKeys from 'snakecase-keys';

axios.defaults.withCredentials = true;

export const hostUrl = window.location.host.startsWith('localhost')
  ? import.meta.env.VITE_LOCALHOST_API_ENDPOINT
  : import.meta.env.VITE_BACKEND_API_ENDPOINT ?? '';

export function get(query: string) {
  return axios
    .get(`${hostUrl}${trimLeadingSlash(query)}`, {
      headers: getHeaders(),
    })
    .then((response) => {
      response.data = camelcaseKeys(response.data, { deep: true });
      return response;
    });
}

export function post(query: string, variables: any, headers?: any) {
  const allHeaders = {
    ...getHeaders(),
    ...(headers ?? {}),
  };

  const body =
    variables instanceof FormData
      ? variables
      : snakecaseKeys(variables, { deep: true });

  return axios
    .post(`${hostUrl}${trimLeadingSlash(query)}`, body, {
      headers: allHeaders,
    })
    .then((response) => {
      response.data = camelcaseKeys(response.data, { deep: true });
      return response;
    });
}

function getHeaders() {
  const accessToken = getAccessToken();
  return accessToken
    ? {
        Authorization: `Bearer ${accessToken}`,
      }
    : {};
}

function trimLeadingSlash(query: string) {
  if (query.startsWith('/') && hostUrl.endsWith('/')) {
    query = query.substring(1);
  }
  return query;
}

export const setAuthTokens = (
  accessToken: string | undefined,
  refreshToken?: string
) => {
  if (accessToken === undefined) {
    localStorage.removeItem('accessToken');
  } else {
    localStorage.setItem('accessToken', accessToken);
  }
  if (refreshToken === undefined) {
    localStorage.removeItem('refreshToken');
  } else {
    localStorage.setItem('refreshToken', refreshToken);
  }
};

export const getAccessToken = () => {
  return localStorage.getItem('accessToken');
};

export const getRefreshToken = () => {
  return localStorage.getItem('refreshToken');
};
