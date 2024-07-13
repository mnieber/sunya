import axios from 'axios';
import camelcaseKeys from 'camelcase-keys';
import snakecaseKeys from 'snakecase-keys';

axios.defaults.withCredentials = true;

export const hostUrl = window.location.host.startsWith('localhost')
  ? import.meta.env.VITE_LOCALHOST_API_ENDPOINT
  : import.meta.env.VITE_BACKEND_API_ENDPOINT ?? '';

export function get(query: string) {
  return axios.get(`${hostUrl}${trimLeadingSlash(query)}`).then((response) => {
    response.data = camelcaseKeys(response.data);
    return response;
  });
}

export function post(query: string, variables: any) {
  return axios.post(
    `${hostUrl}${trimLeadingSlash(query)}`,
    snakecaseKeys(variables)
  );
}

function trimLeadingSlash(query: string) {
  if (query.startsWith('/') && hostUrl.endsWith('/')) {
    query = query.substring(1);
  }
  return query;
}
