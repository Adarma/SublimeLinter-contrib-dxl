#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Adam Cadamally
# Copyright (c) 2014 Adam Cadamally
#
# License: MIT
#

"""This module exports the Dxl plugin class."""

from SublimeLinter.lint import Linter, util
from os.path import abspath, dirname, join, isfile

def LinterPath():
    """Ascertain the dxl.exe path from this .py files path because sublime.packages_path is unavailable at startup."""
    ThisPath = abspath(dirname(__file__))
    if isfile(ThisPath):
        # We are in a .sublime-package file in the 'Installed Package' folder
        return abspath(join(ThisPath, '..', '..', 'Packages', 'DXL', 'Lint', 'dxl.exe'))
    else:
        # We are in a subfolder of the 'Packages' folder
        return abspath(join(ThisPath, '..', 'DXL', 'Lint', 'dxl.exe'))

LINTER_PATH = LinterPath()

class Dxl(Linter):

    """Provides an interface to dxl."""

    syntax = 'dxl'
    cmd = [LINTER_PATH]

    regex = (
        r'^-(?:(?P<error>E)|(?P<warning>W))- DXL:'
        r' <(?P<path>.*?):(?P<line>[0-9]+)> '
        r'''(?P<message>(?:undeclared variable|badly formed token|incorrect arguments? for(?: function)|Invalid '//<Requires>' syntax: Expected '#include '|could not (?:open|run) include file) \((?P<near>.*?)\).*|.*)'''
    )

    tempfile_suffix = 'dxl'
    error_stream = util.STREAM_STDOUT
