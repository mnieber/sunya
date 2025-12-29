from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--module")

    return parser.parse_args()
