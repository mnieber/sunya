# Instructions for writing App.tsx

When writing a App.tsx file, please follow the example in app/components/App.tsx. The sample code for the layout.ts file is provded in frames/layout.ts.

## Providers

In general, try to place the providers high up enough in the tree so that they wrap the components that need the provided resources. For example, all components need the AuthState so therefore the AuthStateProvider is high up in the tree. At the same time, try to limit the scope of providers to the components that actually use the provided resources. For example, the BlogsStateProvider only wraps the components that need the BlogsState.

In general, don't worry too much about getting this right, it's not so important, and I can easily correct this myself.

## Switches

Switches are used to pack a group of routes into a single object to not bloat the size of the App component.

## The layout object (L)

The layout object (L) is used throughout the code to make the used layouts easier to recognize. The layouts it offers are shown in frames/layout.ts.

## Terminology: elements and components

With component we mean a React component. With element we mean a DOM element such as a div. Since most React components have an outer div, we sometimes use element to mean either a component or a DOM element.

## The use of scss files

The code should make a general distinction between so-called intrinsic styles and ad-hoc styles. The intrinsic styles are the styles that are not context-dependent. This makes them pretty boring, and for that reason they are placed in an scss file where they do not clutter the code. The ad-hoc styles are the context-dependent styles.

The distinction between intrinsic styles and ad-hoc styles is quite subjective, but there are patterns:

- margins are always considered ad-hoc, because they are outside of the boundaries of the element itself.
- background-color is ad-hoc when users of the element will have their own preference for what the color should be. For example, a card element may be used in various places with different background-colors. In that case, it's possible that the background-color comes from a so-called style-object, which is basically menu of style-choices from which the users of an element can choose to style the element.
- background-color is intrinsic when the element should always have the same background-color. There is no objective rule for deciding if a style property is intrinsic or ad-hoc, please use your own judgement and inspect the code samples to get a feeling for this.

Finally, note that although intrinsic style properties are usually put in the scss file, they are sometimes inlined in the element. This is done when it's important or interesting to know that this style property is uesd. In general, the boring style properties should go into the scss file, and the interesting ones should be inlined in the element.
