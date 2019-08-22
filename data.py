import sqlite3
from sqlite3 import Error
from helpers import fetch_price_data
import os


def return_conn():
    return sqlite3.connect('data.db')


def initial_retrieval():
    data = fetch_price_data()

    conn = return_conn()
    c = conn.cursor()

    # insert and commit to database
    for key, value in data.items():
        c.execute(
            'INSERT INTO prices(currency, price) VALUES (?,?)', (key, value))
    conn.commit()
    conn.close()


def initialize_db():
    exists = os.path.exists('data.db')

    if not exists:
        try:
            # create database
            conn = return_conn()
            c = conn.cursor()
            # create table in databse
            c.execute(
                'CREATE TABLE prices (id integer PRIMARY KEY, currency text unique,price real)')
        except Error as e:
            print(e)
        finally:
            return conn


def update_data():
    updated_prices = fetch_price_data()

    conn = return_conn()
    c = conn.cursor()

    # insert and commit to database
    for key, value in updated_prices.items():
        c.execute(
            'UPDATE prices SET price = ? WHERE currency = ?', (value, key))
    conn.commit()
    conn.close()
