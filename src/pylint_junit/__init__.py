"""JUnit reporter"""
from __future__ import absolute_import, print_function

import sys
from typing import TextIO
from linecache import getline
from pylint.interfaces import IReporter         # noqa: F401 # TODO: Report bug to flake8 tools, its is used in __implements__
from pylint.reporters import BaseReporter
from junit_xml_2 import TestSuite, TestCase, to_xml_report_string
from .version import get_version                # noqa: F401

def to_unicode(line):
    # Hack, fix later .. Or drop completely if/when not supporting python2 anymore ..
    try:
        return line.decode("utf-8")
    except:
        return line

class JUnitReporter(BaseReporter):
    """Report messages and layouts in JUnit."""

    name = "junit"
    extension = "junit"

    def __init__(self, output: TextIO | None = None):
        BaseReporter.__init__(self, output)
        self.items = {}
        self.current_module = None
        self.current_filepath = None

    def on_set_current_module(self, module, filepath):
        if self.current_module is not None and self.items[self.current_module].test_cases is not None:
            stdout_line = "All checks passed for: {0}".format(self.current_filepath)
            testcase_name = "{0}:0:0".format(self.current_module)
            testcase = TestCase(testcase_name, classname='pylint', stdout=stdout_line, file=self.current_filepath, line=0)
            self.items[self.current_module].test_cases.append(testcase)

        self.current_module = module
        self.current_filepath = filepath
        if module not in self.items:
            self.items[module] = TestSuite(module)

    def on_close(self, stats, previous_stats):
        pass

    def handle_message(self, msg):
        """Manage message of different type and in the context of path."""
        source_line = to_unicode(getline(msg.path, msg.line).strip())
        stdout_line = u"{0}:{1}:{2}:{3}".format(msg.path, msg.line, msg.column, source_line)
        stderr_line = u"{0}:{1}\n{2}".format(msg.msg_id, msg.msg, stdout_line)
        testcase_name = u"{0}:{1}:{2}".format(msg.module, msg.line, msg.column)
        testcase = TestCase(testcase_name, classname='pylint', stdout=stdout_line, stderr=stderr_line, file=msg.path, line=msg.line, category=msg.category)
        testcase.add_failure_info(message=msg.symbol, output=stderr_line)
        self.items[self.current_module].test_cases.append(testcase)

    def display_messages(self, layout):
        xml_str = to_xml_report_string(self.items.values())
        print(xml_str, file=self.out)

    def display_reports(self, layout):
        """Don't do nothing in this reporter."""
        pass

    def _display(self, layout):
        """Don't do nothing in this reporter."""
        pass


def register(linter):
    """Register the reporter classes with the linter."""
    linter.register_reporter(JUnitReporter)
