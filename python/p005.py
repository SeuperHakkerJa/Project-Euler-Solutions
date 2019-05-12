#
# Solution to Project Euler problem 5
#
# Author: Xiaochen Li
# Date: May 11, 2019
#
#
# Problem: What is the smallest positive number that is evenly divisible by all
#          of the numbers from 1 to 20?
#
#


def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return int(a * b / gcd(a, b))

def lcm_Of_1_To_20():
    ans = 1
    for i in range( 1, 21 ):
        ans = lcm( ans, i)
    return ans


if __name__ == "__main__":
    print( lcm_Of_1_To_20() )
