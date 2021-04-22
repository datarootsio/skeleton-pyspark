from src.jobs import extract, transform, load
from pyspark.sql import SparkSession


def main():
    spark = (SparkSession
             .builder
             .appName("skeleton-pyspark")
             .getOrCreate())
    # TODO But what about additional arguments?

    df = extract.extract_file(spark)
    count_df = transform.transform_df(df)
    load.write_to_path(count_df)



if __name__ == "__main__":
    main()
