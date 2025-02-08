import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { Link } from 'wouter';
import { L } from '/src/frames/layout';
import { projectCtx } from '/src/projects/hooks/useProjectContext';
import { projectsNav } from '/src/projects/routes';
import { scenariosNav } from '/src/scenarios/routes';
import { cn } from '/src/utils/classnames';

// Import styles
import './Breadcrumb.scss';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  project: projectCtx.project,
  scenario: projectCtx.scenario,
};

export const Breadcrumb = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const { project, scenario } = props;

    return (
      <nav
        className={cn('Breadcrumb', [L.row.skewer(), 'py-2', props.className])}
      >
        <ol className={cn('flex', 'items-center', 'space-x-4')}>
          <li>
            <Link href={projectsNav.projects({}).url}>
              <div className="text-blue-500 hover:text-blue-600">Projects</div>
            </Link>
          </li>
          <li className="text-gray-500">/</li>
          {project && (
            <>
              <li>
                <Link href={projectsNav.project({ projectId: project.id }).url}>
                  <div className="text-blue-500 hover:text-blue-600">
                    {project.name}
                  </div>
                </Link>
              </li>
              <li className="text-gray-500">/</li>
            </>
          )}
          {scenario && (
            <li>
              <Link
                href={
                  scenariosNav.scenario({
                    projectId: project?.id || '',
                    scenarioId: scenario.id,
                  }).url
                }
              >
                <div className="text-blue-500 hover:text-blue-600">
                  {scenario.name}
                </div>
              </Link>
            </li>
          )}
        </ol>
      </nav>
    );
  }, ContextProps)
);
