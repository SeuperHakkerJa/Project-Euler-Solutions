# 
# Solution to Project Euler problem 2
#
# Author: Xiaochen Li
# Date: May 04, 2019
#
#
# Problem: By considering the terms in the Fibonacci sequence whose values
#          do not exceed four million, find the sum of the even-valued terms.
#          ( starting from 1, 2, 3, 5 ... )
def find_even_fibo_under_4M():

    bound = 4000000

    fibo_operation = [1,2]
    fibo_list = []

    while(fibo_operation[1] < bound ):


        if ( fibo_operation[1] % 2 == 0 ):
            fibo_list.append(fibo_operation[1])

        temp = fibo_operation[0]
        fibo_operation[0] = fibo_operation[1]
        fibo_operation[1] += temp

    return str(sum(fibo_list))





if __name__ == "__main__":
    print( find_even_fibo_under_4M() )

