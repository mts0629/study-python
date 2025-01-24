#!/usr/bin/python

import argparse
import time
from typing import Callable, List


def _trial_division_naive(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def _trial_division_by_sqrt(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def _get_prime_numbers_by_n(
    n: int, is_prime: Callable[[int], bool]
) -> List[int]:
    prime_numbers = []
    for i in range(2, (n + 1)):
        if is_prime(i):
            prime_numbers.append(i)

    return prime_numbers


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

    return parser.parse_args()


def main() -> None:
    args = _get_args()

    if args.n < 2:
        print("Number must be >= 2")
        return

    test_func = _trial_division_by_sqrt if args.by_sqrt \
        else _trial_division_naive

    print(f"Prime numbers by {args.n}:")

    start = time.time()
    prime_numbers = _get_prime_numbers_by_n(args.n, test_func)
    end = time.time()
        
    print(prime_numbers)
    print(f"Elapsed: {end - start}[sec]")

if __name__ == "__main__":
    main()
