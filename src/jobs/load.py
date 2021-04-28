"""This module is responsible for transform (L) in ETL."""
from pathlib import Path

from pyspark.sql import DataFrame


def write_to_path(df: DataFrame, path_to_write: str = None) -> None:
    """
    Write the dataframe to a local location.

    Args:
        df (DataFrame): dataframe to be written
        path_to_write (str): path for csv file to write the file at

    """
    if path_to_write is None:
        path_to_write = f"file://{Path(__file__).parents[2]}/counted_file.csv"
    (df.coalesce(1).write.mode("overwrite").csv(path_to_write))
