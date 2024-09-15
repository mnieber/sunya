import { useObservableMutation } from '/src/api/lib/ObservableMutation';
import { queryClient } from '/src/api/queryClient';
import { post, setAuthTokens } from '/src/api/restClient';
import { AuthState, anonymous } from '/src/auth/AuthState';
import { States } from '/src/auth/endpoints/states';
import { hasErrorCode } from '/src/auth/utils/hasErrorCode';
import { ObjT } from '/src/utils/types';
import { waitOnDev } from '/src/utils/wait';

export type SignInArgsT = {
  userId: string;
  password: string;
};

export function signIn(args: SignInArgsT) {
  const url = '/users/sign-in/';
  return post(url, {
    signInUserForm: {
      email: args.userId,
      password: args.password,
    },
  })
    .then((response) => {
      setAuthTokens(response.data.accessToken, response.data.refreshToken);
      return waitOnDev(1000, {
        success: !!response.data.accessToken,
        userId: response.data.userId,
      });
    })
    .catch((error) => {
      if (
        hasErrorCode(error.response.data, [
          'INVALID_CREDENTIALS',
          'INACTIVE_ACCOUNT',
        ])
      ) {
        setAuthTokens(undefined, undefined);
        return waitOnDev(1000, {
          success: false,
          userId: anonymous,
          errors: [States.INVALID_CREDENTIALS],
        });
      }

      throw error;
    });
}

export const useSignIn = (authState?: AuthState) => {
  const queryName = 'signIn';

  return useObservableMutation({
    mutationFn: signIn,
    onMutate: () => {
      if (authState) authState.onUpdating(queryName);
    },
    onSuccess: (data: ObjT) => {
      if (authState) authState.onUpdated(queryName, data);
      authState?.setUserId(data.userId);
      queryClient.invalidateQueries();
    },
    onError: (error: Error) => {
      if (authState) authState.onErrored(queryName, error.message);
      authState?.setUserId(anonymous);
    },
  });
};
