import * as Skandha from 'skandha';
import { Highlight } from 'skandha-facets';
import { ProjectT } from '/src/api/types/ProjectT';
import { ScenarioT } from '/src/api/types/ScenarioT';
import { ProjectData } from '/src/projects/ProjectState/ProjectData';
import { ScenariosData } from '/src/projects/ProjectState/ScenariosData.ts';
import { registerProjectCtr } from '/src/projects/ProjectState/registerProjectCtr';
import { registerScenariosCtr } from '/src/projects/ProjectState/registerScenariosCtr';

export type PropsT = {
  getProject: () => ProjectT | undefined;
};

export class ProjectState {
  props: PropsT;

  projectCtr = {
    data: new ProjectData(),
  };

  scenariosCtr = {
    data: new ScenariosData(),
    highlight: new Highlight<ScenarioT>(),
  };

  destroy() {
    Skandha.cleanUpCtr(this);
  }

  constructor(props: PropsT) {
    this.props = props;
    registerProjectCtr(this);
    registerScenariosCtr(this);
  }
}
