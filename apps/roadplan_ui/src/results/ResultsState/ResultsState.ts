import * as Skandha from 'skandha';
import { ResultT } from '/src/api/types';
import { ResultsData } from '/src/results/ResultsState/ResultsData';
import { registerResultsCtr } from '/src/results/ResultsState/registerResultsCtr';
import { bindActionsCtr } from '/src/utils/bindActionsCtr';

export type PropsT = {
  getResults: () => ResultT[];
};

export class ResultsState {
  props: PropsT;

  resultsCtr = {
    data: new ResultsData(),
    highlight: new Highlight<ResultT>(),
    selection: new Selection<ResultT>(),
  };

  actionsCtr = {};

  destroy() {
    Skandha.cleanUpCtr(this);
  }

  constructor(props: PropsT) {
    this.props = props;
    bindActionsCtr(this.actionsCtr, this);
    registerResultsCtr(this);
  }
}
