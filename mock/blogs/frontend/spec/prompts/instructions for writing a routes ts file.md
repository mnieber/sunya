# Instructions for writing a routes.ts file

When writing a routes.ts file, please follow the example in blogs/routes.ts.

## The Nav class

The Nav class has two purposes:

- it defines the module's routing interface as a set of routing functions
- it implements this routing interface by letting each function delegate the work to the global navHandler object.

Note that although the Nav class delegates the work to the global navHandler object, this doesn't mean that the route functions are actually implemented yet. The global navHandler object will search in its set of installed navigation-handler objects for a navigation-handler that can resolve the route.

## The DefaultNav class

The sample code also shows a DefaultBlogsNavHandler that defines the same routing functions as the Nav class does. The application will call navHandler.installDefaultNavHandler(new DefaultBlogsNavHandler()) to install this DefaultNav class into the global navHandler object.

When a View component calls navTo(blogsNav.blogList()) then the global navHandler instance will be invoked to find the blogList url, and unless some more specialized Nav class was installed, it will resolve this url from the DefaultBlogsNavHandler instance.

## Relation to the module spec

The routes that the user can navigate to are described in the Routes section of the module spec.
