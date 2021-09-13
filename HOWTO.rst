=======
How To
=======

This is an opinionated project skeleton for a Pyspark based data pipeline.

-------------------------
Running the project
-------------------------

Before running the commands using `make`, ensure that:

* `poetry` is `installed <https://python-poetry.org/docs/#installation>`_.
* python 3.8+ is installed

.. code:: bash

    git clone https://github.com/datarootsio/skeleton-pyspark.git
    cd skeleton-pyspark
    poetry --version
    poetry install
    poetry run spark-submit run.py dev

Makefile
---------

Try out the :code:`make <command>`.

+-----------------+---------------------------------------------------+
| <command>       |  description                                      |
+=================+===================================================+
| help            | lists the options available with make             |
+-----------------+---------------------------------------------------+
| lint            | flake8 lint and black code style                  |
+-----------------+---------------------------------------------------+
| mypy            | static analysis with mypy                         |
+-----------------+---------------------------------------------------+
| bandit          | discover common security issues                   |
+-----------------+---------------------------------------------------+
| test            | run tests in the current environment              |
+-----------------+---------------------------------------------------+
| coverage        | generate coverage report                          |
+-----------------+---------------------------------------------------+
| sphinx.html     | build html documentation                          |
+-----------------+---------------------------------------------------+
| submit          | submits the job without any extra dependency      |
+-----------------+---------------------------------------------------+
| submit_with_dep*| submits the job with packaged dependency          |
+-----------------+---------------------------------------------------+
| run-pipeline    | runs the full-CI/CD workflow locally              |
+-----------------+---------------------------------------------------+

\* uses the :code:`docker-compose` command. Ensure that your docker-compose version is 1.29.0+

-----------------
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

---------------
Submitting jobs
---------------
Jobs are submitted to the cluster with the :code:`spark-submit` script.

- If the nodes on the cluster already have all the required Python dependencies installed locally, :code:`make submit` can be used. This will not use the :code:`--py-files` argument.


- If a particular dependency is missing on the nodes of the cluster :code:`make submit_with_dep` can be used to package the dependency with the :code:`--py-files` `argument <https://spark.apache.org/docs/3.1.1/submitting-applications.html#bundling-your-applications-dependencies>`_.


Using :code:`make submit_with_dep`
-----------------------------------------
:code:`make submit_with_dep` can be used to package and send Python dependencies to the cluster-node if it does not have the required Python dependencies.

#. Ensure that the poetry per-requisite is installed as described in :ref:`Running the project`.
#. Extra dependencies can be added to the `pyproject.toml` with the :code:`poetry add <module_name>` command. For example :code:`poetry add click`.
#. In `docker/package_dependency.Dockerfile` edit the `FROM python:3.8` to the operating system of the nodes. This step is strictly not-necessary if the new dependency added in step 2 are pure-python files. For example: if the nodes are running Ubuntu 20.04, change the line to `FROM ubuntu:20.04`.
#. Submit the job with :code:`make submit_with_dep`.

This will build a docker image where the Python modules are installed which are archived as package.zip in the root directory. They are submitted to the cluster with the command

.. code:: bash

    spark-submit --py-files package.zip run.py arg1 arg2

----------
Build docs
----------
It is a pre-requisite that the dependencies are installed as described in see :ref:`Running the project`.
Different flavours of the documentation can be generated with wildcard entries:

.. code:: bash

    make sphinx.html # Builds HTML doc at docs/build/html/index.html
    make sphinx.epub # Builds EPUB doc at docs/build/epub

