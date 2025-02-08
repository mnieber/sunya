# Instructions for writing enums.py files

When writing a enums.py file, please follow the example in blogs/enums.py.

Note that the name of an enum is plural. This way, the singular version of the name can still be used for a regular Python class.

## How to determine which enums exist

The enum classes are not mentioned explicitly in the module specs. Instead, they are mentioned implicitly using the notation "Audiences: expert | novice | any". In the example file, the existence of a `Audiences` enum in `blogs/enums.py` is inferred.
