# Instructions for writing extensions.py files

When writing an extensions.py file, please follow the example in the blogs/backend/extensions.py file.

## Purpose of extensions.py

The purpose of the extensions.py file is to simulate the standard behaviour of a Django backend to provide related sets. For example, if a Blog has a foreign key to a User, then the User model is automatically extended with a blog_set member. The scenarios need to be able to access these related sets on the mock-units, so that they can simulate the behaviour of the real application. Therefore, the extensions.py dynamically extends the backend Model classes with fields for these related sets.
