#!/bin/python3
#this code finds the maximum length of 1's in the binary representation of a base 10 number.
#for ex: binary of 125 = 1111101, so we first need to convert 125 to binary (1111101) and then return 5, as 1's are repeated maximum 5 times:

import math
import os
import random
import re
import sys

    
def getBinary(n):
#this function gets the binary representation of a base 10 number:
    res = []
    while n!=0:
        r = n%2
        #print(r)
        res.append(r)
        n = n//2
    res.reverse
    return res


def getMaxLen(ls):
#this function finds the maximum length of consecutive 1's in the binary representation: 
    ls_ln = []
    
    while len(ls) > 1:
        if 0 in ls:
            for i in range(len(ls)):
                if ls[i] == 0:
                    ls_ln.append(i)
                    break
                    
            ls = ls[i+1:]
        else:
            ls_ln.append(len(ls))
            break
                    
    if len(ls) == 1:
        if ls[0] == 1:
            ls_ln.append(1)
    return max(ls_ln)
            
if __name__ == '__main__':
    n = int(input())
    print(getMaxLen(getBinary(n)))
