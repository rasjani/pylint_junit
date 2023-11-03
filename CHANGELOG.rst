Changelog
=========

0.3.4 (2023-03-11)
------------
- Fix console output

0.3.3 (2023-03-11)
------------
- Add support pylint for 3.0

0.3.2 (2020-27-10)
------------
- Fix classname

0.3.1 (2020-27-10)
------------
- Fix byte strings 

0.3.0 (2020-27-10)
------------
- Avoid overwriting existing modules. [Jani Mikkonen]
  Fixes #1
- Added link to junit_xml. [Jani Mikkonen]
- Lintian fixes. [Jani Mikkonen]
- Add more info to stderr. [Jani Mikkonen]

  Due to azure test results not showing stdout by default, only stderr as
  a stacktrace so its now a bit more straight forward to find offending
  lines.
- Add classname so that this works in gitlab [themanifold]
- Use Failure instead of error [Jeff Cook]

0.1.0 (2019-03-05)
------------------
- Add all fully passed files also to the report. [Jani Mikkonen]
- Removed unnessary flake8 plugins. [Jani Mikkonen]
- Version with the old way. [Jani Mikkonen]
- Removed lint and fluff. [Jani Mikkonen]
