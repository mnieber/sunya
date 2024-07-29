import { restApi } from 'src/api/rest/client';
import { handleMe } from 'src/mocks/users';
import { withMswHandlers } from 'src/mocks/utils/withMswHandlers';

describe(
  'testMsw',
  withMswHandlers([handleMe], () => {
    it('displays data from backend', async () => {
      const response = await restApi.get('user/me/', { params: {} });
      expect(response.data).toEqual({
        data: 'fancy data string',
      });
    });
  }),
);
