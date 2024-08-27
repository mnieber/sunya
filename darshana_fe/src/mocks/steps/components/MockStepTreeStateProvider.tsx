import { QueryClientProvider } from '@tanstack/react-query';
import { observer } from 'mobx-react-lite';
import React, { useEffect } from 'react';
import { withContextProps } from 'react-props-from-context';
import { queryClient } from '/src/api/queryClient';
import { ProjectLeadsStateProvider } from '/src/projects/components/ProjectLeadsStateProvider';
import { ProjectStateProvider } from '/src/projects/components/ProjectStateProvider';
import { projectCtx } from '/src/projects/hooks/useProjectContext';
import { projectLeadsCtx } from '/src/projects/hooks/useProjectLeadsContext';
import { StepTreeStateProvider } from '/src/steps/components/StepTreeStateProvider';
import { stepTreeCtx } from '/src/steps/hooks/useStepTreeContext';

const ContextProps = {
  projectLeads: projectLeadsCtx.projectLeads,
  projectLeadsHighlight: projectLeadsCtx.projectLeadsHighlight,
  project: projectCtx.project,
  stepTreeState: stepTreeCtx.stepTreeState,
};

type PropsT = React.PropsWithChildren<{}>;

export const MockStepTreeStateProvider = observer((props: PropsT) => {
  return (
    <QueryClientProvider client={queryClient}>
      <ProjectLeadsStateProvider>
        <ProjectStateProvider>
          <StepTreeStateProvider>
            <InnerComponent {...props} />
          </StepTreeStateProvider>
        </ProjectStateProvider>
      </ProjectLeadsStateProvider>
    </QueryClientProvider>
  );
});

const InnerComponent = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    useEffect(() => {
      if (props.projectLeads.length > 0) {
        props.projectLeadsHighlight.set({ itemId: props.projectLeads[0].id });
      }
    }, [props.projectLeads, props.projectLeadsHighlight]);

    useEffect(() => {
      const scenario = props.project?.scenarios[0];
      if (scenario) {
        const step = scenario.rootStep.childSteps[0];
        props.stepTreeState.actionsCtr.setHighlightedActor(
          step,
          step.fact[1].value
        );
      }
    }, [props.project, props.stepTreeState]);

    return props.children;
  }, ContextProps)
);
