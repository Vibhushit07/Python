'''
    Write a program that accepts the lengths of three sides of a triangle as inputs:
    - The program output should indicate whether or 
      not the triangle is an equilateral triangle. (all three sides are equal)
    - The program output should indicate whether or 
      not the triangle is right triangle. (the square of one side equals the sum of the squares of the other two sides)
'''

import math

print("Enter side of triangle")

a = int(input())
b = int(input())
c = int(input())

if a == b and a == c:
    print("Equilateral triangle")

else:
    h = 0
    p = 0
    base = 0

    if a > b and a > c:
        h = a
        p = b
        base = c

    elif b > a and b > c:
        h = b
        p = a
        base = c

    else:
        h = c
        p = a
        base = b

    if int(math.sqrt(math.pow(p, 2) + math.pow(base, 2))) == h:
        print("Right triangle")
    else:
        print("Neither Equilateral triangle nor Right triangle")