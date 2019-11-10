from pyicloud import PyiCloudService
from two_way_auth import get_gps_from_iphone
import sqlite3

api = PyiCloudService('ychikara@unomaha.edu', 'Bakabaka0208')

# 緯度経度をリストで保存
gps = get_gps_from_iphone(api)


conn = sqlite3.connect('gps_log.sqlite3')
cur = conn.cursor()

path = './gps_log.sqlite3'


cur.execute('create table if not exists log(latitude text, longitude text )')
cur.execute(f'INSERT INTO log VALUES ({gps[0]}, {gps[1]})')
cur.execute("select * from log")
for row in cur:
    print(row[0])
conn.commit()
conn.close()


