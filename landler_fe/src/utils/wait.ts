export function wait<T>(ms: number, value: T) {
  return new Promise<T>((resolve) => setTimeout(resolve, ms, value));
}

export function waitOnDev<T>(ms: number, value: T) {
  return new Promise<T>((resolve) =>
    setTimeout(resolve, ms, import.meta.env.DEV ? value : 0)
  );
}
