import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { Portal } from '/src/frames/components/Portal';
import { dashboardCtx } from '/src/frames/hooks/useDashboardStateContext';
import { L } from '/src/frames/layout';
import { EditProjectButton } from '/src/projects/components/EditProjectButton';
import { ProjectLeadFormView } from '/src/projects/components/ProjectLeadFormView';
import { ProjectListView } from '/src/projects/components/ProjectListView';
import { projectLeadsCtx } from '/src/projects/hooks/useProjectLeadsContext';
import { cn } from '/src/utils/classnames';

// Import styles
import './ProjectsPage.scss';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  projectLeadsEdit: projectLeadsCtx.projectLeadsEdit,
  buttonsPortalElm: dashboardCtx.buttonsPortalElm,
};

export const ProjectsPage = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    return (
      <div className={cn('ProjectsPage', L.col.canvas(), props.className)}>
        {
          // 🔳 ButtonsCard 🔳
        }
        <Portal elm={props.buttonsPortalElm}>
          <EditProjectButton className="mb-4" label={'Create project'} />
        </Portal>
        {
          // 🔳 Body 🔳
        }
        <div className={cn(L.col.skewer(), 'p-4')}>
          {props.projectLeadsEdit.isEditing && (
            <ProjectLeadFormView className="mb-4" />
          )}
          <ProjectListView className="mt-4" />
        </div>
      </div>
    );
  }, ContextProps)
);
