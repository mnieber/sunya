import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { ActionButton } from '/src/frames/components/ActionButton/ActionButton';
import { projectLeadsCtx } from '/src/projects/hooks/useProjectLeadsContext';
import { cn } from '/src/utils/classnames';

// Import styles
import './CreateProjectButton.scss';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  projectLeadsEdit: projectLeadsCtx.projectLeadsEdit,
};

export const CreateProjectButton = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const handleClick = () => {
      props.projectLeadsEdit.enable();
    };

    return (
      <ActionButton
        className={cn('CreateProjectButton', props.className)}
        onClick={handleClick}
        label="Create New Project"
      />
    );
  }, ContextProps)
);
