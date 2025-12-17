#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr:list) -> int:
    n = len(arr)
    primary = 0
    secondary = 0
    
    for i in range(n):
        assert len(arr[i]) == n
        
        for j in range(n):
            assert -100 <= arr[i][j] <= 100
        primary += arr[i][i]
        secondary += arr[i][n - i - 1]
        
    return abs(primary - secondary)
