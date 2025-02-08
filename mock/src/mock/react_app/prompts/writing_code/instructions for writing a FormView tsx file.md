# Instructions for writing a FormView.tsx file

When writing a FormView.tsx file, please follow the example in blogPosts/components/BlogPostFormView/BlogPostFormView.tsx.

## Use of withContextProps

The withContextProps hoc extends the properties that are passed into the component with properties that come from a React context.

## FormFieldLabel buttons

In the example code, the usePreviewButton hook is called to create a button that is passed to a FormFieldLabel. The FormFieldLabel component can host buttons that will be shown to the far right of the label.

## Fields

The Field component is used to provide a fieldName (using a React context) to its wrapped components
