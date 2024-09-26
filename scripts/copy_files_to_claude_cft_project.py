import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

import sync_files_to_local_claude_dir

in_cft = "/home/maarten/projects/landler/src/platform/geographic_models/models/coolfarmtool-co2"
in_cft_lib = f"{in_cft}/src/coolfarmtool_co2"
in_backend = "/home/maarten/projects/landler/src/platform/backend"


dir_list = [
    "geomodel/coolfarmtool_co2/cropland",
    "geomodel/coolfarmtool_co2/organic_carbon_stock",
    "geomodel/coolfarmtool_co2/organic_carbon_stock_forecast",
    "geomodel/coolfarmtool_co2/organic_carbon_stock_benchmark",
    "geomodel/tests",
    "geomodel/generated_docs",
    "interface",
]

file_map = {
    f"{in_backend}/calculations/lib/coolfarmtool_co2.py": "interface",
    f"{in_cft_lib}/args_helpers.py": "geomodel/coolfarmtool_co2",
    f"{in_cft_lib}/args.py": "geomodel/coolfarmtool_co2",
    f"{in_cft_lib}/conversions.py": "geomodel/coolfarmtool_co2",
    f"{in_cft_lib}/cool_farm_tool.py": "geomodel/coolfarmtool_co2",
    f"{in_cft_lib}/cropland/carbon_changes.py": "geomodel/coolfarmtool_co2/cropland",
    f"{in_cft_lib}/cropland/model_parameters.py": "geomodel/coolfarmtool_co2/cropland",
    f"{in_cft_lib}/organic_carbon_stock/model_parameters.py": "geomodel/coolfarmtool_co2/organic_carbon_stock",
    f"{in_cft_lib}/organic_carbon_stock_benchmark/__init__.py": "geomodel/coolfarmtool_co2/organic_carbon_stock_benchmark",
    f"{in_cft_lib}/organic_carbon_stock_forecast/forecast.py": "geomodel/coolfarmtool_co2/organic_carbon_stock_forecast",
    f"{in_cft_lib}/organic_carbon_stock_forecast/__init__.py": "geomodel/coolfarmtool_co2/organic_carbon_stock_forecast",
    f"{in_cft_lib}/enums.py": "geomodel/coolfarmtool_co2",
    f"{in_cft_lib}/model.py": "geomodel/coolfarmtool_co2",
    f"{in_cft_lib}/types.py": "geomodel/coolfarmtool_co2",
    f"{in_cft}/tests/*.py": "geomodel/tests",
    f"{in_cft}/generated_docs/*.md": "geomodel/generated_docs",
    f"{in_cft}/interface.py": "geomodel",
}


if __name__ == "__main__":
    args = sync_files_to_local_claude_dir.parse_args()
    files_copied = sync_files_to_local_claude_dir.sync_files(
        file_map, dir_list, args.target_dir
    )

    if args.verbose:
        print(f"Synced {len(files_copied)} files.")
