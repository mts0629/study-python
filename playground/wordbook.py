import argparse
import sqlite3
from pathlib import Path
from typing import List, Tuple, Union


class WordBookDB:
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
        cur = self.con.cursor()
        cur.execute(
            f"INSERT INTO {self.table} (word, meaning) VALUES (?, ?)",
            (word, meaning),
        )
        self.con.commit()

    def __replace_wildcard(self, expr: str) -> str:
        return expr.translate(str.maketrans({"*": "%", "?": "_"}))

    def search_words(self, word: str) -> List[Tuple[str, str]]:
        cur = self.con.cursor()
        res = cur.execute(
            f"SELECT * FROM {self.table} WHERE word LIKE '{self.__replace_wildcard(word)}'"
        )
        return res.fetchall()

    def search_meanings(self, meaning: str) -> List[Tuple[str, str]]:
        cur = self.con.cursor()
        res = cur.execute(
            f"SELECT * FROM {self.table} WHERE meaning LIKE '{self.__replace_wildcard(meaning)}'"
        )
        return res.fetchall()

    def __del__(self):
        self.con.close()


def _parse_args() -> argparse.Namespace:
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


def main() -> None:
    args = _parse_args()

    db = WordBookDB(args.database)

    if args.add_entry:
        word, meaning = args.add_entry
        db.add_entry(word, meaning)

    if args.search_word:
        results = db.search_words(args.search_word)
        if results:
            for result in results:
                print(f"{result[0]} : {result[1]}")
        else:
            print(f'No entry for the word "{args.search_word}"')

    if args.search_meaning:
        results = db.search_meanings(args.search_meaning)
        if results:
            for result in results:
                print(f"{result[0]} : {result[1]}")
        else:
            print(f'No entry for the meaning "{args.search_meaning}"')


if __name__ == "__main__":
    main()
