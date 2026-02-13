"""
Create a simple scenarios directory structure from the store.

This action reads the store contents and creates a simplified directory structure
that mirrors: store -> components -> scenarios -> scenario.markdown files.
"""

from pathlib import Path

from sunya.runtime.utils.get_logger import get_logger
from sunya.scenarios.models.store import get_store

logger = get_logger()


def create_simple_scenarios_dir(root_config_context):
    """
    Create a simple 'store' directory in the root config's output dir.

    The structure mirrors: store/{component_name}/scenarios/{scenario_name}.md

    Args:
        root_config_context: The root ConfigContext containing the output_dir
    """
    if not root_config_context.output_dir:
        logger.error("No output_dir specified in root config context")
        return

    # Get the store with all components and scenarios
    store = get_store()

    if not store.components:
        logger.warning(
            "No components found in store. Skipping simple scenarios dir creation."
        )
        return

    # Create the base 'store' directory
    store_dir = root_config_context.output_dir / "store"
    store_dir.mkdir(exist_ok=True, parents=True)

    logger.info(f"Creating simple scenarios directory at: {store_dir}")

    # Iterate through components and scenarios
    for component in store.components:
        if not component.scenarios:
            logger.debug(f"Component '{component.name}' has no scenarios, skipping.")
            continue

        # Create component directory
        component_dir = store_dir / component.name
        component_dir.mkdir(exist_ok=True, parents=True)

        # Create scenarios subdirectory
        scenarios_dir = component_dir / "scenarios"
        scenarios_dir.mkdir(exist_ok=True, parents=True)

        # Write each scenario markdown file
        for scenario in component.scenarios:
            if not scenario.markdown_fn:
                logger.warning(
                    f"Scenario '{scenario.name}' in component '{component.name}' "
                    f"has no markdown_fn. Skipping."
                )
                continue

            # Read the original markdown content
            original_path = Path(scenario.markdown_fn)
            if not original_path.exists():
                logger.warning(
                    f"Markdown file not found: {scenario.markdown_fn}. Skipping."
                )
                continue

            # Read content and write to simple structure
            content = original_path.read_text()
            output_path = scenarios_dir / f"{scenario.name}.md"
            output_path.write_text(content)

            logger.debug(
                f"Wrote scenario '{scenario.name}' to {output_path.relative_to(store_dir)}"
            )

    logger.info(
        f"✓ Created simple scenarios directory with "
        f"{len(store.components)} component(s) at {store_dir}"
    )
