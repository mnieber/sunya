import { http, HttpResponse } from 'msw';
import { hostUrl } from '/src/api/restClient';
import { createProjectEntry } from '/src/api/types/ProjectEntryT';
import { createScenario } from '/src/api/types/ScenarioT';

export const handleGetProjectEntries = http.get(
  `${hostUrl}projects/entries/`,
  () => {
    const mockProjectEntries = [
      createProjectEntry({
        name: 'Mock ProjectEntry 1',
        scenarios: [
          createScenario({ name: 'Scenario 1.1' }),
          createScenario({ name: 'Scenario 1.2' }),
        ],
      }),
      createProjectEntry({
        name: 'Mock ProjectEntry 2',
        scenarios: [createScenario({ name: 'Scenario 2.1' })],
      }),
      createProjectEntry({
        name: 'Mock ProjectEntry 3',
        scenarios: [],
      }),
    ];

    return HttpResponse.json(mockProjectEntries);
  }
);
