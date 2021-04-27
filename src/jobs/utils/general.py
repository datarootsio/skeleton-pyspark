"""General utilities around the ETL job."""
import argparse
from pathlib import Path
from enum import Enum


def get_argument_parser() -> argparse.ArgumentParser:
    """
    Argument parse using argparse for the run.py file.

    Returns (argparse.ArgumentParser): arg parser options

    """
    parser = argparse.ArgumentParser(
        description="Parse the arguments that are passed to the run.py file."
    )
    parser.add_argument("-v", "--verbose", action="store_true", required=False)
    parser.add_argument("--version", action="store_true", required=False)
    parser.add_argument(
        "-e",
        "--env",
        type=EnvEnum,
        choices=list(EnvEnum),
        action="store",
        required=True,
    )
    parser.add_argument(
        "-f",
        "--file-path",
        action="store",
        required=False,
        default=f"file://{Path(__file__).parents[3]}/LICENSE",
    )
    return parser


class EnvEnum(Enum):
    """Maintain the enums of the environments."""

    dev = "dev"
    prod = "prod"
    stage = "stage"

    def __str__(self: "Enum") -> str:
        """
        Modification needed for String Enum to work with argparse.

        Returns:
            str, value of string at Enum

        """
        return self.value
