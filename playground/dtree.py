import argparse
import os
from pathlib import Path
from typing import List


def _parse_args() -> argparse.Namespace:
    """
    Parse commandline arguments.
    """
    parser = argparse.ArgumentParser(
        description="Print a directory tree of specified path"
    )

    parser.add_argument(
        "path",
        metavar="PATH",
        type=Path,
        default=Path("."),
        help="root path to see the directory tree",
    )
    parser.add_argument(
        "-d",
        "--max-depth",
        metavar="MAX_DEPTH",
        type=int,
        default=0,
        help="max depth to expand the directory tree. "
        "0 (default) is the current level and expand the next level by adding +1",
    )
    parser.add_argument(
        "-a", "--all", action="store_true", help="expand all sub-directories"
    )

    return parser.parse_args()


def _get_files(path: Path) -> List[Path]:
    """
    Get sorted list of files in a specified path.
    """
    return sorted([p for p in path.absolute().iterdir()])


def _get_path_expr(path: Path) -> str:
    """
    Get a file name/a directory name (with trailing slash).
    """
    if path.is_dir():
        return f"{str(path.name)}{os.sep}"

    return f"{str(path.name)}"


def _print_file_tree(
    path: Path, remaining_depth: int, indent: str = ""
) -> None:
    """
    Print file tree from a specified path.
    """
    files = _get_files(path)

    for f in files:
        branch = "`-" if f is files[-1] else "|-"

        print(f"{indent}{branch} {_get_path_expr(f)}")

        # Search sub-directories recursively while depth is remaining
        # If remaining_depth < 0, all sub-directories are searched
        if f.is_dir() and (remaining_depth != 0):
            tree_indent = "   " if f is files[-1] else "|  "

            _print_file_tree(f, (remaining_depth - 1), (indent + tree_indent))


def main() -> None:
    args = _parse_args()

    if not args.path.is_dir():
        print(f"[Error] {args.path} is not directory")
        return

    if args.max_depth < 0:
        print(f"[Error] MAX_DEPTH must be more than 0")
        return

    # Print the specified root
    print(f"{_get_path_expr(args.path)}")

    if args.all:
        _print_file_tree(args.path, -1)
    else:
        _print_file_tree(args.path, args.max_depth)


if __name__ == "__main__":
    main()
