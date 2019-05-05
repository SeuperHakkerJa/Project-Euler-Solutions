# 
# Solution to Project Euler problem 1
#
# Author: Xiaochen Li
# Date: May 04, 2019
#
#
# Problem: Find the sum of all the multiples of 3 or 5 below 1000.


def find_mul_of_3_or_5():

    s = sum( x for x in range(1000) if x % 3 == 0 or x % 5 == 0 )
    return str(s)

if __name__ == "__main__":
    print( find_mul_of_3_or_5() )
