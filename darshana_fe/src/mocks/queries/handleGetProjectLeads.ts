import { http, HttpResponse } from 'msw';
import { hostUrl } from '/src/api/restClient';
import { createProjectLead } from '/src/api/types/ProjectLeadT';
import { createScenario } from '/src/api/types/ScenarioT';

export const handleGetProjectLeads = http.get(
  `${hostUrl}projects/leads/`,
  () => {
    const mockProjectLeads = [
      createProjectLead({
        name: 'Mock ProjectLead 1',
        scenarios: [
          createScenario({ name: 'Scenario 1.1' }),
          createScenario({ name: 'Scenario 1.2' }),
        ],
      }),
      createProjectLead({
        name: 'Mock ProjectLead 2',
        scenarios: [createScenario({ name: 'Scenario 2.1' })],
      }),
      createProjectLead({
        name: 'Mock ProjectLead 3',
        scenarios: [],
      }),
    ];

    return HttpResponse.json(mockProjectLeads);
  }
);
