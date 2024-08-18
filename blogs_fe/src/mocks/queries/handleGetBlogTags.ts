import { http, HttpResponse } from 'msw';
import { hostUrl } from '/src/api/restClient';

export const handleGetBlogTags = http.get(`${hostUrl}blogs/tags/*`, () => {
  return HttpResponse.json({
    tags: ['sports', 'music'],
  });
});
