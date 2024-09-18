import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { ToolButton } from '/src/frames/components/ToolButton';
import { projectCtx } from '/src/projects/hooks/useProjectContext';
import { cn } from '/src/utils/classnames';

// Import styles
import './ImportSpecFilesButton.scss';

export type PropsT = {
  className?: any;
  label?: string;
};

const ContextProps = {
  projectEdit: projectCtx.projectEdit,
};

export const ImportSpecFilesButton = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const handleClick = () => {
      props.projectEdit.enable();
    };

    return (
      <ToolButton
        iconName="repeat"
        className={cn('ImportSpecFilesButton', props.className)}
        onClick={handleClick}
        label={props.label ?? 'Upload spec files'}
      />
    );
  }, ContextProps)
);
