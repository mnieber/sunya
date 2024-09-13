import { observer } from 'mobx-react-lite';
import { isLoading } from 'mobx-resource-states';
import { withContextProps } from 'react-props-from-context';
import { L } from '/src/frames/layout';
import { EditProjectButton } from '/src/projects/components/EditProjectButton';
import { ImportSpecFilesButton } from '/src/projects/components/ImportSpecFilesButton';
import { ImportSpecFilesFormView } from '/src/projects/components/ImportSpecFilesFormView/ImportSpecFilesFormView';
import { ProjectLeadFormView } from '/src/projects/components/ProjectLeadFormView';
import { projectCtx } from '/src/projects/hooks/useProjectContext';
import { projectLeadsCtx } from '/src/projects/hooks/useProjectLeadsContext';
import { ScenarioListView } from '/src/scenarios/components/ScenarioListView';
import { cn } from '/src/utils/classnames';

// Import styles
import './ProjectPage.scss';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  project: projectCtx.project,
  scenarios: projectCtx.scenarios,
  projectLeadsEdit: projectLeadsCtx.projectLeadsEdit,
  projectEdit: projectCtx.projectEdit,
  projectLead: projectLeadsCtx.projectLead,
};

export const ProjectPage = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    // TODO: should not need !props.project
    if (isLoading(props.project) || !props.project) {
      return <div>Loading project...</div>;
    }

    return (
      <div className={cn('ProjectPage', L.col.canvas(), props.className)}>
        <h1 className="mb-4 text-2xl font-bold">{props.project.name}</h1>
        <p className="mb-4">{props.project.description}</p>
        <div className={cn(L.row.skewer(), 'mb-4')}>
          <EditProjectButton className="" />
          <ImportSpecFilesButton className="" />
        </div>

        <div className={cn(L.col.skewer(), 'p-4')}>
          {props.projectLeadsEdit.isEditing && (
            <ProjectLeadFormView projectLead={props.projectLead} />
          )}
          {props.projectEdit.isEditing && <ImportSpecFilesFormView />}
          <ScenarioListView className="mb-4" />
        </div>
      </div>
    );
  }, ContextProps)
);
