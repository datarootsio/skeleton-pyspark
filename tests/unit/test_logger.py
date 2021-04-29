"""Tests the logger."""
import logging
import pytest
from pytest_mock.plugin import MockerFixture

from src.jobs.utils import log_utils
from src.jobs.utils.general import EnvEnum


class TestLogger:
    """Test the functionality of the logger."""

    @pytest.mark.parametrize(
        "env,effective_level",
        [
            (EnvEnum.dev, 10),
            (EnvEnum.stage, 20),
            (EnvEnum.prod, 30),
        ],
    )
    def test_set_log_level(
        self, env: EnvEnum, effective_level: int, mocker: MockerFixture
    ) -> None:
        """Test the setting of the log-level."""
        mocker.patch.object(log_utils.Logger, "__init__", lambda x: None)
        patched_logger = log_utils.Logger()
        patched_logger.spark = mocker.Mock()
        patched_logger.spark._jvm.org.apache.log4j.Level = logging
        patched_logger.logger = logging.getLogger(f"{env}_{effective_level}")
        assert patched_logger.logger.getEffectiveLevel() == 30
        patched_logger.set_log_level(env)
        assert patched_logger.logger.getEffectiveLevel() == effective_level
