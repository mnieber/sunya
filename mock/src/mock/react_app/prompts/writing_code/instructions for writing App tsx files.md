# Instructions for writing App.tsx

When writing a App.tsx file, please follow the example in app/components/App.tsx.

## Providers

In general, try to place the providers high up enough in the tree so that they wrap the components that need the provided resources. For example, all components need the AuthState so therefore the AuthStateProvider is high up in the tree. At the same time, try to limit the scope of providers to the components that actually use the provided resources. For example, the BlogsStateProvider only wraps the components that need the BlogsState.

In general, don't worry too much about getting this right, it's not so important, and I can easily correct this myself.

## Switches

Switches are used to pack a group of routes into a single object to not bloat the size of the App component.
