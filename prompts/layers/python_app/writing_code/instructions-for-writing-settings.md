# Instructions for writing settings files

As shown by the `bookie/settings.py` example, the settings defined in `extra/spec_src/modules/books.py` and `extra/spec_src/modules/chapters.py` are added to this global file.

The settings.py file is a central file that contains the settings for the Python app.
Usually, each setting is derived from an environment variable. The application should not read
environment variables outside of the settings.py file, so that it's easy to inspect the environment
variables that the application depends on.

## RULE: Settings are collected into the settings.py at the application package root

Note that each module spec, such as `bookie/modules/books.py` in spec_src, may have an Settings section that describes the settings and environment variables that the module depends on. However, as shown in `bookie/settings.py`, the settings.py file is not located at the module level but at the root level of the application.
