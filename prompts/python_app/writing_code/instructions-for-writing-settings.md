# Instructions for writing settings files

The settings.py file is a central file that contains the settings for the Python app.
Usually, each setting is derived from an environment variable. The application should not read
environment variables outside of the settings.py file, so that it's easy to inspect the environment
variables that the application depends on.

Note that each module spec may have an Settings section that describes the settings and environment
variables that the module depends on. However, the settings.py file is not located at the module level
but at the root level of the application.
