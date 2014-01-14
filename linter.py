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
from os.path import abspath, dirname, join

BASE_PATH = abspath(dirname(__file__))

class Dxl(Linter):

    """Provides an interface to dxl."""

    syntax = 'dxl'
    cmd = '"' + join(BASE_PATH, "..", "DXL", "Lint", "dxl.exe") + '"'

    regex = (
        r'^-(?:(?P<error>E)|(?P<warning>W))- DXL:'
        r' <(?P<path>.*):(?P<line>[0-9]+)> '
        r'''(?P<message>(?:undeclared variable|incorrect arguments for|Invaild '//<Requires>' syntax: Expected '#include '|could not (?:open|run) include file) \((?P<near>.*?)\).*|.*)$'''
    )

    tempfile_suffix = 'dxl'
    error_stream = util.STREAM_STDOUT
