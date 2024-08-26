import { http, HttpResponse } from 'msw';
import { hostUrl } from '/src/api/restClient';
import { createScenario } from '/src/api/types/ScenarioT';
import { createStep } from '/src/api/types/StepT';

export const handleGetScenarios = http.get(`${hostUrl}scenarios/list/`, () => {
  const mockRootStep = createStep({
    fact: ['Root step'],
    childSteps: [],
    fieldDeltaSetByActorKey: {},
  });

  return HttpResponse.json([
    createScenario({
      name: 'My First Scenario',
      rootStep: mockRootStep,
    }),
    createScenario({
      name: 'Another Scenario',
      rootStep: mockRootStep,
    }),
  ]);
});
