# Instructions for writing frontend module specs

Taking the roadmap.md file as input, your task is to identify which frontend module specification files (aka frontend module specs) are needed, and to generate these module specs.

When writing a frontend module spec, please follow the example in the frontend/modules/blogs.py file.

## Purpose of a frontend module spec

The purpose of a frontend module spec is similar to the purpose of the backend module spec, but aimed at the frontend. It declares mock code-units that can be used in frontend scenarios.

## Top-level module class

The top-level data-structure is a so-called module class that inherits from Module. It acts as a namespace for all mock code-units for a specific module.

### Types

The Types section of the module class describes the Typescript types that are based on the entities in the roadmap. Typically these Typescript types will be similar to the Django entities in the backend.

### Mutations

The Mutations section describes the mutations that the frontend can use. These mutations correspond to the api views in the backend that mutate data.

### Queries

The Queries section describes the queries that the frontend can use. These queries correspond to the api views in the backend that query data.

### States

The States section describes the state objects that are used in the frontend to store local state data. Typically, any server state (that is received through queries) and any local state that is shared between different components is stored in these state objects.

Every State object has one or more containers. Each container stores a particular resource and related meta-data. States can use the following facets:

- the data facet is used to store the resource data itself
- the addition facet allows components to add a new item
- the deletion facet allows components to delete the selected items
- the display facet offers a display-only list to components that shows users the future state of the resource (e.g. it shows the expected state when the dragAndDrop or addition facet have mutated the resource)
- the dragAndDrop facet allows components to set the drop location for a new item and to signal the drop of the item
- the edit facet allows components to toggle editing of the highlighted component, and to confirm/save the changes
- the filtering facet allows components to turn filtering on or off, and to set a filter
- the highlight facet allows components to get and set the highlighted item
- the insertion facet allows components to insert an item into the resource. Insertion usually works together with addition and dragAndDrop.
- the selection facet allows components to get and set the selection.

When you translate a milestone (from the roadmap) into a module spec, please reflect on which states, containers and facets will probably be needed. Feel free to make a guess, as I will be able to make corrections to the States section afterwards.

### Routes

The Routes section describes the routes that the frontend will render. Usually, a route corresponds to a particular page in the application.

### StateProviders

The StateProviders section describes the state-provider components that provide state to other components. For every State object in the States section, there will be a corresponding StateProvider. However, if you conclude - based on the roadmap - that a different type of shared state must be provided to the components then feel free to insert an extra state-provider in this section.

### Views

The Views section describes components that can be considered Views. A View component typically shows a resource. Each view in the Views section can have a Root class that contains a high-level description of the layout of that view. The Root class corresponds to the root div of the view.

There are two ways to specify views and components. They may be listed explicitly in the Views section or Components section, or they may be specified implicitly by their appearence within the Root class of some other View, or both of the above.

Elements in the Root class that start with a double underscore denote divs that are embedded in the root div.

#### View layouts

When I ask you to write a frontend module spec I will usually also supply information (both in text and in images) about the layout of the views that the user is interacting with. This information can then be used to fill the Root class of the view. Since there is no right or wrong way to fill the Root class, just make a best effort on filling out this part of the spec, and take on the role of a UX designer who is free to imagine what a good layout might be.

### Effects

The Effects section describes so-called url-effects. Usually when a State is provided that has a highlight facet then the highlighted item should be synchronized with the url. The SelectEffect (which is a type of url-effect) takes care of this.

### Components

The Components section describes the components that are used in the various views of the Views section. If a component should be stylable from the outside (i.e. by the View that uses it) then it will have a trim property.
