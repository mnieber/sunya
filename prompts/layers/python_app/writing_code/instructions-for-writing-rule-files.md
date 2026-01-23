# Instructions for writing rule files

When writing a rule file, please follow the example in `bookie/chapters/rules/is_bad_word.py`.

Rule files live in the rules sub-directory. An rule is a function that retrieves information (from the application state, or otherwise) subject to business logic.
Sometimes rules and utils look similar. Functions that involve business logic are usually rules, and functions that are unopiniated are usually utils.
