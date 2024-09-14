import { observer } from 'mobx-react-lite';
import * as R from 'ramda';
import { withContextProps } from 'react-props-from-context';
import { useSignOut } from '/src/auth/endpoints/mutations/useSignOut';
import { authStateCtx } from '/src/auth/hooks/useAuthStateContext';
import { authNav } from '/src/auth/routes';
import { Icon } from '/src/frames/components';
import { MenuItemS } from '/src/frames/components/MenuItem';
import { L } from '/src/frames/layout';
import { navTo } from '/src/routes/navHandler';
import { cn } from '/src/utils/classnames';

// Import styles
import './AccountMenu.scss';
import '/src/frames/components/DialogButton/DialogButton.scss';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  authState: authStateCtx.authState,
};

export const AccountMenu = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const signOut = useSignOut(props.authState).mutateAsync;

    return (
      <div
        className={cn(
          'AccountMenu',
          R.values({
            preline: 'hs-dropdown ',
            layout: 'relative inline-flex',
            color: 'text-white',
          }),
          [props.className]
        )}
      >
        <button
          type="button"
          className={cn(
            R.values({
              preline: 'hs-dropdown-toggle',
              layout: 'inline-flex items-center justify-center gap-x-2',
            })
          )}
          aria-expanded="false"
          aria-label="Menu"
        >
          Account
        </button>

        <div
          className={cn(
            R.values({
              preline: 'hs-dropdown-menu duration hidden',
              layout: 'z-10 mt-2 w-56 min-w-60',
              appearance:
                'opacity-0 transition-[opacity,margin] hs-dropdown-open:opacity-100',
            })
          )}
          role="menu"
          aria-labelledby="hs-dropdown-unstyled"
        >
          <div
            className={cn(L.row.skewer())}
            onClick={() => navTo(authNav.signIn({}))}
          >
            <Icon className={cn(MenuItemS.Icon())} name="signIn" />
            Sign In
          </div>
          <div
            className={cn(L.row.skewer())}
            onClick={() => {
              signOut({}).then(() => {
                navTo(authNav.signIn({}));
              });
            }}
          >
            <Icon className={cn(MenuItemS.Icon())} name="signOut" />
            Sign Out
          </div>
        </div>
      </div>
    );
  }, ContextProps)
);
