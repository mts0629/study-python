import sqlite3


def main() -> None:
    """
    SQLite test.
    """
    con = sqlite3.connect("test.db")

    cur = con.cursor()
    cur.execute("CREATE TABLE persons(name, age)")
    cur.execute("INSERT INTO persons VALUES " "('John', 20)," "('Mary', 22)")
    con.commit()

    res = cur.execute("SELECT name FROM persons")
    print(res.fetchall())

    con.close()


if __name__ == "__main__":
    main()
