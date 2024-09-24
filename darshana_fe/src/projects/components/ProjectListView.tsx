import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { ProjectLeadT } from '/src/api/types/ProjectLeadT';
import { L } from '/src/frames/layout';
import { projectLeadsCtx } from '/src/projects/hooks/useProjectLeadsContext';
import { projectsNav } from '/src/projects/routes';
import { RouterLink } from '/src/routes/components/RouterLink';
import { cn } from '/src/utils/classnames';

// Import styles
import './ProjectListView.scss';

import { DeleteProjectButton } from '/src/projects/components/DeleteProjectButton';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  projectLeads: projectLeadsCtx.projectLeads,
  projectLeadsDeletion: projectLeadsCtx.projectLeadsDeletion,
};

export const ProjectListView = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const projectLeadItems = props.projectLeads.map(
      (projectLead: ProjectLeadT) => (
        <div
          key={projectLead.id}
          className={cn('ProjectListView__Item', 'mb-2 flex items-center')}
        >
          <RouterLink
            to={projectsNav.project({ projectId: projectLead.id }).url}
            className={cn('mr-2 text-blue-300 hover:underline')}
          >
            {projectLead.name}
          </RouterLink>
          <DeleteProjectButton className="ml-4" projectLead={projectLead} />
        </div>
      )
    );

    return (
      <div className={cn('ProjectListView', [L.col.banner(), props.className])}>
        {projectLeadItems}
      </div>
    );
  }, ContextProps)
);
