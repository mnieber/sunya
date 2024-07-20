import React from 'react';
import { AuthState } from '/src/auth/AuthState';
import { useLoadUserId } from '/src/auth/endpoints/queries';
import { States } from '/src/auth/endpoints/states';
import { AuthStateContext } from '/src/auth/hooks/useAuthStateContext';
import { AuthNav, type AuthRoutesT } from '/src/auth/routeTable';
import { getRouteFns } from '/src/routes/routeTable';
import { createGetProps } from '/src/utils/createGetProps';
import { useBuilder } from '/src/utils/hooks/useBuilder';

type PropsT = React.PropsWithChildren<{}>;

export const AuthStateProvider = (props: PropsT) => {
  const authState = useBuilder(() => new AuthState(States.INITIAL));
  useLoadUserId();

  const authNav = useBuilder(
    () => new AuthNav({ routeFns: getRouteFns<AuthRoutesT>() })
  );

  const getAuthStateContext = () => {
    return createGetProps({
      authState: () => authState,
      authNav: () => authNav,
    });
  };

  return (
    <AuthStateContext.Provider value={getAuthStateContext()}>
      {props.children}
    </AuthStateContext.Provider>
  );
};
