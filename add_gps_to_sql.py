from pyicloud import PyiCloudService
from two_way_auth import get_gps_from_iphone
import sqlite3
from cal_rho import cal_rho

api = PyiCloudService('ychikara@unomaha.edu', 'Bakabaka0208')

# 緯度経度をリストで保存
gps = get_gps_from_iphone(api)

conn = sqlite3.connect('gps_log.sqlite')
cur = conn.cursor()

path = './gps_log.sqlite3'


cur.execute('create table if not exists log(latitude text, longitude text )')
# cur.execute('delete from log')
cur.execute(f'INSERT INTO log VALUES (?, ?)', (gps[0], gps[1]))
cur.execute("select * from log")
cur.execute('select count(*) from log')
results = cur.fetchall()[0][0]

if results > 2:
    cur.execute('select * from log limit 1 offset 0')
    print(list(cur))

# cur.execute('select * from log')
gps_list = list(cur)
distance = 0
for i in range(0, results - 2):
    lat_a, lon_a, lat_b, lon_b = int(gps_list[i][0]), int(gps_list[i][1]), int(gps_list[i + 1][0]), int(gps_list[i + 1][1])
    cal_rho(lat_a, lon_a, lat_b, lon_b)
    distance += cal_rho()
print(distance)

# for row in cur:
#     print(row[0], row[1])


conn.commit()
conn.close()
