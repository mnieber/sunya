import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { ActionButton } from '/src/frames/components/ActionButton/ActionButton';
import { projectCtx } from '/src/projects/hooks/useProjectContext';
import { cn } from '/src/utils/classnames';

// Import styles
import './EditProjectButton.scss';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  projectEdit: projectCtx.projectEdit,
};

export const EditProjectButton = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const handleClick = () => {
      props.projectEdit.enable();
    };

    return (
      <ActionButton
        className={cn('EditProjectButton', props.className)}
        onClick={handleClick}
        label="Edit Project"
      />
    );
  }, ContextProps)
);
