from pyspark.sql import SparkSession, DataFrame


def extract_file(spark: SparkSession, file_path: str) -> DataFrame:
    """
    Extracts the local file into a DF
    Args:
        spark (SparkSession): spark session to read the file
        file_path (str): file_path to extract

    Returns:
        DataFrame of single-column text file

    """
    return spark.read.text(file_path)
