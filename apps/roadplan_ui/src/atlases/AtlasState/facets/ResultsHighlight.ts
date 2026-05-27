import { Highlight } from 'skandha-facets';
import { ResultT } from '/src/api/types';
import { AtlasState } from '/src/atlases/AtlasState';
import * as R from 'ramda';
import { findMilestoneAndRoadmapByResultId } from '/src/atlases/utils/findMilestoneAndRoadmapByResultId';

export class ResultsHighlight extends Highlight<ResultT> {
  constructor(private state: AtlasState) {
    super();
  }

  protected onSet(args: { itemId: string | undefined }): void {
    this.highlightRoadmapWhenResultIsHighlighted();
  }

  private highlightRoadmapWhenResultIsHighlighted(): void {
    if (R.isNil(this.itemId)) return;

    const { roadmap } = findMilestoneAndRoadmapByResultId(
      this.state.atlasCtr.data.atlas!,
      this.itemId
    );
    if (roadmap) {
      this.state.roadmapsCtr.highlight.set({ itemId: roadmap.id });
    }
  }
}
