import psycopg2

import config


class DatabaseManager:
    def __init__(self, dbname: str, user: str, password: str, host: str):
        self.conn = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host
        )
        self.cur = self.conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Exception has been caught. {exc_type}, {exc_val}, {exc_tb}")
        self.cur.close()
        self.conn.close()

    def create_table(self):
        try:
            self.cur.execute(config.CREATE_TABLE)
            self.conn.commit()
        except psycopg2.Error as e:
            print(f"An error occurred while creating the table: {e}")
            self.conn.rollback()
