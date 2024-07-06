import axios from 'axios';

axios.defaults.withCredentials = true;

export const hostUrl = window.location.host.startsWith('localhost')
  ? import.meta.env.VITE_LOCALHOST_API_ENDPOINT
  : import.meta.env.VITE_BACKEND_API_ENDPOINT ?? '';

export function get(query: string) {
  return axios.get(`${hostUrl}/${query}`);
}

export function post(query: string, variables: any) {
  return axios.post(`${hostUrl}/${query}`, variables);
}
