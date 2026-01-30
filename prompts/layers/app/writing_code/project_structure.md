# Project description

The software development process contains three steps:

1. first, we create a roadmap
2. from this roadmap, we create a technical specification in the extra/spec_src directory
3. finally, from the technical specification, we create software

When I ask for your help, it will be either with writing the spec_src files based on a roadmap in `extra/spec_src/roadmaps`, or with generating the real app from the spec_src files. However, I will never ask you to help with both steps at the same time (the steps are strictly separate).

Note that in a practical application, the spec_src files are compiled into markdown files in the doc/spec directory. However, to keep it simple, we are leaving this step outside of our consideration and only focus on the spec_src files.

## Example roadmap

Please use the bookie roadmap in `extra/spec_src/roadmaps/roadmap.md` as an example of how roadmaps are structured.

## The use of an example application

The rest of the software development process will be explained using the bookie example application.

## The use of research/plan/implement for refactoring and feature implementation

When we are refactoring the existing code or implementing features, I will often ask you to create a research.md document that describes how the current feature works. Afterwards, I will ask you to create a plan.md file that describes the refactoring plan.

RULE: When I ask you to write a plan.md document, then this plan should be based on the research.md document.
