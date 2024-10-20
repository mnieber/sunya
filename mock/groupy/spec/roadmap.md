# Goal

The goal of Groupy is to analyze a Python package and identify three types of funtions:
main functions, helper functions and utility functions.
Groupy will create a refactoring plan for moving each main function into its own file,
together with its helper functions.

## Main functions

These are functions that address a high-level concern. Main functions may call other main functions,
helper functions and utility functions.

## Helper functions

A helper function is a function that is used by one (and only one) main function. A helper function
may call utility functions, but it may not call main functions or other helper functions.

## Utility functions

Utility functions are simple generic functions. Utility functions may call other utility functions,
but not main functions or helper functions.

# Milestones

## MS1: Groupy analyzes a Python package

1. Groupy creates a tree structure that contains all directories and files.
2. The tree has directory nodes and file nodes that reflect the file-system
3. Every file-node contains a symbol list
   1. Every symbol in the list has a "##.#" prefix
      1. The prefix has two digits and a character (M, H, U, C), separated by a dot
   2. The character indicates the type of function
      1. The `M.##` prefix indicates a main function
      2. The `H.##` prefix indicates a helper function
      3. The `U.##` prefix indicates a utility function
      4. The `C.##` prefix indicates a constant
         1. Constants have to be all caps or Groupy will throw an error
   3. The digits indicate the number of callers (function that call this function)
   4. Every function in the list may have a suffix that is a colon plus a path
      1. This path points to the target location and symbol-name for this symbol
   5. Consider some examples:
      1. `- H.my_helper_function: my_foo_function`
         1. This indicates that this helper function must be renamed to my_foo_function
         2. The value in the suffix cannot have a path
            1. This is because the target path is determined by the main function that calls this helper function
      2. `- M.my_main_function: one.three.my_main_function`
         1. This indicates that this main function must be renamed to my_main_function
         2. Moreover, the new location of this function must be `one.three`
4. In the previous step, Groupy automatically assigned the prefixes for M and H.
   1. If a function is only called by one caller function then it receives the `H.` prefix
      1. Otherwise, it receives the `M.` prefix
   2. Groupy doesn't assign the `U.` prefix since it cannot distinguish between a main function and a utility function.
      1. However, the user will be able to correct this by assigning the `U.` to the appropriate functions.
5. Groupy writes the tree structure to a tree.yaml file
   1. The user can make corrections by editing the tree.yaml file
6. In case of errors, Groupy always prints an error message to the screen and then exits

## MS2: Groupy refactors a Python package

1. The user edits the tree.yaml file to make corrections
2. Based on the tree.yaml file, Groupy creates new files and edits existing files
   1. Helper functions are automatically moved to live in the file that contains their related main function
   2. Moreover, helper functions are automatically renamed to have an underscore as their prefix
   3. When a function is moved to a new file, then all imports from the source file are also copied to the target file
   4. Note that constants may also be moved to new locations as indicated by the tree.yaml refactoring plan
   5. When a moved function depends on symbols in the source file, then extra imports for these symbols are added to the target file.
3. Note that the copying of all import statements from the source file may easily lead to spurious imports in the target file.
   1. Therefore, the spurious imports in the target file are removed by calling `isort --fix` on that file.
   2. Moreover, spurious imports in the source file are also removed by calling `isort --fix` on that file.
4. It might happen that the renamings in the refactoring plan lead to naming conflicts
   1. In that case Groupy should stop with an error message
5. It might also happen that circular dependencies are introduced by moving functions to new locations
   1. Groupy will ignore this problem and leave it to the user to address them
6. The moving of functions to new locations will break the existing imports of those functions
   1. Groupy will not try to fix these errors but it will print a list of filenames with broken imports
      1. The user will manually fix these files
7. The moving of functions to new locations may introduce missing imports in the source file
   1. This only happens if other functions in the source file were calling the moved function
      1. In that case, Groupy will also mention the source file its list of files with broken imports
