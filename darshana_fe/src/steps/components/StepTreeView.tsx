import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { ActorView } from '/src/actors/components/ActorView';
import { StepListView } from '/src/steps/components/StepListView';
import { stepTreeCtx } from '/src/steps/hooks/useStepTreeContext';
import { cn } from '/src/utils/classnames';

type PropsT = {
  className?: string;
};

const ContextProps = {
  rootStep: stepTreeCtx.rootStep,
  stepTreeState: stepTreeCtx.stepTreeState,
};

export const StepTreeView = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    if (!props.rootStep) {
      return null;
    }

    return (
      <div className={cn('StepTreeView', props.className)}>
        <StepListView
          step={props.rootStep}
          setHighlightedActor={
            props.stepTreeState.actionsCtr.setHighlightedActor
          }
          depth={0}
        />
        <ActorView />
      </div>
    );
  }, ContextProps)
);
