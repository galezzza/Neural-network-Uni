import numpy as np
import random
import math


def DL(N: int, a: int) -> int:
    r = 1
    while True:
        if a ** r % N == 1:
            return r
        else:
            r += 1


def aFactorization(N: int) -> int:
    print(f'N: {N}')
    while True:
        a = random.randint(1, N - 1)
        gcd_res = math.gcd(N, a)

        if gcd_res > 1:

            print(f'gcd({N},{a}): {gcd_res}')
            return

        elif gcd_res == 1:

            r = DL(N, a)

            if 2 % r != 0:
                continue

            gcd_p = math.gcd(N, int(a ** (r / 2)) + 1)
            gcd_n = math.gcd(N, int(a ** (r / 2)) - 1)

            if gcd_p > 1 or gcd_n > 1:
                print(f'gcd({N},{int(a ** (r / 2)) + 1}), gcd({N},{int(a ** (r / 2)) - 1}): {gcd_p}, {gcd_n}')
                return

            elif gcd_p == 1 and gcd_n == 1:
                continue


data = [12, 91, 57, 143, 1737, 1859, 13843]

for N in data:
    aFactorization(N)



