# Background

To produce facts during an assessment, we run geomodels that receive their inputs in a dictionary object.

# Problem statement

When refactoring the geomodels, we may introduce errors that affect the geomodel output numbers. We want to catch these errors early.

# Solution

## Add a tlg_geomodel_testing library

The below proposals require new shared library code that will live in the tlg_geomodel_testing library.

## Each geomodel defines regression-testing selector functions

A selector function selects input/output examples for the purpose of regression testing. E.g. the selector function can check whether cover-crops were used in the last year. Each selector function can be annotated with the number of examples that should be collected.

## Each geomodel automatically collects input/output pairs

Collection happens when the geomodel runs. The geomodel checks whether some selector functions have not yet collected all their input/output pairs. In that case, if the current model input meets the selector function criteria, the input/output pair is added to an S3 bucket (labelled with the name of the selector function).

## Geomodels can run regression tests

Every geomodel has an extra entry point to run the smoke test. This entry point:

- downloads the input/output pairs from S3.
- runs the geomodel on the input and compares the result to the expected output
- produces an html report that shows a diff
  - we can use difflib

## Geomodels can invalidate the input/output pairs

If the geomodel has changed for good reasons, then the user can run a command on the command-line to recompute all outputs, or remove all input/output pairs.

## Github runs the regression test

Github will also run the regression test in CI, either after each commit or after merging to main (to be decided).
