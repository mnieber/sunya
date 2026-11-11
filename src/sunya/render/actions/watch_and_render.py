import time

from sunya.render.utils.get_scenario_watch_dirs import (
    get_scenario_watch_dirs,
    remove_nested_dirs,
)
from sunya.render.utils.spec_file_change_handler import SpecFileChangeHandler
from sunya.utils.get_logger import get_logger
from watchdog.observers import Observer
from watchdog.observers.polling import PollingObserver

logger = get_logger()


def watch_and_render(config_contexts, *, create_simple_output_dir, poll_interval=None):
    """Re-render the specs of all configs whenever a scenario file changes.

    Watches the directories of the scenario patterns (recursively), so that new
    scenario files are picked up too. Blocks until interrupted with Ctrl+C.
    """
    print("Watch mode enabled. Monitoring spec files for changes...")
    logger.info("Watch mode enabled. Monitoring spec files for changes...")

    # Use polling observer if poll_interval is set, otherwise use native observer
    if poll_interval:
        logger.info(
            f"Using polling mode with {poll_interval}s interval (recommended for Docker)"
        )
        observer = PollingObserver(timeout=poll_interval)
    else:
        logger.info("Using native file system events (may not work in Docker)")
        observer = Observer()

    logger.info("Press Ctrl+C to stop watching.")

    event_handler = SpecFileChangeHandler(
        config_contexts, create_simple_output_dir=create_simple_output_dir
    )

    for watch_dir in sorted(_get_watch_dirs(config_contexts)):
        logger.info(f"Watching directory: {watch_dir}")
        observer.schedule(event_handler, str(watch_dir), recursive=True)

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("\nStopping watch mode...")
        observer.stop()
    observer.join()


def _get_watch_dirs(config_contexts):
    watch_dirs = set()
    for ctx in config_contexts:
        package_config_by_name = ctx.config_dict.get("package_config_by_name") or {}
        for package_config in package_config_by_name.values():
            watch_dirs.update(
                get_scenario_watch_dirs(
                    ctx.root_dir, package_config.get("scenario_paths", [])
                )
            )
    return remove_nested_dirs(watch_dirs)
