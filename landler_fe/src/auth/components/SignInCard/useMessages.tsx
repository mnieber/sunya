import type { AuthRoutesT } from '/src/auth/routeTable';
import { RouterLink } from '/src/routes/components';
import { getRouteFns } from '/src/routes/routeTable';

export const useMessages = () => {
  const routes = getRouteFns<AuthRoutesT>();

  const divChangedYourMind = (
    <div>
      Changed your mind? You can return to the{' '}
      <RouterLink to={routes.home()}>home</RouterLink> page.
    </div>
  );

  return {
    messages: {
      divAMagicLinkHasBeenSentToYourEmailAddress:
        'A magic link has been sent to your email address.',
      divChangedYourMind,
      createAccount: 'Create An Account',
    },
  };
};
