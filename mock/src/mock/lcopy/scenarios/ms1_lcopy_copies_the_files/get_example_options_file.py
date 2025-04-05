example_options = """
# Configuration files to use (can list multiple)
configs:
  - mock/src/mock/blogs/blogs.lcopy-config.yaml
  - mock/src/mock/landler/landler.lcopy-config.yaml

# Destination directory for copied files
destination: ~/projects/sunya/res/claude/landler_be

# Labels to include (can list multiple)
labels:
  - use-scenarios
  - use-be-scenarios
  - generate-be

# Conflict resolution strategy (overwrite, skip, prompt)
conflict: overwrite

# Enable verbose output
verbose: true

# Purge files in destination that weren't copied
purge: true

# Enable dry run mode (no actual copying)
dry_run: false

# Enable default ignore patterns
default_ignore: true

# Extra ignore patterns
extra_ignore:
  - .foo
"""


def get_example_options_file():
    return example_options
