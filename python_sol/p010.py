#
# Solution to Project Euler problem 10
#
# Author: Xiaochen Li
# Date: May 24, 2019
#
#

def sieve_of_eratosthenes(n):
    
    list_of_prime = list( range( 2, n+1 )) # all nun between 2 - n
    prime = 2 # first prime number

    while ( prime**2 <= n ):
        if prime in list_of_prime:

            # cross off all multiples of each prime number
            for i in range( prime**2, n+1, prime ):
                if i in list_of_prime:
                    list_of_prime.remove( i )
        # go to next prime number
        prime+=1
    return list_of_prime


if __name__ == "__main__":
    print( sieve_of_eratosthenes( 2000000 ) )




