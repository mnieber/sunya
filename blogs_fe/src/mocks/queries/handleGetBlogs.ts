import { http, HttpResponse } from 'msw';
import { hostUrl } from '/src/api/restClient';
import { createBlog } from '/src/api/types/BlogT';

export const handleGetBlogs = http.get(`${hostUrl}blogs/list/`, () => {
  return HttpResponse.json([
    createBlog({
      name: 'Judo',
    }),
    createBlog({
      name: 'Karate',
    }),
  ]);
});
