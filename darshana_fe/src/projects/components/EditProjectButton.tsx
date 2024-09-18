import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { ToolButton } from '/src/frames/components/ToolButton';
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
      <ToolButton
        iconName="pencil"
        className={cn('EditProjectButton', props.className)}
        onClick={handleClick}
        label={props.label ?? 'Edit project'}
      />
    );
  }, ContextProps)
);
