#
# Solution to Project Euler problem 301
#
# Author: Xiaochen Li
# Date: August 11, 2023
#
#
# Nim is a game played with heaps of stones, where two players take it in turn to
# remove any number of stones from any heap until no stones remain.
#
# We'll consider the three-heap normal-play version of Nim, which works as follows:
# - At the start of the game there are three heaps of stones.
# - On each player's turn, the player may remove any positive number of stones
#   from any single heap.
# - The first player unable to move (because no stones remain) loses.
#
# If (n1,n2,n3) indicates a Nim position consisting of heaps of size n1, n2, and
# n3, then there is a simple function, which you may look up or attempt to deduce
# for yourself, X(n1,n2,n3) that returns:
# - zero if, with perfect strategy, the player about to move will eventually lose; or
# - non-zero if, with perfect strategy, the player about to move will eventually win.
#
# For example X(1,2,3) = 0 because, no matter what the current player does, the
# opponent can respond with a move that leaves two heaps of equal size, at which
# point every move by the current player can be mirrored by the opponent until no
# stones remain; so the current player loses. To illustrate:
# - current player moves to (1,2,1)
# - opponent moves to (1,0,1)
# - current player moves to (0,0,1)
# - opponent moves to (0,0,0), and so wins.
#
# For how many positive integers n <= 2^30 does X(n,2n,3n) = 0?




from utils import timeout
@timeout(report_time=True)
def compute():
    a = 0
    b = 1
    for i in range(32):
        a, b = b, a + b
    return str(a)

import numpy as np

# @timeout(report_time=True)
# def fib(n):
#     for _ in range(1000000):
#         F = np.array([[1, 1], [1, 0]], dtype=np.int64)
#     return np.linalg.matrix_power(F, n - 1)[0, 0]


# n = 32
# print(fib(n))  
print(compute())
# if __name__ == "__main__":
# 	print(compute())