import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { Route, Switch } from 'wouter';
import { ProjectStateProvider } from '/src/projects/components/ProjectStateProvider';
import { SelectProjectLeadEffect } from '/src/projects/components/SelectProjectLeadEffect';
import { projectsRoutes } from '/src/projects/routes';
import { ext } from '/src/routes/navHandler';
import { SelectScenarioEffect } from '/src/scenarios/components/SelectScenarioEffect';
import { scenariosRoutes } from '/src/scenarios/routes';
import { StepTreeStateProvider } from '/src/steps/components/StepTreeStateProvider';

type PropsT = {
  className?: any;
};

const ContextProps = {};

export const ProjectsSwitch = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    return (
      <Switch>
        <Route path={ext(projectsRoutes.projects())}>
          <Route path={projectsRoutes.projects()}>
            <div>Projects</div>
          </Route>
          <Route path={ext(projectsRoutes.project())}>
            <SelectProjectLeadEffect />
            <ProjectStateProvider>
              <Route path={scenariosRoutes.scenario()}>
                <SelectScenarioEffect />
                <StepTreeStateProvider>
                  <div>Project Page</div>
                </StepTreeStateProvider>
              </Route>
            </ProjectStateProvider>
          </Route>
        </Route>
      </Switch>
    );
  }, ContextProps)
);
