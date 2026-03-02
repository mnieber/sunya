# Instructions for writing settings files

As shown by the `bookie/settings.py` example, the settings for the application are collected into this global file.

The settings.py file is a central file that contains the settings for the Python app.
Usually, each setting is derived from an environment variable. The application should not read
environment variables outside of the settings.py file, so that it's easy to inspect the environment
variables that the application depends on.

## RULE: Settings are collected into the settings.py at the application package root

Each module's Settings section (declared implicitly in the scenario specs, e.g. `m.Books.Settings.MAX_CHAPTERS_PER_BOOK`) describes the settings and environment variables that the module depends on. However, as shown in `bookie/settings.py`, the settings.py file is not located at the module level but at the root level of the application.
