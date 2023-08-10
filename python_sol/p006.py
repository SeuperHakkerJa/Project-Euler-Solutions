#
# Solution to Project Euler problem 6
#
# Author: Xiaochen Li
# Date: May 20, 2019
#
#
#

def square( n ) :
    return n * n



def sum_square_diff():
    sum_of_square = 0
    square_of_sum = 0
    for i in range( 100 ):
        sum_of_square += square( i );
        square_of_sum += i
    square_of_sum = square(square_of_sum)
    diff = square_of_sum - sum_of_square
    return diff
    






if __name__ == "__main__":
    print( sum_square_diff() ) 
