#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    money = 0
    
    for i in range(len(bill)):
        if i != k:
            money += bill[i]
    
    money /= 2
            
    if money == b:
        print('Bon Appetit')
    else:
        print(b - int(money))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
