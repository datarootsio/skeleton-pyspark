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

----------
Windows Troublshoot
----------
1. Download 7-zip from https://www.7-zip.org/download.html (to extract .zip/.tgz/.tar)
2. Download Apache Spark from http://spark.apache.org/downloads.html (Spark Release 3.1.2, Pre-built for Hadoop 3.2 and later),
    - Download is a .tgz file, extract it to get a .tar file and finally extract to get "spark-3.1.2-bin-hadoop3.2" folder
    - Store this "spark-3.1.2-bin-hadoop3.2" folder in a directory like "C:\Spark\spark-3.1.2-bin-hadoop3.2"
3. Download Java SDK 11 (a.k.a. JDK) from https://www.oracle.com/java/technologies/javase-jdk11-downloads.html
    - MUST create an Oracle account to download, open source JDKs like from https://jdk.java.net/java-se-ri/11 WILL NOT WORK!!!
    - MUST be version 11, different versions may not work!
    - Store the JDK in a directory like "C:\Program Files\Java\jdk-11.0.12"
4. Under "System Properties" > "Advanced" > "Environment Variables" (or simply search "environment" in search bar and select "Edit the system environment variables")
    - Set these System Variables:
+----------------+------------------------------------------+
| <Variable>     |  Value                                   |
+================+==========================================+
| HADOOP_HOME    | C:\Spark\spark-3.1.2-bin-hadoop3.2       |
+----------------+------------------------------------------+
| JAVA_HOME      | C:\Program Files\Java\jdk-11.0.12        |
+----------------+------------------------------------------+
| SPARK_HOME     | C:\Spark\spark-3.1.2-bin-hadoop3.2       |
+----------------+------------------------------------------+
    - Under User Variables, add these to Path:
        - %JAVA_HOME%\bin
        - %HADOOP_HOME%\bin
        - %SPARK_HOME%\bin
5. In PyCharm, create a new project like "testing java", create a file main.py and paste this code:

.. code:: bash

    import findspark
    import pyspark
    from pyspark.sql import SparkSession

    findspark.init()
    spark = SparkSession.builder.getOrCreate()
    df = spark.sql("select 'spark' as hello ")
    df.show()

- if errors appear at "import" commands, right click on them to manually install!
- run main.py, result should be something like:
(error messages)
+-----+
|hello|
+-----+
|spark|
+-----+

6. Go to https://github.com/datarootsio/rootsacademy-pyspark-101, under Code, clone using SSH,
get the link and use it in Pycharm to clone the repo

7. Pyspark errors and checks:
- If Java gateway issues, check version of Java is JDK 11 (not JRE, not version 8 or version > 11), and check step 4 variables are setup correctly
- If Hadoop issues, check step 4 variables are setup correctly
