#!/usr/bin/python

import argparse
import math


def is_prime(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def _get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "n", metavar="NUMBER",
        type=int,
        help="integer (more than 2)"
    )

    return parser.parse_args()


def main() -> None:
    args = _get_args()

    if args.n < 2:
        print("Number must be more than 2")
        return

    print(f"Prime numbers until {args.n}:")
    for i in range(2, (args.n + 1)):
        if is_prime(i):
            print(i)
        

if __name__ == "__main__":
    main()
