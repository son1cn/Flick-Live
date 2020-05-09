#!/usr/bin/env python3

import os
import sys
import time

lib_dir = os.path.normpath(os.path.dirname(os.path.realpath(__file__)) + '/modules/link-python/lib/')
sys.path.insert(0, lib_dir)
print(lib_dir)

try:
    import link
except ImportError:
    exit("link is not properly installed")


lib_dir = os.path.normpath(os.path.dirname(os.path.realpath(__file__)) + '/modules/Flick/flick/')
sys.path.insert(0, lib_dir)
print(lib_dir)

try:
    import flicklib
except ImportError:
    exit("Flick is not properly installed")

import signal
import time
import curses
from curses import wrapper
