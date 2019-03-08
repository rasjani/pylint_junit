
pylint_junit
============

Pylint plugin that generates JUnit based report that can be consumed
by CI environments like Jenkins, Azure Devops and such.

Why ?
=====

At the time of writing, few tools existed that where able to generate
JUnit format from pylint output. Both of these projects where not
handling "empty" results scenario well, eg both cases generated an empty
file and that caused issues in ci as the resulting document was not
proper xml file. Another issue was that issues found by pylint where
marked under single testcase failure and this caused atleast Azure to
report a single item per file even thought there could have been multiple.

Thus, pylint_junit was written.

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
   output-format=junit

This does set the default output to junit, so if still want to run pylint and get
normal output, you might want to consider omitting the "output-format=junit"
portion and only when junit format is needed, provide it via command line like this:

.. code-block::

   pylint --output-format=junit src/



Or, without making any changes to your pylint configuration, you can just pass the class
as report formatter like this:

.. code-block::

   pylint --output-format=pylint_junit.JUnitReporter src/

Dependencies
============


* junit_xml__

__ https://github.com/kyrus/python-junit-xml

Bugs / Feedback
===============

Use Github Issues Tracker @ https://github.com/omenia/pylint_junit/issues
