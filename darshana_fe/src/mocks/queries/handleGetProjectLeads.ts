import { http, HttpResponse } from 'msw';
import { hostUrl } from '/src/api/restClient';
import { createProjectLead } from '/src/api/types/ProjectLeadT';

export const handleGetProjectLeads = http.get(
  `${hostUrl}projects/leads/`,
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

    return HttpResponse.json(mockProjectLeads);
  }
);
