import * as R from 'ramda';
import { data } from 'skandha';
import { ResultT } from '/src/api/types';

export class ResultsData {
  static className = () => 'ResultsData';

  @data results: ResultT[] = [];

  @data get resultById() {
    return R.indexBy(R.prop('id'), this.results);
  }
}
