import { ResultT } from '/src/api/types/ResultT';

export const topologicalSort = (
  results: ResultT[],
  tieBreaker?: (a: ResultT, b: ResultT) => number
): ResultT[] => {
  // Create a mapping of result ID to result object
  const resultMap = new Map<string, ResultT>();
  results.forEach((result) => resultMap.set(result.id, result));

  // Calculate in-degree (number of parents) for each result
  const inDegree = new Map<string, number>();
  results.forEach((result) =>
    inDegree.set(result.id, result.parentResultIds.length)
  );

  // Start with results that have no parents
  let currentLayer: ResultT[] = results.filter(
    (result) => inDegree.get(result.id) === 0
  );
  if (tieBreaker) {
    currentLayer.sort(tieBreaker);
  }

  const result: ResultT[] = [];

  while (currentLayer.length > 0) {
    const nextLayer: ResultT[] = [];

    // Process all results in the current layer
    for (const current of currentLayer) {
      result.push(current);

      // Find all children of this result and decrease their in-degree
      results.forEach((result) => {
        if (result.parentResultIds.includes(current.id)) {
          const newDegree = inDegree.get(result.id)! - 1;
          inDegree.set(result.id, newDegree);
          if (newDegree === 0) {
            nextLayer.push(result);
          }
        }
      });
    }

    // Sort the next layer before processing
    if (tieBreaker && nextLayer.length > 0) {
      nextLayer.sort(tieBreaker);
    }

    currentLayer = nextLayer;
  }

  // Check if all results were processed (cycle detection)
  if (result.length !== results.length) {
    throw new Error('Cycle detected in the graph!');
  }

  return result;
};
