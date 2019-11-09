import sqlite3
import os

path = "./test_sql.sqlitte3"
conn = sqlite3.connect('test_sql.sqlite3')
cur = conn.cursor()
if os.path.exists(path):
    cur.executescript('create table GPS_log (longitude integer, latitude integer, place text)')

conn.commit()
cur.close()
