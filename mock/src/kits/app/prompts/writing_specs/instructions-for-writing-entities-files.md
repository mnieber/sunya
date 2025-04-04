# Instructions for writing entities.py files

## Purpose

The entities.py file contains mock code-units that represent resources that are available in the
programming environment in which the application will run. For example, the programming environment
will provide programming constructs such as Function, Enum, List, etc. When we write a module spec,
and we declare that a CreateUser action function exists, then we can declare that CreateUser is a Function.

## Mock code-units in the module spec are different from those in the entities.py file

It's important to understand that the mock code-units in the module specs are different (in meaning) from
the mock code-units in the entities.py file. The former code-units are specific to the application. When
we implement the application, then we will have to provide a real implementation for these mock code-units.
The latter code-units are specific to the programming environment in which the application runs. For example,
if the application is running on Django, then the user-session is provided by Django. Therefore, we should
not include a UserSession type in our module-spec, but instead include it in the django_app/entities.py file.
