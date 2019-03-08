# -*- coding: utf-8 -*-

from codecs import open
from os.path import join, abspath, dirname
from setuptools import setup, find_packages

CWD = abspath(dirname(__file__))
PACKAGE_NAME = 'pylint_junit'

# Get the long description from the README file
with open(join(CWD, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(join(CWD, 'requirements.txt'), encoding="utf-8") as f:
    REQUIREMENTS = f.read().splitlines()

VERSION_PATH = join(CWD, "src", PACKAGE_NAME, 'version.py')
exec(compile(open(VERSION_PATH).read(), VERSION_PATH, 'exec'))


CLASSIFIERS = '''Development Status :: 4 - Beta
Environment :: Console
Intended Audience :: Developers
Intended Audience :: End Users/Desktop
Intended Audience :: Information Technology
Intended Audience :: System Administrators
License :: OSI Approved :: MIT License
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.7
Topic :: Software Development :: Libraries
Topic :: Software Development :: Quality Assurance
Topic :: Software Development :: Testing
Topic :: Utilities
Operating System :: MacOS
Operating System :: Microsoft :: Windows
Operating System :: POSIX :: Linux
Operating System :: POSIX :: Other
'''.strip().splitlines()

setup(name=PACKAGE_NAME,
      version=VERSION,  # noqa: F821
      description='pylint reporter for junit format.',
      long_description=long_description,
      classifiers=CLASSIFIERS,
      url='https://github.com/omenia/pylint_junit',
      author='Jani Mikkonen',
      author_email='jani.mikkonen@siili.com',
      license='MIT',
      platforms='any',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      install_requires=REQUIREMENTS,
      include_package_data=True,
      zip_safe=False)
