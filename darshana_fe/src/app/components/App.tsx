import { QueryClientProvider } from '@tanstack/react-query';
import * as R from 'ramda';
import { queryClient } from '/src/api/queryClient';
import { L } from '/src/frames/layout';
import { MockApp } from '/src/mocks/app/components/MockApp';
import { NavStateProvider } from '/src/routes/components/NavStateProvider';
import { RootSwitch } from '/src/routes/components';
import { history } from '/src/routes/history';
import { cn } from '/src/utils/classnames';

export const App = () => {
  return flags.mockApp ? (
    <AppBody>
      <MockApp />
    </AppBody>
  ) : (
    <QueryClientProvider client={queryClient}>
      <NavStateProvider>
        <AppBody>
          <RootSwitch />
        </AppBody>
      </NavStateProvider>
    </QueryClientProvider>
  );
};

const AppBody = (props: React.PropsWithChildren<{}>) => {
  return (
    <div
      id="App"
      className={cn('App', [
        R.values({
          root: L.col.banner(),
          // 320px = breakpoints.xs
          size: `min-width-[320px] h-screen`,
          scroll: 'overflow-x-hidden',
        }),
      ])}
      tabIndex={0}
      ref={(x: any) => x?.focus()}
    >
      {props.children}
    </div>
  );
};
