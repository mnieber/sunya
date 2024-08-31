import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { ActorView } from '/src/actors/components/ActorView';
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
        <ActorView />
      </div>
    );
  }, ContextProps)
);
