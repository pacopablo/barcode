#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2008 John Hampton <pacopablo@pacopablo.com>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#
# Author: John Hampton <pacopablo@pacopablo.com>

from setuptools import setup

setup(
    name = 'Symbol Barcode Scanner',
    version = '0.1',
    author = 'John Hampton',
    author_email = 'pacopablo@pacopablo.com',
    url = 'https://pacopablo.com/Projects/SymbolBarcode',
    description = 'Python interface for controlling the Symbol Barcode Scanner',
    license = 'BSD' 
    zip_safe=True,
    packages=['barcode'],
)
