from pathlib import Path
from pyspark.sql import SparkSession, DataFrame


def extract_file(spark: SparkSession) -> DataFrame:
    """
    Extracts the local file into a DF
    Args:
        spark (SparkSession): spark session to read the file

    Returns:
        DataFrame of single-column text file

    """
    path_to_local_file = f"file://{Path(__file__).parents[2]}/LICENSE"
    return (spark.
            read.
            text(path_to_local_file))
