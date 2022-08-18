import argparse
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
sys.path.append(current_dir.as_posix() + "/../")

from cocoa import Analyzer


def make_parse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--filename",
        default="../assets/annotations/instances_val2017.json",
        type=str,
        help="plese set annotation file",
    )

    return parser.parse_args()


def main():
    args = make_parse()

    analyzer = Analyzer(filename=args.filename)
    print(analyzer.categories)


if __name__ == "__main__":
    main()
