import { QueryClientProvider } from '@tanstack/react-query';
import { observer } from 'mobx-react-lite';
import React, { useEffect } from 'react';
import { withContextProps } from 'react-props-from-context';
import { queryClient } from '/src/api/queryClient';
import { ProjectLeadsStateProvider } from '/src/projects/components/ProjectLeadsStateProvider';
import { ProjectStateProvider } from '/src/projects/components/ProjectStateProvider';
import { projectLeadsCtx } from '/src/projects/hooks/useProjectLeadsContext';
import { StepTreeStateProvider } from '/src/steps/components/StepTreeStateProvider';

const ContextProps = {
  projectLeads: projectLeadsCtx.projectLeads,
  projectLeadsHighlight: projectLeadsCtx.projectLeadsHighlight,
};

type PropsT = React.PropsWithChildren<{}>;

export const MockStepTreeStateProvider = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    useEffect(() => {
      if (props.projectLeads.length > 0) {
        props.projectLeadsHighlight.set({ itemId: props.projectLeads[0].id });
      }
    }, [props.projectLeads, props.projectLeadsHighlight]);

    return (
      <QueryClientProvider client={queryClient}>
        <ProjectLeadsStateProvider>
          <ProjectStateProvider>
            <StepTreeStateProvider>{props.children}</StepTreeStateProvider>
          </ProjectStateProvider>
        </ProjectLeadsStateProvider>
      </QueryClientProvider>
    );
  }, ContextProps)
);
