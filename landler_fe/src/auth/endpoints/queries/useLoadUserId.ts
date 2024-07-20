import { useQuery } from '@tanstack/react-query';
import { queryClient } from '/src/api/queryClient';
import { get, getRefreshToken, setAuthTokens } from '/src/api/restClient';
import { AuthState } from '/src/auth/AuthState';
import { refreshToken } from '/src/auth/endpoints/mutations/refreshToken';
import { createQueryKey } from '/src/auth/utils/createQueryKey';
import { ObjT } from '/src/utils/types';

export class Anonymous {}
export const anonymous = new Anonymous();

export type ArgsT = {
  maybeRefreshToken: boolean;
};

export function loadUserId(args: ArgsT): Promise<any> {
  const url = '/users/user-id/';

  return get(url)
    .then((response: ObjT) => {
      return {
        userId: response.username ?? anonymous,
        isAuthenticated: !!response.username,
      };
    })
    .catch((error: ObjT) => {
      const message = error.response.errors[0].message;
      if (
        ['Signature has expired', 'Error decoding signature'].includes(
          message
        ) &&
        getRefreshToken() &&
        args.maybeRefreshToken
      ) {
        // Try to refresh the token. Regardless of whether that worked, retry the
        // loadUserId, but this time with maybeRefreshToken set to false.
        return refreshToken().finally(() =>
          loadUserId({ maybeRefreshToken: false })
        );
      }

      // If we get here, then there was an unresolvable problem with the auth tokens,
      // and we've already tried to refresh them. In that case, clear the tokens and
      // throw an error.
      setAuthTokens(undefined, undefined);
      throw new Error(message);
    })
    .catch(() => {
      return {
        userId: anonymous,
        isAuthenticated: false,
      };
    });
}

export type QueryKeyT = {};

export function queryKey(args: QueryKeyT) {
  return createQueryKey<QueryKeyT>('loadUserId', args);
}

export const useLoadUserId = (authState?: AuthState) => {
  return useQuery({
    queryKey: queryKey({}),
    queryFn: () => {
      return loadUserId({ maybeRefreshToken: true }).then((data) => {
        if (authState) authState.setUserId(data.userId);
        return data;
      });
    },
  });
};

export const invalidateLoadUserId = (args: QueryKeyT) => {
  return queryClient.invalidateQueries({
    queryKey: queryKey(args),
  });
};
