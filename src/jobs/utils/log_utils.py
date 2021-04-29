"""Utilities related to logging."""
from pyspark.sql import SparkSession
from py4j.java_gateway import JavaObject  # type: ignore

from src.jobs.utils.general import EnvEnum


class Logger:
    """Logger class connecting to the SparkLogger."""

    def __init__(
        self,
        env: EnvEnum,
        spark: SparkSession,
    ) -> None:
        """
        Initialize the logger to connect to the SparkLogger.

        Args:
            env (EnvEnum): The level of EnumEnv (dev, prod, stage)
            spark (SparkSession): The Spark session whose logger\
             will be accessed
        """
        self.spark = spark
        self.logger = self.init_logger()
        self.set_log_level(env)
        self.info = self.logger.info
        self.warn = self.logger.warn
        self.debug = self.logger.debug

    def init_logger(self) -> JavaObject:
        """Get the Log4J logger."""
        if hasattr(self, "logger") is False:
            log4j_manager = self.spark._jvm.org.apache.log4j.LogManager  # type: ignore
            self.logger = log4j_manager.getLogger(__name__)
        return self.logger

    def set_log_level(self, env: EnvEnum) -> None:
        """
        Set the level of logging.

        Args:
            env (EnvEnum): The level of EnumEnv (dev, prod, stage)

        Returns:
            None
        """
        levels = self.spark._jvm.org.apache.log4j.Level  # type: ignore
        if env == EnvEnum.dev:
            specific_level = levels.DEBUG
        elif env == EnvEnum.stage:
            specific_level = levels.INFO
        elif env == EnvEnum.prod:
            specific_level = levels.WARN
        else:
            raise NotImplementedError
        self.logger.warn(f"Setting log level to {specific_level}")
        self.logger.setLevel(specific_level)
