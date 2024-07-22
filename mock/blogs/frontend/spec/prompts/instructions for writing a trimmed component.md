# Instructions for writing a trimmed component

When writing a trimmed component, please follow the example in frames/components/DialogButton/DialogButton.tsx.

## The trim.ts file

This file declares the trim-format (in the example source code this is DialogButtonTrimT) that can be used to style the associated component. The file also declares a style object (in the example source code this is DialogButtonTrimS) that can be used to fill the slots of the trim-object.

## The trims.ts file

The trims.ts file defines a set of pre-made trim objects based on the trim that is declared in trim.ts.
