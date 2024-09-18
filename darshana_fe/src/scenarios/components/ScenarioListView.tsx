import { observer } from 'mobx-react-lite';
import * as R from 'ramda';
import { withContextProps } from 'react-props-from-context';
import { ScenarioT } from '/src/api/types/ScenarioT';
import { L } from '/src/frames/layout';
import { projectCtx } from '/src/projects/hooks/useProjectContext';
import { RouterLink } from '/src/routes/components/RouterLink';
import { scenariosNav } from '/src/scenarios/routes';
import { cn } from '/src/utils/classnames';

// Import styles
import './ScenarioListView.scss';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  project: projectCtx.project,
  scenarios: projectCtx.scenarios,
};

export const ScenarioListView = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    if (!props.project) {
      return null;
    }

    const scenarioItems = props.scenarios.map((scenario: ScenarioT) => (
      <RouterLink
        key={scenario.id}
        to={
          scenariosNav.scenario({
            projectId: props.project.id,
            scenarioId: scenario.id,
          }).url
        }
        className={cn(
          'ScenarioListView__Item',
          R.values({
            color: ['bg-blue-400 text-white'],
            layout: ['rounded-xl p-4'],
            appearance: ['hover:bg-blue-500 hover:underline'],
          })
        )}
      >
        {scenario.name}
      </RouterLink>
    ));

    return (
      <div
        className={cn('ScenarioListView', [L.col.banner(), props.className])}
      >
        {scenarioItems}
      </div>
    );
  }, ContextProps)
);
