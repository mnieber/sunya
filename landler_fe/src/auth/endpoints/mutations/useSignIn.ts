import { useObservableMutation } from '/src/api/ObservableMutation';
import { post, setAuthTokens } from '/src/api/restClient';
import { AuthState } from '/src/auth/AuthState';
import { ObjT } from '/src/utils/types';
import { waitOnDev } from '/src/utils/wait';

export type ArgsT = {
  userId: string;
  password: string;
};

export function signIn(args: ArgsT) {
  const url = '/users/sign-in/';
  return post(url, {
    signInUserForm: {
      email: args.userId,
      password: args.password,
    },
  })
    .then((response) => {
      setAuthTokens(response.data.token, response.data.refreshToken);
      return waitOnDev(1000, {
        success: true,
      });
    })
    .catch(() => {
      setAuthTokens(undefined, undefined);
      return waitOnDev(1000, {
        success: false,
      });
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
    },
    onError: (error: Error) => {
      if (authState) authState.onErrored(queryName, error.message);
    },
  });
};
