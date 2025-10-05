import * as R from 'ramda';
import React from 'react';
import { Highlight, Selection } from 'skandha-facets';
import { ResultT } from '/src/api/types';
import { ResultsState } from '/src/results/ResultsState';

export const ResultsContext = React.createContext<any>(null);

export const useResultsContext = () => {
  const context = React.useContext(ResultsContext);
  if (!context) {
    throw new Error(
      'useResultsContext must be used within a ResultsContext.Provider'
    );
  }
  return context;
};

export const resultsCtx = R.mergeAll([
  {
    resultsState: [useResultsContext, 'resultsState'] as any as ResultsState,
    resultsActions: [
      useResultsContext,
      'resultsActions',
    ] as any as ResultsState['actionsCtr'],
    result: [
      //
      useResultsContext,
      'result',
    ] as any as ResultT,
    results: [
      //
      useResultsContext,
      'results',
    ] as any as ResultT[],
    resultsHighlight: [
      useResultsContext,
      'resultsHighlight',
    ] as any as Highlight,
    resultsSelection: [
      useResultsContext,
      'resultsSelection',
    ] as any as Selection,
  },
]);
