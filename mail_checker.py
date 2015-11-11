#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os
import sys

my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(my_path, "libtool"))
#print sys.path
from libtool.libtool import append
append("iconizer")
#print sys.path
from iconizer import Iconizer

log = logging.getLogger(__name__)


def main():
    Iconizer().execute({"mail checker": ["outlook_checker.py",]})


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
