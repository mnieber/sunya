import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { ActionButton } from '/src/frames/components/ActionButton/ActionButton';
import { projectLeadsCtx } from '/src/projects/hooks/useProjectLeadsContext';
import { cn } from '/src/utils/classnames';

// Import styles
import './EditProjectButton.scss';

export type PropsT = {
  className?: any;
  label?: string;
};

const ContextProps = {
  projectLeadsEdit: projectLeadsCtx.projectLeadsEdit,
};

export const EditProjectButton = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const handleClick = () => {
      props.projectLeadsEdit.enable();
    };

    return (
      <ActionButton
        className={cn('EditProjectButton', props.className)}
        onClick={handleClick}
        label={props.label ?? 'Edit Project'}
      />
    );
  }, ContextProps)
);
