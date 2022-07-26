import psycopg2

class Database:
    def __init__(self):
        self._conn = psycopg2.connect(host="localhost", user="apple", password="kumari12345", database="postgres")
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, query, params=None):
        self.cursor.execute(query, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.fetchall()