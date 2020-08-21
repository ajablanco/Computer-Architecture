#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *


cpu = CPU()

cpu.load("examples/test.ls8")
cpu.run() 