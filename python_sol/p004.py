#
# Solution to Project Euler problem 4
#
# Author: Xiaochen Li
# Date: May 11, 2019
#
#
# Problem: Find the largest palindrome made from the product of two
#          3-digit numbers.
#
# The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99.
#



'''
1. check from 999 x 999 to 100 x 100 get the first palindrome
######## however this is wrong, just like 4x4 is larger than 5x3 while program
######## stop at 5x3 first
## 1* find the max through all these calcs
2. brute force?
3. isPalindrom
'''
from utils import timeout


def isPalindrom( n ):
    return n == int(str(n)[::-1])  ## int -> slice str -> int

@timeout(report_time=True)
def largest_palindrom():
    return max( i * j
    for i in range (999,99,-1)
    for j in range (999,99,-1) ## to include 100
    if ( isPalindrom( i * j ) )
    )


if __name__ == "__main__":
    print( largest_palindrom() )
