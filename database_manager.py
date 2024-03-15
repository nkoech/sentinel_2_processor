import psycopg2


class DatabaseManager:
    def __init__(self, dbname: str, user: str, password: str, host: str):
        self.conn = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host
        )
        self.cur = self.conn.cursor()
