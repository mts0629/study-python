#!/usr/bin/python

import argparse
import math
import time


def is_prime(n: int) -> bool:
    root_n = math.floor(math.sqrt(n))
    for i in range(2, root_n):
        if n % i == 0:
            return False
    return True


def _get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Print prime numbers from 1 to N"
    )

    parser.add_argument(
        "n",
        metavar="N",
        type=int,
        help="maximum number to be checked (> 2)"
    )

    return parser.parse_args()


def main() -> None:
    args = _get_args()

    if args.n < 2:
        print("Number must be more than 2")
        return

    print(f"Prime numbers until {args.n}:")
    start = time.time()

    for i in range(2, (args.n + 1)):
        if is_prime(i):
            print(i)

    end = time.time()
    print(f"Elapsed: {end - start}[sec]")
        

if __name__ == "__main__":
    main()
