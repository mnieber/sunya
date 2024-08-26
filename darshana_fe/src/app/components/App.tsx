import { QueryClientProvider } from '@tanstack/react-query';
import * as R from 'ramda';
import { queryClient } from '/src/api/queryClient';
import { flags } from '/src/app/flags';
import { L } from '/src/frames/layout';
import { MockApp } from '/src/mocks/app/components/MockApp';
import { ProjectEntriesStateProvider } from '/src/projects/components/ProjectEntriesStateProvider';
import { ProjectStateProvider } from '/src/projects/components/ProjectStateProvider';
import { NavStateProvider } from '/src/routes/components/NavStateProvider';
import { StepTreeStateProvider } from '/src/steps/components/StepTreeStateProvider';
import { cn } from '/src/utils/classnames';

export const App = () => {
  return flags.mockApp ? (
    <AppBody>
      <MockApp />
    </AppBody>
  ) : (
    <QueryClientProvider client={queryClient}>
      <NavStateProvider>
        <ProjectEntriesStateProvider>
          <ProjectStateProvider>
            <StepTreeStateProvider>
              <AppBody></AppBody>
            </StepTreeStateProvider>
          </ProjectStateProvider>
        </ProjectEntriesStateProvider>
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
