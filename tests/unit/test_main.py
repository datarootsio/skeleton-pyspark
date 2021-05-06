"""Test the main file."""
import logging

from src.jobs.main import jobs_main, spark_build
from src.jobs import extract, transform, load
from pyspark.sql import SparkSession
from pytest_mock import MockFixture
from src.jobs.utils.general import EnvEnum


def test_jobs_called(mocker: MockFixture) -> None:
    """Test the all the jobs are called."""
    extract.extract_file = mocker.Mock(return_value="extracted")
    transform.transform_df = mocker.Mock(return_value="transformed")
    load.write_to_path = mocker.Mock()

    jobs_main(
        spark="temp", logger=logging.getLogger("test_jobs_cancelled"), file_path="temp"
    )
    transform.transform_df.assert_called_with("extracted")
    load.write_to_path.assert_called_with("transformed")


def test_spark_session_built(mocker: MockFixture) -> None:
    """Test the spark context is built and shut down correctly."""
    SparkSession.builder = mocker.Mock(return_value="mocked_build")
    with spark_build(EnvEnum.dev) as spark_session:
        pass
    SparkSession.builder.appName.assert_called_with("jobs")
    SparkSession.builder.appName().getOrCreate.assert_called()
    spark_session.stop.assert_called()
