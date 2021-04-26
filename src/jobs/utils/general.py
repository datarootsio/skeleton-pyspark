import argparse
from pathlib import Path


def get_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Parse the arguments that are passed to the run.py file."
    )
    parser.add_argument("-v", "--verbose", action="store_true", required=False)
    parser.add_argument("--version", action="store_true", required=False)
    parser.add_argument(
        "-e", "--env", choices=["dev", "prod", "stage"], action="store", required=True
    )
    parser.add_argument(
        "-f",
        "--file-path",
        action="store",
        required=False,
        default=f"file://{Path(__file__).parents[3]}/LICENSE",
    )
    return parser
