# import sympy, numpy as np
# from utils import timeout

# BASE = 10 ** 14
# UBOUND = 100000
# MOD = 1234567891011

# def sieve_of_eratosthenes(limit):
#     sieve = [True] * (limit + 1)
#     sieve[0] = sieve[1] = False
#     for i in range(2, int(limit**0.5) + 1):
#         if sieve[i]:
#             sieve[i*i: limit+1: i] = [False] * len(range(i*i, limit+1, i))
#     return [x for x in range(limit + 1) if sieve[x]]

# def a():
#     idx = 1
#     n = BASE
#     prime_limit = 10**6  # Adjust based on your requirements
#     primes = sieve_of_eratosthenes(prime_limit)
#     while idx <= UBOUND:
#         while n not in primes:
#             n += 1
#         yield n
#         idx += 1
#         n += 1



# def fib(n, mod):
#     if n == 0:
#         return 0, 1
#     else:
#         a, b = fib(n // 2, mod)
#         c = a * ((b * 2) - a) % mod
#         d = (a * a + b * b) % mod
#         return (d, c) if n % 2 else (c, d)



# @timeout(report_time=True)
# def compute():
#     primonacci_sum = 0
#     for num in a():
#         fibonacci, _ = fib(num, MOD)
#         primonacci_sum += fibonacci
#         primonacci_sum %= MOD
#     return str(primonacci_sum)



# print(compute())

def compute():
    BASE = 10**14
    SEARCH_RANGE = 10000000
    MODULUS = 1234567891011
    
    # Sieve of Eratosthenes, but starting at BASE
    iscomposite = [False] * SEARCH_RANGE
    primes = list_primes(int((BASE + SEARCH_RANGE)**0.5))
    for p in primes:
        for i in range((BASE + p - 1) // p * p - BASE, len(iscomposite), p):
            iscomposite[i] = True

    # Returns p - BASE, where p is the next prime after n + BASE
    def next_prime(n):
        while True:
            n += 1
            if n >= len(iscomposite):
                raise AssertionError("Search range exhausted")
            if not iscomposite[n]:
                return n
    
    ans = 0
    p = 0
    for i in range(100000):
        p = next_prime(p)
        ans = (ans + fibonacci_mod(BASE + p, MODULUS)) % MODULUS
    return str(ans)

def list_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            sieve[i*i: limit+1: i] = [False] * len(range(i*i, limit+1, i))
    return [x for x in range(limit + 1) if sieve[x]]

def fibonacci_mod(n, mod):
    a, b = 0, 1
    binary = bin(n)[2:]
    for bit in binary:
        a, b = a * (b * 2 - a), a * a + b * b
        if bit == "1":
            a, b = b, a + b
        a %= mod
        b %= mod
    return a

if __name__ == "__main__":
    print(compute())
