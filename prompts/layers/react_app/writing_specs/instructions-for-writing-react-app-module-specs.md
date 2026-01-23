# Instructions for writing frontend module specs

Taking the roadmap.md file as input, your task is to identify which frontend module specification files (aka frontend module specs) are needed, and to generate these module specs. The process is quite similar to the process of writing backend module specs, though the sections of the modules are different, as detailed below.

When writing a frontend module spec, please follow the example in the blogs/frontend/modules/blogs.py file.

### States

When you translate a milestone (from the roadmap) into a module spec, please reflect on which states, containers and facets will probably be needed. Feel free to make a guess, as I will be able to make corrections to the States section afterwards.

### StateProviders

If you conclude - based on the roadmap - that an extra state (that is not included in the States section) must be provided to the ui components then feel free to insert an extra state-provider in this section.

### Views

As mentioned elsewhere, each view in the Views section can have a root field that contains a high-level description of the layout of that view. There is no right or wrong way to fill the root field, just make a best effort on filling out this part of the spec, and take on the role of a UX designer who is free to imagine what a good layout might be.
