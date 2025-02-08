# Goal

I've uploaded some spec files for the tlg_regression_testing library that I want to create. I would like you to assist me in the writing the code. The spec files consist of module specs (please create a package for every such module) and scenario specs. Scenarios explain the features of the library by presenting them as a workflow.

# Packages

Please create a package directory for each module spec (e.g. there would be an io package).

# Actions

An action is a state-changing function that lives in the actions sub-directory of a module package.

# Models

A model is a dataclass that is based on the dataclassy package from pypi. All models are placed in the models.py file inside of a module package.

# Testing

Please use pytest when generating the test-code.

# Error handling

If a function encounters an error then it should raise a dedicated exception class such as "CannotOpenS3Bucket". The entry-point should catch all exceptions and print a related message on the console.

# Dependencies

Don't worry about them, I will manage them myself. Feel free to use whatever pypi package you find appropriate, such as difflib.

# Documentation

Please be minimalistic. Only add some inline comments if the reader would otherwise not be able to follow what's happening.

# Versioning

Don't worry about this, I will manage it myself.
