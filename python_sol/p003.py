# 
# Solution to Project Euler problem 3
#
# Author: Xiaochen Li
# Date: May 04, 2019
#
#
# Problem: What is the largest prime factor of the number 600851475143 ?
#        

import math
from utils import timeout

@timeout(report_time=True)
def find_prime_factor_of_600851475143():
    n = 600851475143
    ## even number can not be prime
    ## checking range up to sqrt of 600851475143
    i = 2   # dividor, as soon as it is no longer divisable by two, i++ 
    while ( i <= math.sqrt(n) ):
        if (n % i == 0) :
            n = n / i
        else:
            i += 1

    return str(n)

if __name__ == "__main__":
    print( find_prime_factor_of_600851475143() )



