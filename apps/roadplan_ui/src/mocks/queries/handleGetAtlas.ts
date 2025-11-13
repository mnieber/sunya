import { http, HttpResponse } from 'msw';
import { hostUrl } from '/src/api/restClient';
import { joinUrls } from '/src/utils/urls';
import { getAtlasUrl } from '/src/api/queries/useGetAtlas';
import { convertDataToSnakeCase } from '/src/api/utils/convertDataToSnakeCase';
import { AtlasSchema } from '/src/api/types/AtlasSchema';

export const handleGetAtlas = http.get(
  joinUrls(hostUrl, getAtlasUrl),
  ({ params }) => {
    return HttpResponse.json(
      convertDataToSnakeCase(AtlasSchema, {
        id: params.atlasId,
        isSyncedWithJira: false,
        createdAt: '2024-01-15T10:00:00Z',
        roadmaps: [
          {
            name: 'Q1 2025 Roadmap',
            owner: 'maarten',
            id: 'q1_2025_roadmap',
            milestones: [
              {
                title: 'Phase 1: Foundation',
                id: 'phase_1_foundation',
                markdownContent: 'Build core infrastructure',
                isFuture: false,
                isCompleted: true,
                results: [
                  {
                    id: 'database schema',
                    name: 'Database schema',
                  },
                  { id: 'api_endpoints', name: 'api-endpoints' },
                ],
              },
              {
                title: 'Phase 2: Features',
                id: 'phase_2_features',
                markdownContent: 'Implement key features',
                isFuture: false,
                isCompleted: false,
                results: [
                  {
                    id: 'user_authentication',
                    name: 'user-authentication',
                    parentResultNames: ['api_endpoints'],
                  },
                  {
                    id: 'data visualization',
                    name: 'Data visualization',
                    owner: 'maarten',
                    parentResultNames: ['user_authentication'],
                  },
                ],
              },
            ],
          },
          {
            name: 'Q2 2025 Roadmap',
            owner: 'pablo',
            id: 'q2_2025_roadmap',
            milestones: [
              {
                title: 'Phase 3: Polish',
                id: 'phase_3_polish',
                markdownContent: 'Refine and optimize',
                isFuture: true,
                isCompleted: false,
                results: [
                  {
                    id: 'performance improvements',
                    name: 'Performance improvements',
                  },
                ],
              },
            ],
          },
        ],
      })
    );
  }
);
