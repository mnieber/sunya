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
          rootStep: {
            id: 'rootStepId',
            fact: [],
            parentStepId: null,
            childSteps: [
              {
                id: 'baseStep0',
                fact: [
                  { type: 'string', value: 'The' },
                  { type: 'actor', value: 'alice@example.com+:user' },
                  { type: 'string', value: 'signs in' },
                ],
                parentStepId: null,
                childSteps: [
                  {
                    id: 'nestedStep1',
                    fact: [
                      {
                        type: 'string',
                        value: 'Alice navigates to the dashboard',
                      },
                    ],
                    parentStepId: 'baseStep0',
                    childSteps: [],
                    fieldDeltaSetByActorKey: {
                      'alice@example.com+:user': {
                        currentPage: 'dashboard',
                      },
                    },
                  },
                  {
                    id: 'nestedStep2',
                    fact: [
                      {
                        type: 'string',
                        value: 'Alice opens the project creation modal',
                      },
                    ],
                    parentStepId: 'baseStep0',
                    childSteps: [
                      {
                        id: 'deeplyNestedStep1',
                        fact: [
                          {
                            type: 'string',
                            value: 'Alice enters project details',
                          },
                        ],
                        parentStepId: 'nestedStep2',
                        childSteps: [],
                        fieldDeltaSetByActorKey: {
                          'alice@example.com+:user': {
                            projectName: 'New Project',
                            projectDescription: 'A sample project',
                          },
                        },
                      },
                      {
                        id: 'deeplyNestedStep2',
                        fact: [
                          {
                            type: 'string',
                            value: 'Alice submits the project creation form',
                          },
                        ],
                        parentStepId: 'nestedStep2',
                        childSteps: [],
                        fieldDeltaSetByActorKey: {
                          'alice@example.com+:user': {
                            projects: ['New Project'],
                          },
                        },
                      },
                    ],
                    fieldDeltaSetByActorKey: {
                      'alice@example.com+:user': {
                        isProjectModalOpen: true,
                      },
                    },
                  },
                ],
                fieldDeltaSetByActorKey: {
                  'alice@example.com+:user': {
                    email: 'alice@example.com',
                    isAuthenticated: true,
                  },
                },
              },
              {
                id: 'baseStep1',
                fact: [
                  { type: 'string', value: 'The' },
                  { type: 'actor', value: 'bob@example.com+:user' },
                  { type: 'string', value: 'joins the project' },
                ],
                parentStepId: null,
                childSteps: [],
                fieldDeltaSetByActorKey: {
                  'bob@example.com+:user': {
                    email: 'bob@example.com',
                    isAuthenticated: true,
                    projects: ['New Project'],
                  },
                },
              },
            ],
            fieldDeltaSetByActorKey: {},
          },
        }),
        createScenario({
          name: 'Mock Scenario 2',
        }),
      ],
    });

    return HttpResponse.json(mockProject);
  }
);
