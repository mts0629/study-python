import argparse
import calendar
from datetime import datetime


def _parse_args() -> argparse.Namespace:
    today = datetime.today()

    parser = argparse.ArgumentParser(description="print a calendar")
    parser.add_argument(
        "-y",
        "--year",
        type=int,
        default=today.year,
        help="year to print (1-9999, this year in default)",
    )
    parser.add_argument(
        "-m",
        "--month",
        type=int,
        default=today.month,
        help="month to print (1-12, this month in default)",
    )
    parser.add_argument(
        "-a",
        "--annual",
        action="store_true",
        help="annual calendar",
    )

    return parser.parse_args()


def main() -> None:
    args = _parse_args()

    if (args.year < 1) or (args.year > 9999):
        print("Error: year is invalid (within 1-9999)")
        return
    if (args.month < 1) or (args.month > 12):
        print("Error: month is invalid (within 1-12)")
        return

    if args.annual:
        print(calendar.calendar(args.year))
    else:
        print(calendar.month(args.year, args.month))


if __name__ == "__main__":
    main()
