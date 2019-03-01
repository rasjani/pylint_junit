
pylint-junit
============

Pylint plugin that generates JUnit based report that can be consumed by CI environments like Jenkins, Azure Devops and such.

Installation
============

Install the package with

.. code-block::

   pip install pylint_junit

or add it to your requirements.

Usage
=====

After the plugin has been installed there are few options to take it into use.

Add following lines into your .pylintrc:

.. code-block::

   [MASTER]
   load-plugins=pylint_junit
   [REPORTS]
   output-format=json

Or you could pass the reporter class directly from command-line like this:

.. code-block::

   pylint --output-format=pylint_junit.JUnitReporter src/

Or if you have enabled the loading of pylint_junit plugin in your rc file, you can just use:

.. code-block::

   pylint --output-format=junit src/

Dependencies
============


* junit_xml

Bugs / Feedback
===============

Use Github Issue Tracker
