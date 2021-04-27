import sys

from src.jobs import (
    main,
)
from src.jobs.utils.general import (
    get_argument_parser,
)
from src.jobs.utils import log_utils

if __name__ == '__main__':
    argument_parser = get_argument_parser()
    arguments = argument_parser.parse_args(sys.argv[1:])
    with main.spark_build(arguments) as spark:
        logger = log_utils.Logger(env=arguments.env,
                                  spark=spark)
        logger.info("Spark and logger initialized")
        main.main(spark,
                  logger,
                  file_path=arguments.file_path)
