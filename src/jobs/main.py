from pyspark.sql import SparkSession

from src.jobs import extract, transform, load


def main():
    spark = SparkSession.builder.appName("skeleton-pyspark").getOrCreate()
    # TODO But what about additional arguments if
    #  you want to run on a cluster?

    df = extract.extract_file(spark)
    count_df = transform.transform_df(df)
    load.write_to_path(count_df)


if __name__ == "__main__":
    main()
