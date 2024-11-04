import json

from groupy.create_refactoring_plan import create_refactoring_plan
from groupy.models.json_encoder import JSONEncoder
from groupy.scan_package import scan_package


def main(package_path: str):
    tree_structure = scan_package(package_path)
    refactoring_plan = create_refactoring_plan(tree_structure)
    print(json.dumps(refactoring_plan, indent=2, cls=JSONEncoder))


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <package_path>")
        sys.exit(1)

    package_path = sys.argv[1]
    main(package_path)
