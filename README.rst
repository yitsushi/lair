lair
====

**lair** is a small lightweight helper to create eggs
for flask based microservices.

Install
~~~~~~~

::

   pip install lair

**For details and extra helpers, read the
documentation: https://lair.readthedocs.io/en/latest/**

In the docs:
  * CLI usage
  * built-in decorators
  * built-in Blueprints

Example usage:
~~~~~~~~~~~~~~

::

   # This will generate a project directory
   # for your new microservice with Flask
   lair --project-name my-shiny-project

   # This will generate a  project directory
   # for your new microservice with Flask and SqlAlchemy,
   # and place an example modell in
   # project-dir/project_name/models/example.txt
   #  to use this as a model just rename from .txt to .py
   lair --project-name my-shiny-project --with-db


.. image:: https://coveralls.io/repos/github/yitsushi/lair/badge.svg?branch=master
   :target: https://coveralls.io/github/yitsushi/lair?branch=master
.. image:: https://travis-ci.org/yitsushi/lair.svg?branch=master
   :target: https://travis-ci.org/yitsushi/lair
.. image:: https://readthedocs.org/projects/lair/badge/?version=latest
   :target: https://lair.readthedocs.io
