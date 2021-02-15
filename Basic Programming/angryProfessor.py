'''
    A Discrete Mathematics professor has a class of students. 
    Frustrated with their lack of discipline, the professor decides to cancel class 
    if fewer than some number of students are present when class starts. 
    Arrival times go from on time (arrivalTime <= 0) to arrived late (arrivalTime > 0).

    Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled.

    Example:
    n = 5
    k = 3
    a = [-2, -1, 0, 1, 2]
    The first 3 students arrived on. The last 2 were late. The threshold is 3 students, so class will go on. Return YES.

    Note: Non-positive arrival times (a[i] <= 0) indicate the student arrived early or on time; 
    positive arrival times (a[i] > 0) indicate the student arrived a[i] minutes late.
    Return YES if class is cancelled, or NO otherwise.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    count = 0
    
    for i in a:
        if i <= 0:
            count += 1
            
    if count < k:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
