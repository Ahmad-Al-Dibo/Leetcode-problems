#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    assert 1 <= len(ar) <= 10
    for i in ar:
        assert 0 <= i <= 10**10
    return sum(ar)
