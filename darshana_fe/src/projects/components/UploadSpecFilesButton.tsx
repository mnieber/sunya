import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { ActionButton } from '/src/frames/components/ActionButton/ActionButton';
import { projectCtx } from '/src/projects/hooks/useProjectContext';
import { cn } from '/src/utils/classnames';

// Import styles
import './UploadSpecFilesButton.scss';

export type PropsT = {
  className?: any;
  label?: string;
};

const ContextProps = {
  projectEdit: projectCtx.projectEdit,
};

export const UploadSpecFilesButton = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const handleClick = () => {
      props.projectEdit.enable();
    };

    return (
      <ActionButton
        className={cn('UploadSpecFilesButton', props.className)}
        onClick={handleClick}
        label={props.label ?? 'Upload spec files'}
      />
    );
  }, ContextProps)
);
