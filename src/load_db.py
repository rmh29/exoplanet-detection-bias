"""
Clean the raw data and load it into a local SQLite database
"""

import sqlite3

from clean import clean, load_raw

DB_PATH = "data/exoplanets.db"


def build_database() -> None:
    df = clean(load_raw())
    with sqlite3.connect(DB_PATH) as conn:
        df.to_sql("planets", conn, if_exists="replace", index=False)
    print(f"Wrote {len(df)} planets to table 'planets' in {DB_PATH}")


if __name__ == "__main__":
    build_database()