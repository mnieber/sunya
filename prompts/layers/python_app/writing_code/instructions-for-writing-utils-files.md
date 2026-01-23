# Instructions for writing utils files

When writing a utils file, please follow the example in `bookie/chapters/utils/strip_prefix.py`.

Util files live in the utils sub-directory. Typically, each util function lives in its own file within the utils directory.
The exception is when there are many small util functions that have a clear grouping criterion (e.g. small math functions),
these can go into a group utils file. When in doubt, please ask about creating a group file or a separate file.

## Rules are opinionated, utils are not

When a function is opiniated, such as the is_bad_word function, then it is located in the rules sub-package. However, when the function is free from business logic, such as strip_prefix, then it is located in the utils sub-package.
