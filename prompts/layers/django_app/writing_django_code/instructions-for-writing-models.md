# Instructions for writing models.py files

When writing a models.py file, please follow blogs/models.py of the blogs_be example.

Note that SingleLineTextField is used for model fields that contain short strings, such as the name field. A SingleLineTextField inherits from TextField, but it's shown as a single line text input in the Django admin.
