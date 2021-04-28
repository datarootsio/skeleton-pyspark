"""Integration-test transform jobs."""
from pyspark.sql import SparkSession, Row

from src.jobs.transform import explode_df, clean_df, transform_df


def test_explode_df(spark_session_test: SparkSession) -> None:
    """Confirm that explosion of DF works well."""
    pre_explode_data = [("a b,c d",), ("",), ("12",), ("123*4",)]
    df = spark_session_test.createDataFrame(pre_explode_data).toDF("in")
    out_df = explode_df(df, input_col="in", output_col="out")
    assert [item["out"] for item in out_df.collect()] == [
        "a",
        "b,c",
        "d",
        "",
        "12",
        "123*4",
    ]


def test_clean_df(spark_session_test: SparkSession) -> None:
    """Confirm that clean of DF works well."""
    pre_clean_data = ["aAb*,c4e, d4", "", "\\", "12", "43", "123*4"]
    list_tuple = [(item,) for item in pre_clean_data]
    df = spark_session_test.createDataFrame(list_tuple).toDF("in")
    out_df = clean_df(df, input_col="in", output_col="out")
    assert [item["out"] for item in out_df.collect()] == [
        "aAbc4ed4",
        "12",
        "43",
        "1234",
    ]


def test_end_to_end_transform(spark_session_test: SparkSession) -> None:
    """Confirm that the complete transformation of DF works well."""
    pre_clean_data = ["aAb*,c4e, d4", "d4,", "D4", "\\", "12", "43", "123*4"]
    list_tuple = [(item,) for item in pre_clean_data]
    df = spark_session_test.createDataFrame(list_tuple).toDF("value")
    out_df = transform_df(df)
    assert out_df.collect() == [
        Row(lower_cased="aabc4e", count=1),
        Row(lower_cased="43", count=1),
        Row(lower_cased="1234", count=1),
        Row(lower_cased="d4", count=3),
        Row(lower_cased="12", count=1),
    ]
