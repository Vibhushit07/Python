#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    count = dict()
    
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
            
    index = arr[0]
    
    for i in arr:
        if(count[index] < count[i]):
            index = i
        elif(count[index] == count[i]):
            if(index > i):
                index = i
                
    return index

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
