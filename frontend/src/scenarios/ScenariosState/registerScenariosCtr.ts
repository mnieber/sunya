import { setCallbackMap } from 'aspiration';
import { addCleanUpFunctionToCtr, cleanUpCtr, mapDataToProps } from 'skandha';
import { HighlightCbs, SelectionCbs, handleSelectItem } from 'skandha-facets';
import { registerCtr } from 'skandha-mobx';
import { ScenarioT } from '/src/api/types/ScenarioT';
import { ScenariosState } from '/src/scenarios/ScenariosState';
import { getIds } from '/src/utils/ids';

const mapData = (state: ScenariosState) => {
  const ctr = state.scenariosCtr;

  const getScenarioById = (x: string | undefined) =>
    x ? ctr.store.itemById[x] : undefined;

  mapDataToProps(ctr, {
    store: {
      items: () => state.props.getScenarios(),
    },
    selection: {
      selectableIds: () => getIds(ctr.store.items ?? []),
      items: () =>
        ctr.selection.itemIds
          .map(getScenarioById)
          .filter((x?: ScenarioT) => !!x) as ScenarioT[],
    },
    highlight: {
      highlightableIds: () => getIds(ctr.store.items ?? []),
      item: () => getScenarioById(ctr.highlight.itemId),
    },
  });
};

const setCallbacks = (state: ScenariosState) => {
  const ctr = state.scenariosCtr;
  addCleanUpFunctionToCtr(state, () => cleanUpCtr(ctr));

  setCallbackMap(ctr.highlight, {} as HighlightCbs);

  setCallbackMap(ctr.selection, {
    selectItem: {
      selectItem(this: SelectionCbs['selectItem']) {
        handleSelectItem(ctr.selection, this.args);
        // Highlight follows selection
        if (!this.args.isCtrl && !this.args.isShift) {
          ctr.highlight.set({ id: this.args.itemId });
        }
      },
    },
  } as SelectionCbs);
};

export const registerScenariosCtr = (state: ScenariosState) => {
  registerCtr({
    ctr: state.scenariosCtr,
    options: { name: 'ScenariosState.Scenarios' },
    initCtr: () => {
      mapData(state);
      setCallbacks(state);
    },
  });
};
