import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { ActorContextView } from '/src/actors/components/ActorContextView';
import { StepTreeView } from '/src/steps/components/StepTreeView';
import { cn } from '/src/utils/classnames';

type PropsT = {
  className?: string;
};

const ContextProps = {};

export const ScenarioPage = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    return (
      <div className={cn('ScenarioPage', props.className)}>
        <StepTreeView />
        <ActorContextView />
      </div>
    );
  }, ContextProps)
);
