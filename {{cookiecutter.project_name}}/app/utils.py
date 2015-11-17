#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: sw=4:ts=4:expandtab

"""
utils
~~~~~

Provides miscellaneous utility methods
"""

from __future__ import (
    absolute_import, division, print_function, with_statement,
    unicode_literals)

import requests

from tempfile import SpooledTemporaryFile
from tabutils import io


def gen_data(location=None, **kwargs):
    """Fetches realtime data and generates records"""
    url = '%s/%s' % (kwargs['BASE_URL'], location)
    r = requests.get(url)
    f = SpooledTemporaryFile()  # wrap to access `fileno`
    f.write(r.content)
    return io.read_xls(r., sanitize=True, encoding=r.encoding)
