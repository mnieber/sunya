import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { StepListView } from '/src/steps/components/StepListView';
import { cn } from '/src/utils/classnames';

// Import styles
import './StepsView.scss';

export type PropsT = {
  className?: any;
};

const ContextProps = {};

export const StepsView = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    return (
      /*
      🔳 StepsView 🔳
      */
      <div className={cn('StepsView', [props.className])}>
        <StepListView />
      </div>
    );
  }, ContextProps)
);
