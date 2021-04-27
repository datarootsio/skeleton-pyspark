"""This module is the entry-point for the run.py to handle spark session \
building and ETL."""

import contextlib
from argparse import Namespace
from pyspark.sql import SparkSession
from pathlib import Path
from typing import Generator

from src.jobs import extract, transform, load


def main(spark: SparkSession, file_path: str) -> None:
    """
    High-level function to perform the ETL job.

    Args:
        spark (SparkSession) : spark session to perform ETL job
        file_path (str): path on which the job will be performed

    """
    df = extract.extract_file(spark, file_path)
    count_df = transform.transform_df(df)
    load.write_to_path(count_df)


@contextlib.contextmanager
def spark_build(arguments: Namespace) -> Generator[SparkSession, None, None]:
    """
    Build the spark object.

    Args:
        arguments (Namespace): arguments passed to the run.py

    Yields:
        SparkSession object

    """
    spark_builder = SparkSession.builder
    app_name = Path(__file__).parent.name
    if arguments.env == "dev":
        spark = spark_builder.appName(app_name).getOrCreate()
    elif arguments.env == "prod" or arguments.env == "stage":
        raise NotImplementedError
    yield spark
