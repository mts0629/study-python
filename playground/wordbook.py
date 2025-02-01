import argparse
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
                word STRING PRIMARY KEY,
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

        return results.fetchall()

    def __del__(self):
        self.con.close()


def _parse_args() -> argparse.Namespace:
    """
    Parse commandline arguments.
    """
    parser = argparse.ArgumentParser(description="Wordbook by sqlite")

    parser.add_argument(
        "-d",
        "--database",
        type=Path,
        default="./wordbook.db",
        help='path to sqlite DB file (default: "./wordbook.db")',
    )
    parser.add_argument(
        "-a",
        "--add-entry",
        type=str,
        metavar=("WORD", "MEANING"),
        nargs=2,
        help="add new entry, pair of word and its meaning",
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


def _print_entries(entries: List[Tuple[str, str]]) -> None:
    """
    Print database entries.
    """
    for entry in entries:
        print(f"{entry[0]} : {entry[1]}")


def main() -> None:
    args = _parse_args()

    db = WordBookDB(args.database)

    if args.add_entry:
        word, meaning = args.add_entry
        db.add_entry(word, meaning)

    if args.search_word or args.search_meaning:
        results = db.search_entries(args.search_word, args.search_meaning)
        if results:
            _print_entries(results)
        else:
            print("No matching entries")


if __name__ == "__main__":
    main()
