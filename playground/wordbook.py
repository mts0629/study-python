import argparse
import csv
import sqlite3
from pathlib import Path
from typing import Dict, List, Tuple, Union


class WordBookDB:
    """
    Word book database.
    """

    def __init__(self, file_name: Union[str, Path]):
        self.con = sqlite3.connect(Path(file_name))
        self.word_table = "words"
        self.meanings_table = "meanings"

        cur = self.con.cursor()
        # Word table
        cur.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.word_table}(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                word STRING NOT NULL
            )
            """
        )
        # Meanings table
        cur.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.meanings_table}(
                id SERIAL PRIMARY KEY,
                word_id INTEGER NOT NULL REFERENCES words(id),
                meaning STRING NOT NULL
            )
            """
        )
        self.con.commit()

    def add_entry(self, word: str, meaning: str) -> None:
        """
        Add new entry to the database.
        """
        cur = self.con.cursor()

        # Check whether a word already exists
        results = cur.execute(
            f"SELECT * FROM {self.word_table} WHERE word = '{word}'"
        )
        entry = results.fetchone()

        if not entry:
            # If not exist, insert the word into the word table
            cur.execute(
                f"INSERT INTO {self.word_table} (word) VALUES ('{word}')"
            )
            self.con.commit()
            results = cur.execute(
                f"SELECT * FROM {self.word_table} WHERE word = '{word}'"
            )
            entry = results.fetchone()

        # Insert a new meaning of the word (specified by ID) into the meanings table
        word_id = entry[0]
        cur.execute(
            f"INSERT INTO {self.meanings_table} (word_id, meaning) VALUES ({word_id}, '{meaning}')"
        )
        self.con.commit()

    def remove_entry(self, word: str) -> None:
        """
        Delete found entries from the database.
        """
        cur = self.con.cursor()

        entry = cur.execute(
            f"SELECT * FROM {self.word_table} WHERE word = '{word}'"
        ).fetchone()
        word_id = entry[0]

        cur.execute(
            f"DELETE FROM {self.word_table}"
            f" WHERE word LIKE '{self.__replace_wildcard(word)}'"
        )
        cur.execute(
            f"DELETE FROM {self.meanings_table} WHERE word_id = {word_id}"
        )
        self.con.commit()

    def __replace_wildcard(self, expr: str) -> str:
        """
        Replace wildcard characters: '*'/'?' to valid query for SQL 'LIKE' operator.
        """
        table = str.maketrans({"*": "%", "?": "_"})
        return expr.translate(table)

    def search_entries(self, word: str, meaning: str) -> Dict[str, List[str]]:
        """
        Search entries from the database.
        """
        word = "*" if word is None else word
        meaning = "*" if meaning is None else meaning

        cur = self.con.cursor()
        # Join a word and meanings from the tables
        entries = cur.execute(
            f"SELECT w.word, m.meaning"
            f" FROM {self.word_table} w"
            f" JOIN {self.meanings_table} m ON w.id = m.word_id"
            f" WHERE w.word LIKE '{self.__replace_wildcard(word)}'"
            f" AND m.meaning LIKE '{self.__replace_wildcard(meaning)}'"
            f" ORDER BY w.word"
        ).fetchall()

        # Create a dict which collects meanings for each word
        word_dict: Dict[str, List[str]] = {}
        for word, meaning in entries:
            if word not in word_dict.keys():
                word_dict[word] = []
            word_dict[word].append(meaning)

        return word_dict

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


def _print_entries(entries: Dict[str, List[str]]) -> None:
    """
    Print database entries.
    """
    # Column width by max. word/meaning length
    word_col_width = max([len(w) for w in entries.keys()])
    meaning_col_width = max(
        [max([len(m) for m in ms]) for ms in entries.values()]
    )

    # Header
    print(f"{'-' * word_col_width}---{'-' * meaning_col_width}")

    # Print word and meanings
    for word, meanings in entries.items():
        if len(meanings) == 1:
            print(f"{word:{word_col_width}} | {meanings[0]}")
        else:
            # If the word has multiple meanings, index and print them per line
            for i, meaning in enumerate(meanings):
                word_col = word if i == 0 else ""
                print(f"{word_col:{word_col_width}} | {i + 1}. {meaning}")

    # Footer
    print(f"{'-' * word_col_width}---{'-' * meaning_col_width}")


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
                # Insert new entries, skip existing one
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
