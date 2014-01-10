#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by yks0051
# Copyright (c) 2014 yks0051
#
# License: MIT
#

"""This module exports the Dxl plugin class."""

from SublimeLinter.lint import Linter, util


class Dxl(Linter):

    """Provides an interface to dxl."""

    syntax = ''
    cmd = 'dxl'
    executable = None
    regex = r''
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None
