"""JUnit reporter"""
from __future__ import absolute_import, print_function

import sys
from linecache import getline
from pylint.interfaces import IReporter         # noqa: F401 # TODO: Report bug to flake8 tools, its is used in __implements__
from pylint.reporters import BaseReporter
from pylint.lint import PyLinter as linter      # noqa: N813,F401
from junit_xml import TestSuite, TestCase
from .version import get_version                # noqa: F401

class JUnitReporter(BaseReporter):
    """Report messages and layouts in JUnit."""

    __implements__ = IReporter
    name = "junit"
    extension = "junit"

    def __init__(self, output=sys.stdout):
        BaseReporter.__init__(self, output)
        self.items = {}
        self.current_module = None

    def on_set_current_module(self, module, filepath):
        self.current_module = module
        self.items[module] = TestSuite(module)

    def on_close(self, stats, previous_stats):
        pass

    def handle_message(self, msg):
        """Manage message of different type and in the context of path."""
        stdout_line = "{0}:{1}:{2}:{3}".format(msg.path, msg.line, msg.column, getline(msg.path, msg.line).strip())
        stderr_line = "{0}:{1}".format(msg.msg_id, msg.msg)
        testcase_name = "{0}:{1}:{2}".format(msg.module, msg.line, msg.column)
        testcase = TestCase(testcase_name, stdout=stdout_line, stderr=stderr_line, file=msg.path, line=msg.line, category=msg.category)
        testcase.add_error_info(message=msg.symbol, output=stderr_line)
        self.items[self.current_module].test_cases.append(testcase)

    def display_messages(self, layout):
        print(TestSuite.to_xml_string(self.items.values()), file=self.out)

    def display_reports(self, layout):
        """Don't do nothing in this reporter."""
        pass

    def _display(self, layout):
        """Don't do nothing in this reporter."""
        pass


def register(linter):  # noqa: F811
    """Register the reporter classes with the linter."""
    linter.register_reporter(JUnitReporter)
