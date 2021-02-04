#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    
    time = s.split(":")
    
    a = ""
    
    if(time[2][len(time[2])-2] == 'P'):
        if(int(time[0]) != 12):
            a = str(int(time[0]) + 12)
        else:
            a = time[0]
    
    else:
        if(int(time[0]) == 12):
            a = "00"
        else:
            a = time[0]    
    
    a += ":" + time[1] + ":"
        
    for i in time[2]:
        if i.isdigit():
            a += i
    
    return a
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
