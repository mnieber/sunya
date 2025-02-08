/* eslint-disable */
/**
 * Configuration file for VS Code Vandelay extension.
 * https://github.com/ericbiewener/vscode-vandelay#configuration
 *
 * To install:
 * 1. Install the Vandelay extension in VS Code
 * 2. Use File -> Add Folder to Workspace to add the .vandelay folder to the workspace
 * 3. In your shell, create the LANDLER_PLATFORM_DIR environment variable and set it to the
 *    absolute path of the platform directory (without trailing slash).
 * 4. Save the current file (the file you are currently reading). You should see a message
 *    saying "Project exports have been cached".
 * 5. Press CTRL+K+S to create a new keyboard shortcut for "Import Active Word".
 * 6. Put the cursor on a word and press the keyboard shortcut to import it.
 */

const baseDir = "/home/maarten/projects/sunya/src/mock/src";

module.exports = {
  // This is the only required property. At least one path must be included.
  includePaths: [baseDir],
  processImportPath: (
    importPath,
    absImportPath,
    activeFilepath,
    projectRoot
  ) =>
    absImportPath.startsWith(projectRoot)
      ? absImportPath
          .slice(baseDir.length)
          .replace(/\.[^/.]+$/, "")
          .replaceAll("/", ".")
      : null,
};
