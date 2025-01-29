import argparse
import sqlite3
from pathlib import Path
from typing import Any, List, Union


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

    def add_entry(self, word: str, mean: str) -> None:
        cur = self.con.cursor()

        cur.execute(
            f"INSERT INTO {self.table} (word, meaning) VALUES (?, ?)",
            (word, mean),
        )

        self.con.commit()

    def search_word(self, word: str) -> List[Any]:
        cur = self.con.cursor()

        res = cur.execute(f"SELECT * FROM {self.table} WHERE word='{word}'")

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
        "-s", "--search-word", metavar="WORD", type=str, help="search a word"
    )

    return parser.parse_args()


def main() -> None:
    args = _parse_args()

    db = WordBookDB(args.database)

    if args.add_entry:
        word = args.add_entry[0]
        meaning = args.add_entry[1]
        db.add_entry(word, meaning)

    if args.search_word:
        results = db.search_word(args.search_word)
        if results:
            for result in results:
                print(f"{result[0]} : {result[1]}")
        else:
            print(f'No entry for the word "{args.search_word}"')


if __name__ == "__main__":
    main()
