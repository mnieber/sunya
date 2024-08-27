# Instructions for writing a StateProvider.tsx file

When writing a StateProvider.tsx file, please follow the example in blogPosts/components/BlogPostStateProvider.tsx.

In general, there will be one state-provider for each state in a module spec file. However, the module spec may specify additional state-providers that provide other types of state (not tied to a particular State object).

## The cache object

The StateProvider starts by creating a state object. Certain parts of this state object will be stored in a cache where they will be enriched by the updateSources function with a so-called resource state. This resource state reflects whether the resource is loading or updating. The updateSources function bases the resource state on a list of functions, where each function either contributes to the "loading" state or to the "updating" state.

If you have doubts about which provided fields should come from the cache object, then please ask me before generating the code.

## The combination of React Context and MobX

State is always stored in MobX observable objects. React Contexts are used to pass these MobX observable objects to consuming components.

### The context provider

The provided resources are places in an object with a get function for each resource.
The createGetProps function converts this object into a set of get-properties. The use of createGetProps is important as it allows us to pass an object with MobX-observable data to the context provider, without directly accessing this data in the StateProvider (as doing so would trigger re-renders).
