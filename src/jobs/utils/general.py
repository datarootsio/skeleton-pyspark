"""General utilities around the ETL job."""
from enum import Enum


class EnvEnum(Enum):
    """Maintain the enums of the environments."""

    dev = "dev"
    prod = "prod"
    stage = "stage"
