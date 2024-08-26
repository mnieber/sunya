import { http, HttpResponse } from 'msw';
import { hostUrl } from '/src/api/restClient';
import { createProject } from '/src/api/types/ProjectT';
import { createScenario } from '/src/api/types/ScenarioT';

export const handleGetProject = http.get(
  `${hostUrl}projects/:projectId/`,
  ({ params }) => {
    const projectId = params.projectId as string;

    const mockProject = createProject({
      id: projectId,
      name: 'Mock Project',
      scenarios: [
        createScenario({
          name: 'Mock Scenario 1',
        }),
        createScenario({
          name: 'Mock Scenario 2',
        }),
      ],
    });

    return HttpResponse.json(mockProject);
  }
);
