import psycopg2
import os
import json

def get_conn():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="admin",
        password="admin",
        port=5432
    )

def insert_json(table, data):
    conn = get_conn()
    cur = conn.cursor()

    for row in data:
        cols = ",".join(row.keys())
        vals = ",".join(["%s"] * len(row))
        cur.execute(
            f"INSERT INTO {table} ({cols}) VALUES ({vals})",
            list(row.values())
        )

    conn.commit()
    cur.close()
    conn.close()


def fetch_all(query):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows