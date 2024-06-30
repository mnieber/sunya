import { QueryClientProvider } from '@tanstack/react-query';
import { Router } from 'react-router-dom';
import { queryClient } from '/src/api/queryClient';
import { L, breakpoints } from '/src/frames/layout';
import { RootSwitch } from '/src/routes/components';
import { history } from '/src/routes/history';
import { cn } from '/src/utils/classnames';

export const App = () => {
  return (
    <QueryClientProvider client={queryClient}>
      <Router history={history}>
        <AppFrame>
          <RootSwitch />
        </AppFrame>
      </Router>
    </QueryClientProvider>
  );
};

export const AppFrame = (props: React.PropsWithChildren<{}>) => {
  return (
    <div
      id="App"
      className={cn('App', [
        L.col.banner(),
        `min-width-[${breakpoints.xs}] h-screen overflow-x-hidden`,
      ])}
      tabIndex={0}
      ref={(x: any) => x.focus()}
    >
      {props.children}
    </div>
  );
};
