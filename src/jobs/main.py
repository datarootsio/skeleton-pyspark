"""This module is the entry-point for the run.py to handle spark session \
building and ETL."""

import contextlib
from pyspark.sql import SparkSession
from pathlib import Path
from typing import Generator

from src.jobs import extract, transform, load
from src.jobs.utils.general import EnvEnum
from src.jobs.utils.log_utils import Logger


def jobs_main(spark: SparkSession, logger: Logger, file_path: str) -> None:
    """
    High-level function to perform the ETL job.

    Args:
        spark (SparkSession) : spark session to perform ETL job
        logger (Logger) : logger class instance
        file_path (str): path on which the job will be performed

    """
    df = extract.extract_file(spark, file_path)
    logger.info(f"{file_path} extracted to DataFrame")

    count_df = transform.transform_df(df)
    logger.info("Counted words in the DataFrame")

    load.write_to_path(count_df)
    logger.info("Written counted words to path")


@contextlib.contextmanager
def spark_build(env: EnvEnum) -> Generator[SparkSession, None, None]:
    """
    Build the spark object.

    Args:
        env (EnvEnum): environment of the spark-application

    Yields:
        SparkSession object

    """
    spark_builder = SparkSession.builder
    app_name = Path(__file__).parent.name

    if env == EnvEnum.dev:
        spark = spark_builder.appName(app_name).getOrCreate()
    else:
        raise NotImplementedError
    try:
        yield spark
    finally:
        spark.stop()
