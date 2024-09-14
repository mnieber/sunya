import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { Route, Switch } from 'wouter';
import { ProjectPage } from '/src/projects/components/ProjectPage';
import { ProjectStateProvider } from '/src/projects/components/ProjectStateProvider';
import { ProjectsPage } from '/src/projects/components/ProjectsPage';
import { SelectProjectLeadEffect } from '/src/projects/components/SelectProjectLeadEffect';
import { projectsRoutes } from '/src/projects/routes';
import { ext } from '/src/routes/navHandler';
import { ScenarioPage } from '/src/scenarios/components/ScenarioPage';
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
      <Route path={ext(projectsRoutes.projects())}>
        <Switch>
          <Route path={projectsRoutes.projects()}>
            <ProjectsPage />
          </Route>
          <Route path={projectsRoutes.project()}>
            <SelectProjectLeadEffect />
            <ProjectStateProvider>
              <ProjectPage />
              <Route path={scenariosRoutes.scenario()}>
                <SelectScenarioEffect />
                <StepTreeStateProvider>
                  <ScenarioPage />
                </StepTreeStateProvider>
              </Route>
            </ProjectStateProvider>
          </Route>
        </Switch>
      </Route>
    );
  }, ContextProps)
);
