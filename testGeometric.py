# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 00:21:57 2018

@author: diary
"""

from itertools import accumulate
from operator import mul
n = 1
ratio = 3
start = 4

progression = [start * ratio**i for i in range(n)]

print(3 + sum(progression))