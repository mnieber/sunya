# Instructions for writing a storybook tsx file

When writing a storybook file, please follow the example in stories/BlogListView.stories.tsx.

We'll need a story for every standalone View (in the Views section of the module spec) or reusable component (in the Components section of the module spec).

With standalone I mean that the view does not exist merely as a building block for some bigger view. For example, a ListViewItem component is not standalone, because it is only used as a building block for a particular ListView component. On the other hand, a ListView component is typically reusable in various places, and should be considered a standalone component.

With a reusable component I mean a component that is not merely used as a widget in one particular view (that already shows that component in its storybook page) but is reusable in various views.

When in doubt whether a view or component should have a storybook page, please ask.

Please determine which StateProviders should wrapped the component in the storybook file. Try to include only those StateProviders that are needed by the component. Stories should get their data from mocks provided by the msw framework.
