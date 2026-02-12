import time
import logging
from watchdog.events import FileSystemEventHandler
from sunya.runtime.actions.process_packages import process_packages

logger = logging.getLogger(__name__)


class SpecFileChangeHandler(FileSystemEventHandler):
    """Handler for spec file changes that triggers re-rendering."""

    def __init__(self, config_contexts, verbose=False):
        """
        Initialize handler for multiple configs.

        Args:
            config_contexts: List of ConfigContext objects to re-render
            verbose: Whether to enable verbose logging
        """
        self.config_contexts = config_contexts
        self.verbose = verbose
        self.last_render_time = 0
        self.debounce_seconds = 1  # Debounce to avoid multiple rapid re-renders

    def should_process_event(self, event):
        """Check if the event should trigger a re-render."""
        if event.is_directory:
            return False

        # Check if the changed file is a Python file
        if not event.src_path.endswith(".py"):
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

        self.render_specs()

    def on_created(self, event):
        """Handle file creation events."""
        if not self.should_process_event(event):
            return

        self.render_specs()

    def render_specs(self):
        """Re-render all specs from all configs."""
        self.last_render_time = time.time()
        logger.info("Change detected, re-rendering all configs...")

        # Track which configs we're re-rendering
        config_paths = [str(ctx.config_path) for ctx in self.config_contexts]
        logger.info(f"Re-rendering {len(config_paths)} config(s):")
        for config_path in config_paths:
            logger.info(f"  - {config_path}")

        success_count = 0
        error_count = 0

        for ctx in self.config_contexts:
            try:
                if "spec_paths_by_package" in ctx.config_dict:
                    process_packages(ctx, self.verbose)
                    success_count += 1
            except Exception as e:
                logger.error(f"Error re-rendering {ctx.config_path}: {e}")
                error_count += 1

        if error_count == 0:
            logger.info(f"✓ Successfully re-rendered {success_count} config(s)")
        else:
            logger.info(
                f"Re-rendering completed with {success_count} success(es) and {error_count} error(s)"
            )
