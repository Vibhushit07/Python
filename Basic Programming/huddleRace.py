'''
    A video player plays a game in which the character competes in a hurdle race. 
    Hurdles are of varying heights, and the characters have a maximum height they can jump. 
    There is a magic potion they can take that will increase their maximum jump height by 1 unit for each dose. 
    How many doses of the potion must the character take to be able to jump all of the hurdles. 
    If the character can already clear all of the hurdles, return 0.

    Example:
    height = [1, 2, 3, 3, 2]
    k = 1

    The character can jump 1 unit high initially and must take 3 - 1 = 2 doses of potion to be able to jump all of the hurdles.

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.
def hurdleRace(k, height):
    maxi = -1
    
    for h in height:
        if maxi < h:
            maxi = h
    
    if maxi > k:
        return maxi - k
    else:
        return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
