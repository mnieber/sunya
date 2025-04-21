def get_example_config_file():
    example_config_file = """
sources:
  ../app: app
  ../music: music-collection

options:
  # Destination directory for copied files
  destination: ~/projects/sunya/res/claude/landler_be

  # Concatenated output filename (optional)
  concatenated_output_filename: ~/projects/combined_output.txt

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
    - .tmp

  # Labels to include by default
  labels:
    - organize-dinner-party
    - music-friends

targets:
  organize-dinner-party:
    files:
      instructions:
        recipes:
          "recipes/soups": true
          "recipes/salads/green-salad.md": true
        music:
          jazz:
            "music/jazz/*.md": true
          rock:
            (music/rock/<album-name>/songs):
              "track-*.md": true
              "greatest-hits-of-me.md": false
    include:
      - app.documentation
      - music-collection.playlists

  music-friends:
    files:
      playlists:
        "playlists/*.md": true
        "playlists/private": false
      favorites:
        "favorites/*.txt": true
"""
    return example_config_file
