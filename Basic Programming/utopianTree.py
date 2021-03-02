'''
    The Utopian Tree goes through 2 cycles of growth every year. 
    Each spring, it doubles in height. Each summer, its height increases by 1 meter.

    A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. How tall will the tree be after n growth cycles?

    For example, if the number of growth cycles is n = 5, the calculations are as follows:

    Period  Height
      0       1
      1       2
      2       3
      3       6
      4       7
      5      14
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return utopianTree(n - 1) + 1
    else:
        return 2 * utopianTree(n - 1)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
