from collections import Counter
from functools import reduce
import random
import time

def f(x, n):
    return (x * x + 1) % n

def gcd_ext(a, b, extended=False):
    if b == 0:
        return (a, 1, 0) if extended else a
    g, x1, y1 = gcd_ext(b, a % b, extended=True)
    x, y = y1, x1 - (a // b) * y1
    return (g, x, y) if extended else g

def legendre_symbol(a, p):
    if p <= 0 or p % 2 == 0:
        raise ValueError("p має бути непарним простим числом")

    a = a % p
    if a == 0:
        return 0
    if a == 1:
        return 1
    if a % 2 == 0:
        return legendre_symbol(a // 2, p) * (-1 if (p % 8 in (3, 5)) else 1)
    return legendre_symbol(p % a, a) * (-1 if (a % 4 == 3 and p % 4 == 3) else 1)

def solovay_strassen(n, k=5):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(2, n - 1)
        g = gcd_ext(a, n)
        if g > 1:
            return False

        jacobian = legendre_symbol(a, n) % n
        mod_exp = pow(a, (n - 1) // 2, n)

        if jacobian != mod_exp:
            return False

    return True

def pollard_rho(n):
    if n % 2 == 0:
        return 2

    for _ in range(5):
        x = random.randint(2, n - 1)
        y = x
        d = 1

        while d == 1:
            x = f(x, n)
            y = f(f(y, n), n)
            d = gcd_ext(abs(x - y), n)

        if 1 < d < n:
            return d

    return None

def full_pollard_factorization(n):
    factors = []

    def factorize(n):
        if n <= 1:
            return
        if solovay_strassen(n, 10):
            factors.append(n)
            return

        divisor = None
        while not divisor:
            divisor = pollard_rho(n)
            if divisor is None:
                print(f"Метод Полларда не зміг знайти дільник для {n}")
                return

        factors.append(divisor)
        factorize(n // divisor)

    factorize(n)
    return sorted(factors)

def canonical_factorization(n):
    factors = full_pollard_factorization(n)
    return dict(Counter(factors))
