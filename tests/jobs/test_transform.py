from src.jobs.transform import explode_df


def test_explode_df(spark_session_test):
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