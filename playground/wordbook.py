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
                mean STRING
            )
            """
        )

        self.con.commit()

    def add_entry(self, word: str, mean: str) -> None:
        cur = self.con.cursor()

        cur.execute(
            f"INSERT INTO {self.table} (word, mean) VALUES (?, ?)",
            (word, mean),
        )

        self.con.commit()

    def search_word(self, word: str) -> List[Any]:
        cur = self.con.cursor()

        res = cur.execute(f"SELECT * FROM {self.table} WHERE word='{word}'")

        return res.fetchall()

    def __del__(self):
        self.con.close()


def main() -> None:
    db = WordBookDB("wordbook.db")

    db.add_entry("hello", "こんにちは")

    print(db.search_word("hello"))


if __name__ == "__main__":
    main()
