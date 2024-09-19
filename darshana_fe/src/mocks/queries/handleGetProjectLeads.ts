import { http, HttpResponse } from 'msw';
import { getProjectLeadsUrl } from '/src/api/queries/useGetProjectLeads';
import { hostUrl } from '/src/api/restClient';
import { createProjectLead } from '/src/api/types/ProjectLeadT';
import { joinUrls } from '/src/utils/urls';

export const handleGetProjectLeads = http.get(
  joinUrls(hostUrl, getProjectLeadsUrl),
  () => {
    const mockProjectLeads = [
      createProjectLead({
        id: 'project1',
        name: 'Mock Project 1',
      }),
      createProjectLead({
        id: 'project2',
        name: 'Mock Project 2',
      }),
      createProjectLead({
        id: 'project3',
        name: 'Mock Project 3',
      }),
    ];

    return HttpResponse.json({ results: mockProjectLeads });
  }
);
