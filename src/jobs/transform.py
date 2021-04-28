"""This module is responsible for transform (T) in ETL."""
from pyspark.sql import DataFrame, functions as func


def explode_df(df: DataFrame, input_col: str, output_col: str) -> DataFrame:
    """
    Explodes the input_column.

    Args:
        df (DataFrame): DataFrame which contains a column "input_column"
        input_col (str): input column name
        output_col (str): output column name

    Returns:
        DataFrame with column exploded

    """
    return df.select(
        func.explode(func.split(func.col(input_col), " ")).alias(output_col)
    )


def clean_df(df: DataFrame, input_col: str, output_col: str) -> DataFrame:
    """
    Clean the df's column by removing non-alphanumeric \
    characters from the column and empty-strings.

    Args:
        df (DataFrame): DataFrame which contains a column "input_column"
        input_col(str): input column for the transformation
        output_col(str): output column for the transformation

    Returns:
        DataFrame with cleaned data

    """
    return df.select(
        func.regexp_replace(func.col(input_col), r"[^a-zA-Z\d]", "").alias(output_col)
    ).where(func.col(output_col) != "")


def lower_case_df(df: DataFrame, input_col: str, output_col: str) -> DataFrame:
    """
    Lower cases a DataFrame's column.

    Args:
        df (DataFrame): DataFrame whose column needs to be lower cased
        input_col (str): input column for the transformation
        output_col (str): output column for the transformation

    Returns:
        DataFrame which contains the lower cased column
    """
    return df.select(func.lower(func.col(input_col)).alias(output_col))


def count_df(df: DataFrame, input_col: str, output_col: str) -> DataFrame:
    """
    Count the instances of the input_column and enters them in output_column.

    Args:
        df (DataFrame): DataFrame whose column needs to be counted
        input_col (str): input column name which should be counted
        output_col (str): output column name containing the count

    Returns:
        DataFrame which contains the count of words

    """
    return df.groupBy(input_col).agg(func.count(input_col).alias(output_col))


def transform_df(raw_df: DataFrame) -> DataFrame:
    """
    Count the number of occurrence of words in a single-column raw dataframe.

    Args:
        raw_df (DataFrame): raw dataframe extracted from the text

    Returns:
        DataFrame of single-column text file

    """
    return (
        raw_df.transform(
            lambda df: explode_df(df, input_col="value", output_col="exploded")
        )
        .transform(lambda df: clean_df(df, input_col="exploded", output_col="cleaned"))
        .transform(
            lambda df: lower_case_df(df, input_col="cleaned", output_col="lower_cased")
        )
        .transform(lambda df: count_df(df, input_col="lower_cased", output_col="count"))
    )
