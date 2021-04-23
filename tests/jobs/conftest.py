import pytest
from pyspark.sql.session import SparkSession


@pytest.fixture(scope="module")
def spark_session_test():
    return SparkSession.builder.appName("pytest").getOrCreate()
