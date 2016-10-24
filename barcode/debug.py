# -*- coding: utf-8 -*-
#
# Copyright (C) 2008 John Hampton <pacopablo@pacopablo.com>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#
# Author: John Hampton <pacopablo@pacopablo.com>

__all__ = ['DummyDebug']

class DummyDebug(object):
    """ Dummy Debug object that sends messages to the bit bucket """

    def __init__(self):
        """ Nothing """

    def write(self, msg):
        """ Notthing """

    def traceback(self):
        """ Nothing """

