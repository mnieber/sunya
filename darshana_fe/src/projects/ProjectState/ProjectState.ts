import * as Skandha from 'skandha';
import { Highlight } from 'skandha-facets';
import { ProjectT } from '/src/api/types/ProjectT';
import { ScenarioT } from '/src/api/types/ScenarioT';
import { ProjectData } from '/src/projects/ProjectState/ProjectData';
import { ScenariosData } from '/src/projects/ProjectState/ScenariosData.ts';
import { registerProjectCtr } from '/src/projects/ProjectState/registerProjectCtr';
import { registerScenariosCtr } from '/src/projects/ProjectState/registerScenariosCtr';
import { bindActionsCtr } from '/src/utils/bindActionsCtr';

export type PropsT = {
  getProject: () => ProjectT | undefined;
  uploadSpecFiles: (files: File[]) => Promise<void>;
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

  actionsCtr = {
    uploadSpecFiles: (files: File[]) => {
      return this.props.uploadSpecFiles(files);
    },
  };

  destroy() {
    Skandha.cleanUpCtr(this);
  }

  constructor(props: PropsT) {
    this.props = props;
    bindActionsCtr(this.actionsCtr, this);
    registerProjectCtr(this);
    registerScenariosCtr(this);
  }
}
