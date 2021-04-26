import sys

from src.jobs import (
    main,
)
from src.jobs.utils.general import (
    get_argument_parser
)

if __name__ == '__main__':
    argument_parser = get_argument_parser()
    arguments = argument_parser.parse_args(sys.argv[1:])
    with main.spark_build(arguments) as spark:
        main.main(spark,
                  file_path=arguments.file_path)
