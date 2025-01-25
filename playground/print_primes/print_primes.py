#!/usr/bin/python

import argparse
import time
from functools import partial
from typing import Callable, List


def _test_naive(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def _test_by_sqrt(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def _trial_division(
    test_func: Callable[[int], bool], n: int, 
) -> List[int]:
    prime_numbers = []
    for i in range(2, (n + 1)):
        if test_func(i):
            prime_numbers.append(i)

    return prime_numbers


def _sieve_of_eratosthenes(n: int) -> List[int]:
    # Flags for numbers <= n
    # when flags[n] = True, n is prime
    flags = [True] * (n + 1)
    # 0, 1 aren't prime
    flags[0] = flags[1] = False

    p = 2
    while p * p <= n:
        # Multiples of p aren't prime
        mult_p = p * p
        while mult_p <= n:
            flags[mult_p] = False
            mult_p += p

        # Get the next number with True
        while True:
            p += 1
            if flags[p]:
                break

    # Return numbers which flag is True
    return [n for n, flag in enumerate(flags) if flag]


def _get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Print prime numbers from 1 to N"
    )

    parser.add_argument(
        "n",
        metavar="N",
        type=int,
        help="maximum number to find prime numbers (>= 2)"
    )
    parser.add_argument(
        "--by_sqrt",
        action="store_true",
        help="adopt trial division by sqrt(n)"
    )
    parser.add_argument(
        "--sieve",
        action="store_true",
        help="adopt \"Sieve of Eratosthenes\""
    )

    return parser.parse_args()


def main() -> None:
    args = _get_args()

    if args.n < 2:
        print("Number must be >= 2")
        return

    if args.sieve:
        get_prime_numbers = _sieve_of_eratosthenes
    else:
        test_func = _test_by_sqrt if args.by_sqrt \
            else _test_naive

        get_prime_numbers = partial(_trial_division, test_func)


    print(f"Prime numbers by {args.n}:")

    start = time.time()
    prime_numbers = get_prime_numbers(args.n)
    end = time.time()
        
    print(prime_numbers)
    print(f"{len(prime_numbers)} numbers")
    print(f"Elapsed: {end - start}[sec]")


if __name__ == "__main__":
    main()
