'''
    When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle. 
    In this PDF viewer, each word is highlighted independently.
    There is a list of 26 character heights aligned by index to their letters. 
    
    For example, 'a' is at index 0 and 'z' is at index 25. 
    There will also be a string. 
    Using the letter heights given, determine the area of the rectangle highlight in mm^2 assuming all letters are 1mm wide.

    Example:
    h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    word = "torn"

    The heights are t = 2, o = 1, r = 1 and n = 1. The tallest letter is t = 2 high and there are 4 letters. 
    The hightlighted area will be 2 * 4 = 8 mm^2 so the answer is 8.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    maxi = -1
    
    for w in word:
        if maxi < h[ord(w) - 97]:
            maxi = h[ord(w) - 97]
    
    return maxi * len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
