import os
import time
from pathlib import Path

from sunya.render.actions.render_specs import render_specs
from sunya.render.utils.get_scenario_watch_dirs import is_scenario_spec_path
from sunya.utils.get_logger import get_logger
from watchdog.events import FileSystemEventHandler

logger = get_logger()


class SpecFileChangeHandler(FileSystemEventHandler):
    """Handler for spec file changes that triggers re-rendering."""

    def __init__(self, config_contexts, create_simple_output_dir):
        """
        Initialize handler for multiple configs.
        """
        self.config_contexts = config_contexts
        self.create_simple_output_dir = create_simple_output_dir
        self.last_render_time = 0
        self.debounce_seconds = 1  # Debounce to avoid multiple rapid re-renders

    def should_process_event(self, event):
        """Check if the event should trigger a re-render."""
        if event.is_directory:
            return False

        paths = [event.src_path]
        if getattr(event, "dest_path", None):
            paths.append(event.dest_path)

        # Check if a changed file is a (new, existing or removed) scenario file
        if not any(self._is_scenario_file(path) for path in paths):
            return False

        # Debounce: avoid processing events that are too close together
        current_time = time.time()
        if current_time - self.last_render_time < self.debounce_seconds:
            return False

        return True

    def on_modified(self, event):
        """Handle file modification events."""
        if not self.should_process_event(event):
            return

        self._render()

    def on_created(self, event):
        """Handle file creation events."""
        if not self.should_process_event(event):
            return

        self._render()

    def on_deleted(self, event):
        """Handle file deletion events."""
        if not self.should_process_event(event):
            return

        self._render()

    def on_moved(self, event):
        """Handle file move events (e.g. editors that save via a rename)."""
        if not self.should_process_event(event):
            return

        self._render()

    def _is_scenario_file(self, path):
        path = os.fsdecode(path)
        if not path.endswith(".py"):
            return False

        for ctx in self.config_contexts:
            # A file that was rendered before (it may have been removed since)
            if Path(path).resolve() in ctx.watch_paths:
                return True
            # A file that matches a scenario pattern (it may be new)
            package_config_by_name = ctx.config_dict.get("package_config_by_name") or {}
            for package_config in package_config_by_name.values():
                patterns = package_config.get("scenario_paths", [])
                if is_scenario_spec_path(ctx.root_dir, patterns, path):
                    return True
        return False

    def _render(self):
        """Re-render all specs from all configs."""
        self.last_render_time = time.time()
        logger.info("Change detected, re-rendering all configs...")

        # Track which configs we're re-rendering
        config_paths = [str(ctx.config_path) for ctx in self.config_contexts]
        logger.info(f"Re-rendering {len(config_paths)} config(s):")
        for config_path in config_paths:
            logger.info(f"  - {config_path}")

        try:
            count = render_specs(
                self.config_contexts,
                reset_store=True,
                create_simple_output_dir=self.create_simple_output_dir,
            )
            logger.info(f"✓ Successfully re-rendered {count} config(s)")
        except Exception as e:
            logger.exception(f"Error re-rendering: {e}")
