# Module declarations

The modules of a react app are declared implicitly in scenario specs. For example, the types section is declared implicitly in scenario specs by referencing `m.<Module>.Types.<TypeName>`.
This section describes the Typescript types that are based on the entities in the roadmap. In general, you will be able to guess the purpose of each section by looking at the section name, and by inspecting the blogs_fe example. This example contains scenarios that implicitly define sections, and also contains the actual React code that implements these sections.

## Types

Most of the type-script types are declared in the api module. The reason is that types often cut across the feature modules. Therefore, it's convenient to not tie them to a specific feature module but put them in a central location.

## Mutations

The Mutations section describes the mutations that the frontend can use. These mutations correspond to the api views in the backend that mutate data.

## Queries

The Queries section describes the queries that the frontend can use. These queries correspond to the api views in the backend that query data.

## States

The States section describes the state objects that are used in the frontend to store local state data. Typically, any server state (that is received through queries) and any local state that is shared between different ui components is stored in these state objects.

Every State object has one or more containers. Each container stores a particular resource and related meta-data. States can use the following facets:

- the data facet is used to store the resource data itself
- the addition facet allows ui components to add a new item
- the deletion facet allows ui components to delete the selected items
- the display facet offers a display-only list to ui components that shows users the future state of the resource (e.g. it shows the expected state when the dragAndDrop or addition facet have mutated the resource)
- the dragAndDrop facet allows ui components to set the drop location for a new item and to signal the drop of the item
- the edit facet allows ui components to toggle editing of the highlighted component, and to confirm/save the changes
- the filtering facet allows ui components to turn filtering on or off, and to set a filter
- the highlight facet allows ui components to get and set the highlighted item
- the insertion facet allows ui components to insert an item into the resource. Insertion usually works together with addition and dragAndDrop.
- the selection facet allows ui components to get and set the selection.

## Routes

The Routes section describes the routes that the frontend will render. Usually, a route corresponds to a particular page in the application.

## StateProviders

The StateProviders section describes the state-provider components that provide state to other components. For every State object in the States section, there will be a corresponding StateProvider. However, sometime additional state providers are described that provide an extra state that is not described in the States section.

## Views

The Views section describes components that can be considered Views. A View component typically shows a resource.

Each view in the Views section can have a root field that contains a high-level description of the layout of that view. The root field corresponds to the root div of the view. Elements in the root field that start with a double underscore denote divs that are embedded in the root div. The names of these div elements suggest a particular layout for the view.

## Effects

The Effects section describes so-called url-effects. Usually when a State is provided that has a highlight facet then the highlighted item should be synchronized with the url. The SelectEffect (which is a type of url-effect) takes care of this.

## Components

The Components section describes the ui components that are used in the various views of the Views section. If a component should be stylable from the outside (i.e. by the View that uses it) then it will have a trim property.
