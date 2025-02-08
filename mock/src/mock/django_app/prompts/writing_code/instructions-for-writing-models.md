# Instructions for writing models.py files

When writing a models.py file, please follow the example in blogs/models.py.

Note that SingleLineTextField is used for model fields that contain short strings, such as the name field. A SingleLineTextField inherits from TextField, but it's shown as a single line text input in the Django admin.

## Location of enums

Note that whenever an enum class is inferred from the module spec file, the enum should (in most cases) be used in the models.py file but it will be defined in the enums.py file. The sample code shows this, since Audiences is used in blogs/models.py but it's defined in blogs/enums.py.
