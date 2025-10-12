import { action, makeObservable, observable } from 'mobx';
import { createHtmlPortalNode } from 'react-reverse-portal';

export class AppState {
  @observable showRoadmapContents: boolean = true;

  portals = {
    atlasHeader: createHtmlPortalNode(),
    zoomButton: createHtmlPortalNode(),
    showFutureMilestonesButton: createHtmlPortalNode(),
    showCompletedMilestonesButton: createHtmlPortalNode(),
  };

  constructor() {
    makeObservable(this);
  }

  toggleShowRoadmapContents = action((show?: boolean) => {
    if (show !== undefined) {
      this.showRoadmapContents = show;
    } else {
      this.showRoadmapContents = !this.showRoadmapContents;
    }
  });
}
