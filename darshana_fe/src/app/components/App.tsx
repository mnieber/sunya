import { QueryClientProvider } from '@tanstack/react-query';
import * as R from 'ramda';
import { queryClient } from '/src/api/queryClient';
import { flags } from '/src/app/flags';
import { AuthSwitch } from '/src/auth/components';
import { AuthStateProvider } from '/src/auth/components/AuthStateProvider';
import { DashboardFrame } from '/src/frames/components/DashboardFrame';
import { L } from '/src/frames/layout';
import { MockApp } from '/src/mocks/app/components/MockApp';
import { ProjectLeadsStateProvider } from '/src/projects/components/ProjectLeadsStateProvider';
import { ProjectsSwitch } from '/src/projects/components/ProjectsSwitch';
import { NavStateProvider } from '/src/routes/components/NavStateProvider';
import { cn } from '/src/utils/classnames';

export const App = () => {
  return flags.mockApp ? (
    <AppBody>
      <MockApp />
    </AppBody>
  ) : (
    <QueryClientProvider client={queryClient}>
      <AuthStateProvider>
        <NavStateProvider>
          <ProjectLeadsStateProvider>
            <AppBody>
              <DashboardFrame>
                <AuthSwitch />
                <ProjectsSwitch />
              </DashboardFrame>
            </AppBody>
          </ProjectLeadsStateProvider>
        </NavStateProvider>
      </AuthStateProvider>
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
          size: `min-width-[320px] h-screen max-w-[1600px]`,
          pos: `mx-auto`,
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
