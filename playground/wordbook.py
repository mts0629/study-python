import argparse
import csv
import sqlite3
from pathlib import Path
from typing import List, Tuple, Union


class WordBookDB:
    """
    Word book database.
    """

    def __init__(self, file_name: Union[str, Path]):
        self.con = sqlite3.connect(Path(file_name))
        self.table = "wordbook"

        cur = self.con.cursor()
        cur.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table}(
                word STRING,
                meaning STRING
            )
            """
        )

        self.con.commit()

    def add_entry(self, word: str, meaning: str) -> None:
        """
        Add new entry to the database.
        """
        cur = self.con.cursor()
        cur.execute(
            f"INSERT INTO {self.table} (word, meaning) VALUES (?, ?)",
            (word, meaning),
        )
        self.con.commit()

    def remove_entry(self, word: str) -> None:
        """
        Delete found entries from the database.
        """
        cur = self.con.cursor()
        cur.execute(
            f"DELETE FROM {self.table}"
            f" WHERE word LIKE '{self.__replace_wildcard(word)}'"
        )
        self.con.commit()

    def __replace_wildcard(self, expr: str) -> str:
        """
        Replace wildcard characters: '*'/'?' to valid query for SQL 'LIKE' operator.
        """
        table = str.maketrans({"*": "%", "?": "_"})
        return expr.translate(table)

    def search_entries(self, word: str, meaning: str) -> List[Tuple[str, str]]:
        """
        Search entries from the database.
        """
        word = "*" if word is None else word
        meaning = "*" if meaning is None else meaning

        cur = self.con.cursor()
        results = cur.execute(
            f"SELECT * FROM {self.table}"
            f" WHERE word LIKE '{self.__replace_wildcard(word)}'"
            f" AND meaning LIKE '{self.__replace_wildcard(meaning)}'"
        )

        return sorted(results.fetchall())

    def __del__(self):
        self.con.close()


def _parse_args() -> argparse.Namespace:
    """
    Parse commandline arguments.
    """
    parser = argparse.ArgumentParser(
        description="Word book by SQLite database"
    )

    parser.add_argument(
        "-d",
        "--database",
        type=Path,
        default="./wordbook.db",
        help='path to sqlite DB file (default: "./wordbook.db")',
    )
    parser.add_argument(
        "-e",
        "--add-entry",
        type=str,
        metavar=("WORD", "MEANING"),
        nargs=2,
        help="add new entry by pair of word and its meaning",
    )
    parser.add_argument(
        "-f",
        "--add-csv-entry",
        type=Path,
        metavar="CSV_PATH",
        help="add new entry by pair of word and its meaning, in CSV file",
    )
    parser.add_argument(
        "-r",
        "--remove-entry",
        type=str,
        metavar="WORD",
        help="remove specified word from the DB",
    )
    parser.add_argument(
        "-w",
        "--search-word",
        metavar="WORD",
        type=str,
        help="search a word, wildcard ('*'/'?') can be used",
    )
    parser.add_argument(
        "-m",
        "--search-meaning",
        metavar="MEANING",
        type=str,
        help="search a word by meaning, wildcard ('*'/'?') can be used",
    )

    return parser.parse_args()


def _get_csv_rows(csv_file: Path) -> List[List[str]]:
    """
    Get rows in a CSV file.
    """
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
    return rows


def _print_entries(entries: List[Tuple[str, str]]) -> None:
    """
    Print database entries.
    """
    for word, meaning in entries:
        print(f"{word} : {meaning}")


def main() -> None:
    args = _parse_args()

    db = WordBookDB(args.database)

    if args.add_entry:
        word, meaning = args.add_entry
        db.add_entry(word, meaning)

    if args.add_csv_entry:
        csv_file = args.add_csv_entry
        if not csv_file.exists():
            print(f'File not found: "{csv_file}"')
        else:
            rows = _get_csv_rows(csv_file)
            for row in rows:
                word, meaning = row[0], row[1]
                if not db.search_entries(word, meaning):
                    db.add_entry(word, meaning)

    if args.remove_entry:
        word = args.remove_entry

        results = db.search_entries(word, args.search_meaning)
        if results:
            print("Found words:")
            _print_entries(results)

            while True:
                yn = input(
                    "Do you want to remove these words? (y/n): "
                ).lower()
                if yn == "y":
                    db.remove_entry(word)
                    break
                elif yn == "n":
                    print("Cancelled")
                    break
                else:
                    print("Error: please input y/Y/n/N")
        else:
            print("No matching words")

    if args.search_word or args.search_meaning:
        results = db.search_entries(args.search_word, args.search_meaning)
        if results:
            _print_entries(results)
        else:
            print("No matching words")


if __name__ == "__main__":
    main()
