import { ResultT } from '/src/api/types/ResultT';

/**
 * Check if lhs is upstream of rhs (i.e., lhs is a dependency of rhs).
 * This means rhs has lhs as a parent (direct or transitive).
 */
export const isUpstream = (
  lhs: ResultT,
  rhs: ResultT,
  resultById: Record<string, ResultT>
): boolean => {
  // Base case: same result
  if (lhs.id === rhs.id) {
    return false;
  }

  // Check if lhs is a direct or transitive parent of rhs
  const visited = new Set<string>();
  const queue: string[] = [...rhs.parentResultNames];

  while (queue.length > 0) {
    const parentId = queue.shift()!;

    // Avoid cycles
    if (visited.has(parentId)) {
      continue;
    }
    visited.add(parentId);

    // Found it - lhs is upstream of rhs
    if (parentId === lhs.id) {
      return true;
    }

    // Continue searching up the dependency tree
    const parent = resultById[parentId];
    if (parent) {
      queue.push(...parent.parentResultNames);
    }
  }

  return false;
};

export const isRelated = (
  lhs: ResultT,
  rhs: ResultT,
  resultByName: Record<string, ResultT>
): boolean => {
  return (
    isUpstream(lhs, rhs, resultByName) || isUpstream(rhs, lhs, resultByName)
  );
};
