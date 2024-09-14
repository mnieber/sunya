import { observer } from 'mobx-react-lite';
import React from 'react';
import { withContextProps } from 'react-props-from-context';
import { ProjectLeadT } from '/src/api/types/ProjectLeadT';
import { ConfirmationDialog } from '/src/frames/components/ConfirmationDialog';
import { Icon, IconS } from '/src/frames/components/Icon';
import { projectLeadsCtx } from '/src/projects/hooks/useProjectLeadsContext';
import { cn } from '/src/utils/classnames';

// Import styles
import './DeleteProjectButton.scss';

export type PropsT = {
  projectLead: ProjectLeadT;
  className?: any;
};

export const ContextProps = {
  projectLeadsDeletion: projectLeadsCtx.projectLeadsDeletion,
};

export const DeleteProjectButton = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const [isConfirmOpen, setIsConfirmOpen] = React.useState(false);

    const handleConfirmDelete = () => {
      props.projectLeadsDeletion.delete({
        itemIds: [props.projectLead.id],
      });
    };

    return (
      <>
        <Icon
          name="trash"
          className={cn(
            'cursor-pointer text-red-500 hover:text-red-700',
            IconS.size.s15(),
            IconS.color.gray()
          )}
          onClick={() => setIsConfirmOpen(true)}
        />
        <ConfirmationDialog
          isOpen={isConfirmOpen}
          onClose={() => setIsConfirmOpen(false)}
          onConfirm={handleConfirmDelete}
          title="Delete Project"
          message="Are you sure you want to delete this project? This action cannot be undone."
          confirmLabel="Delete"
          cancelLabel="Cancel"
        />
      </>
    );
  }, ContextProps)
);
