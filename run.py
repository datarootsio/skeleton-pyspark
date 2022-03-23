"""Entry point to the pyspark job."""
import typer
from pathlib import Path

from src.jobs.main import jobs_main, spark_build
from src.jobs.utils.general import EnvEnum
from src.jobs.utils import log_utils
file_path = "file:///databricks/python/lib/python3.8/site-packages/src/jobs/main.py"


def main() -> None:
    """Execute main function for the package."""
    logger = log_utils.Logger(env=EnvEnum.dev, spark=spark)
    logger.info("Spark and logger initialized")
    jobs_main(spark, logger, file_path=file_path)


if __name__ == "__main__":
    main()
