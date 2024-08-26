// File: src/mocks/queries/handleGetProjects.ts

import { http, HttpResponse } from 'msw';
import { hostUrl } from '/src/api/restClient';
import { createProject } from '/src/api/types/ProjectT';
import { createScenario } from '/src/api/types/ScenarioT';

export const handleGetProjects = http.get(`${hostUrl}projects/list/`, () => {
  const mockProjects = [
    createProject({
      name: 'Mock Project 1',
      scenarios: [
        createScenario({ name: 'Scenario 1.1' }),
        createScenario({ name: 'Scenario 1.2' }),
      ],
    }),
    createProject({
      name: 'Mock Project 2',
      scenarios: [createScenario({ name: 'Scenario 2.1' })],
    }),
    createProject({
      name: 'Mock Project 3',
      scenarios: [],
    }),
  ];

  return HttpResponse.json(mockProjects);
});
