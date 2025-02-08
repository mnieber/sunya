from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--module")
    parser.add_argument("--scenario")
    parser.add_argument("--all", action="store_true")

    return parser.parse_args()
