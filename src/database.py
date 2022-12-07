import os
import sys
import sqlite3

def cwd_path(file_name: str) -> str:
    return os.path.join(os.getcwd(), file_name)

class Row:
    def __init__(self, values: dict[str]) -> None:
        self.values = {}


class Table:
    def __init__(self, name: str, columns: list[str], rows: list[Row]) -> None:
        self.name = name
        self.columns = columns
        self.rows = rows


class Database:
    def __init__(self, name: str) -> None:
        self.name = name
        self.db_path = cwd_path(f"databases/{self.name}.db")
        self.__conn = sqlite3.connect(self.db_path)
        self.tables = self._load_tables()


    def _load_tables(self) -> dict[str, Table]:
        res = self.__conn.execute(
            """
            SELECT name FROM sqlite_schema
            WHERE type='table'
            """
        )

        table_names = [t[0] for t in res.fetchall() if not t[0].startswith("sqlite")]

        tables = {}

        for t in table_names:
            res = self.__conn.execute(
                """
                SELECT name FROM pragma_table_info(?)
                ORDER BY cid
                """, [t]
            )

            column_names = [c[0] for c in res.fetchall()]

            res = self.__conn.execute(
                f"""
                SELECT * FROM {t}
                """,
            )

            rows = [Row({c: r[i] for i, c in enumerate(column_names)}) for r in res.fetchall()]

            tables[t] = Table(t, column_names, rows)

        return tables


d = Database("test")
print(d.tables["table1"].columns)