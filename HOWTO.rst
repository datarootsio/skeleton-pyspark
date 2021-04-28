=======
How To
=======

This is an opinionated project skeleton for a Pyspark based data pipeline.

------------------------
Run the example on spark
------------------------

Pre-requisite `git`, `spark-submit`,

.. code:: bash

    git clone git@github.com:datarootsio/skeleton-pyspark.git
    cd skeleton-pyspark
    spark-submit run.py --env dev

-------------------------
Running the project
-------------------------

Before running the commands using `make`, ensure that `poetry` is `installed <https://python-poetry.org/docs/#installation>`_.
Install the developer dependencies with:

.. code:: bash

    git clone git@github.com:datarootsio/skeleton-pyspark.git
    cd skeleton-pyspark
    poetry --version
    poetry install

Makefile
---------

Try out the :code:`make <command>`.

+----------------+---------------------------------------------------+
| <command>      |  description                                      |
+================+===================================================+
| help           | lists the options available with make             |
+----------------+---------------------------------------------------+
| lint           | flake8 lint and black code style                  |
+----------------+---------------------------------------------------+
| mypy           | static analysis with mypy                         |
+----------------+---------------------------------------------------+
| bandit         | discover common security issues                   |
+----------------+---------------------------------------------------+
| test           | run tests in the current environment              |
+----------------+---------------------------------------------------+
| coverage       | generate coverage report                          |
+----------------+---------------------------------------------------+
| sphinx.html    | build html documentation                          |
+----------------+---------------------------------------------------+
| submit         | submits the job via `spark-submit`                |
+----------------+---------------------------------------------------+
| run-pipeline   | runs the full-CI/CD workflow locally              |
+----------------+---------------------------------------------------+


Project structure
-----------------
The project structure tree is shown below.
This structure is designed in a way to organize pyspark projects.
Feedback / PRs are always welcome about the structure.

::

    skeleton-pyspark
    ├── .github           # GitHub actions
    ├── HOWTO.rst         # This file
    ├── docs              # Sphinx documentation
    │   └── source        # Configuration for sphinx
    ├── run.py            # Entry point to spark job
    ├── src               # Source code
    │   └── jobs          # Sources related to ETL job
    │       └── utils     # Utilities to assist ETL job
    └── tests             # Tests
        ├── integration   # Integration tests
        └── unit          # Unit tests


Build docs
----------
It is a pre-requisite that the dependencies are installed as described in see :ref:`Running the project`.
Different flavours of the documentation can be generated with wildcard entries:

.. code:: bash

    make sphinx.html # Builds HTML doc at docs/build/html/index.html
    make sphinx.epub # Builds EPUB doc at docs/build/epub




