# Instructions for writing a form.ts file

When writing a form.ts file, please follow the example in blogPosts/components/BlogPostFormView/form.ts.

## The getInitialValues function

The getInitialValues function has two purposes. It allows to pass values from the props object to the form. It also declares which field-names are available in the form. Note that getInitialValues may initialize a form-field to null to declare a field-name that has no corresponding initial value.

## The getInitialErrors function

The getInitialErrors function allows to initialize the error strings from external errors stored in the props object.
