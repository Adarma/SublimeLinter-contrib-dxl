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


class Dxl(Linter):

    """Provides an interface to dxl."""

    syntax = 'dxl'
    cmd = 'C:/Portable/SU336B~1/Data/Packages/DXL/Lint/DxlLint.exe @'

    regex = (
        r'^-(?:(?P<error>E)|(?P<warning>W))- DXL:'
        r' <(?P<path>.*):(?P<line>[0-9]+)> '
        r'(?P<message>(?:undeclared variable|incorrect arguments for) \((?P<near>.*)\)|.*)$'
    )

    tempfile_suffix = 'dxl'
    error_stream = util.STREAM_STDOUT
