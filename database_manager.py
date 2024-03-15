from datetime import date
import typing

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

    def insert_values(self, values: typing.List[typing.Dict[str, float]]):
        for value in values:
            try:
                self.cur.execute(
                    config.INSERT_VALUES_QUERY,
                    (date.today(), value["min"], value["max"], value["mean"], value["median"], value["std"],),
                )
                self.conn.commit()
                print(f"Values {value} inserted successfully.")
            except psycopg2.Error as e:
                print(f"An error occurred while inserting the values: {e}")
                self.conn.rollback()
